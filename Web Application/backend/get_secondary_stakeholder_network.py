from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_secondary_stakeholder_network(query: str, primaryStakeholder: str, access: str):
    if access == 'levelone':
        cypher = """
            MATCH (doc:PUBLICATION_LONE_Document {name: $query})
            MATCH (doc)-[:PUBLICATION_LONE_HAS_AUTHOR]->(author:PUBLICATION_LONE_Author)
            MATCH (author)-[:PUBLICATION_LONE_HAS_YEAR]->(year:PUBLICATION_LONE_Year)
            MATCH (year)-[:PUBLICATION_LONE_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_LONE_PrimaryFormalName {name: $primaryStakeholder})
            MATCH (primary)-[:PUBLICATION_LONE_HAS_TAG]->(tag:PUBLICATION_LONE_Tag)
            MATCH (tag)-[:PUBLICATION_LONE_POINTS_TO_SECONDARY]->(secondary:PUBLICATION_LONE_SecondaryFormalName)

            RETURN DISTINCT 
                elementId(doc) AS id_doc, doc.doc AS label_doc, 'Document' AS type_doc,
                elementId(author) AS id_author, author.name AS label_author, 'Author' AS type_author,
                elementId(year) AS id_year, year.value AS label_year, 'Year' AS type_year,
                elementId(primary) AS id_primary, primary.name AS label_primary, 'Primary Stakeholder' AS type_primary,
                elementId(tag) AS id_tag, tag.name AS label_tag, tag.context AS tooltip_tag, 'Tag' AS type_tag,
                elementId(secondary) AS id_secondary, secondary.name AS label_secondary, 'Secondary Stakeholder' AS type_secondary
        """
    elif access == 'leveltwo':
        cypher = """
            MATCH (doc:PUBLICATION_LTWO_Document {name: $query})
            MATCH (doc)-[:PUBLICATION_LTWO_HAS_AUTHOR]->(author:PUBLICATION_LTWO_Author)
            MATCH (author)-[:PUBLICATION_LTWO_HAS_YEAR]->(year:PUBLICATION_LTWO_Year)
            MATCH (year)-[:PUBLICATION_LTWO_HAS_PRIMARY_LABEL]->(primary:PUBLICATION_LTWO_PrimaryLabel {name: $primaryStakeholder})
            MATCH (primary)-[:PUBLICATION_LTWO_HAS_TAG]->(tag:PUBLICATION_LTWO_Tag)
            MATCH (tag)-[:PUBLICATION_LTWO_POINTS_TO_SECONDARY]->(secondary:PUBLICATION_LTWO_SecondaryLabel)

            RETURN DISTINCT 
                elementId(doc) AS id_doc, doc.doc AS label_doc, 'Document' AS type_doc,
                elementId(author) AS id_author, author.name AS label_author, 'Author' AS type_author,
                elementId(year) AS id_year, year.value AS label_year, 'Year' AS type_year,
                elementId(primary) AS id_primary, primary.name AS label_primary, 'Primary Label' AS type_primary,
                elementId(tag) AS id_tag, tag.name AS label_tag, tag.context AS tooltip_tag, 'Tag' AS type_tag,
                elementId(secondary) AS id_secondary, secondary.name AS label_secondary, 'Secondary Label' AS type_secondary
        """

    try:
        with driver.session() as session:
            results = session.run(cypher, {
                "query": query,
                "primaryStakeholder": primaryStakeholder
            })

            nodes = {}
            links = []

            for record in results:
                entities = [
                    ('doc', 'Document'),
                    ('author', 'Author'),
                    ('year', 'Year'),
                    ('primary', 'Primary Stakeholder' if access == 'levelone' else 'Primary Label'),
                    ('tag', 'Tag'),
                    ('secondary', 'Secondary Stakeholder' if access == 'levelone' else 'Secondary Label')
                ]

                for key, _ in entities:
                    node_id = record[f"id_{key}"]
                    node_label = record[f"label_{key}"]
                    node_type = record[f"type_{key}"]
                    tooltip = record.get(f"tooltip_{key}", node_label)
                    if node_id not in nodes:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": node_label,
                            "type": node_type,
                            "tooltip": tooltip
                        }

                links.append({"source": record["id_doc"], "target": record["id_author"], "type": "HAS_AUTHOR"})
                links.append({"source": record["id_author"], "target": record["id_year"], "type": "HAS_YEAR"})
                links.append({"source": record["id_year"], "target": record["id_primary"], "type": "HAS_PRIMARY"})
                links.append({"source": record["id_primary"], "target": record["id_tag"], "type": "HAS_TAG"})
                links.append({"source": record["id_tag"], "target": record["id_secondary"], "type": "POINTS_TO_SECONDARY"})

            print(f"\n✅ Total nodes: {len(nodes)}, Total links: {len(links)}")

            return {
                "graph": {
                    "nodes": list(nodes.values()),
                    "links": links
                }
            }

    except Exception as e:
        print("❌ Error fetching network data:", e)
        raise
