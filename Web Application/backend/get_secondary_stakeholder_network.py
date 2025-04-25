from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_secondary_stakeholder_network(query: str, primaryStakeholder: str):
    cypher = """
        MATCH (doc:PUBLICATION_Document {identifier: $query})
            -[:PUBLICATION_HAS_AUTHOR]->(author:PUBLICATION_Author)
            -[:PUBLICATION_HAS_YEAR]->(year:PUBLICATION_Year)
            -[:PUBLICATION_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_PrimaryStakeholder {name: $primaryStakeholder})
            -[:PUBLICATION_HAS_TAG]->(tag:PUBLICATION_Tag)
            -[:PUBLICATION_POINTS_TO_SECONDARY]->(secondary:PUBLICATION_SecondaryStakeholder)
            -[:PUBLICATION_HAS_CONTEXT]->(context:PUBLICATION_Context)
        RETURN DISTINCT 
            id(doc) AS id_doc, doc.name AS label_doc, 'Document' AS type_doc,
            id(author) AS id_author, author.name AS label_author, 'Author' AS type_author,
            id(year) AS id_year, year.name AS label_year, 'Year' AS type_year,
            id(primary) AS id_primary, primary.name AS label_primary, 'Primary Stakeholder' AS type_primary,
            id(tag) AS id_tag, tag.name AS label_tag, 'Tag' AS type_tag,
            id(secondary) AS id_secondary, secondary.name AS label_secondary, 'Secondary Stakeholder' AS type_secondary
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
                # Define all node types to handle
                entities = [
                    ('doc', 'Document'),
                    ('author', 'Author'),
                    ('year', 'Year'),
                    ('primary', 'Primary Stakeholder'),
                    ('tag', 'Tag'),
                    ('secondary', 'Secondary Stakeholder')
                ]

                # Add all unique nodes
                for key, _ in entities:
                    node_id = record[f"id_{key}"]
                    node_label = record[f"label_{key}"]
                    node_type = record[f"type_{key}"]
                    if node_id not in nodes:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": node_label,
                            "type": node_type
                        }

                # Create links to reflect relationships in the graph
                links.append({"source": record["id_doc"], "target": record["id_author"], "type": "HAS_AUTHOR"})
                links.append({"source": record["id_author"], "target": record["id_year"], "type": "HAS_YEAR"})
                links.append({"source": record["id_year"], "target": record["id_primary"], "type": "HAS_PRIMARY_STAKEHOLDER"})
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
