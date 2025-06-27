from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_secondary_stakeholder(query: str, primaryStakeholder: str, access:str):
    if access == 'levelone':
        cypher = """
            MATCH (doc:PUBLICATION_LONE_Document {name: $query})
            MATCH (doc)-[:PUBLICATION_LONE_HAS_AUTHOR]->(author:PUBLICATION_LONE_Author)
            MATCH (author)-[:PUBLICATION_LONE_HAS_YEAR]->(year:PUBLICATION_LONE_Year)
            MATCH (year)-[:PUBLICATION_LONE_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_LONE_PrimaryFormalName {name: $primaryStakeholder})
            MATCH (primary)-[:PUBLICATION_LONE_HAS_TAG]->(tag:PUBLICATION_LONE_Tag)
            MATCH (tag)-[:PUBLICATION_LONE_POINTS_TO_SECONDARY]->(secondary:PUBLICATION_LONE_SecondaryFormalName)
            OPTIONAL MATCH (primary)-[:PUBLICATION_LONE_HAS_PRIMARY_CATEGORY]->(primaryCategory:PUBLICATION_LONE_PrimaryCategory)
            OPTIONAL MATCH (secondary)-[:PUBLICATION_LONE_HAS_SECONDARY_CATEGORY]->(secondaryCategory:PUBLICATION_LONE_SecondaryCategory)

            RETURN DISTINCT
                doc.doc AS Document,
                author.name AS Author,
                year.value AS Year,
                primary.name AS `Primary Stakeholder`,
                primaryCategory.name AS `Primary Category`,
                secondary.name AS `Secondary Stakeholder`,
                secondaryCategory.name AS `Secondary Category`,
                tag.name AS Tag,
                tag.context AS Context
            ORDER BY `Secondary Stakeholder`
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
                doc.doc AS Document,
                author.name AS Author,
                year.value AS Year,
                primary.name AS `Primary Stakeholder`,
                NULL AS `Primary Category`,
                secondary.name AS `Secondary Stakeholder`,
                NULL AS `Secondary Category`,
                tag.name AS Tag,
                tag.context AS Context
            ORDER BY `Secondary Stakeholder`
        """

    with driver.session() as session:
        results = session.run(cypher, {
            "query": query,
            "primaryStakeholder": primaryStakeholder
        })
        table = []
        for record in results:
            table.append({
                "Document": record["Document"],
                "Author" : record["Author"],
                "Year" : record["Year"],
                "Primary Stakeholder": record["Primary Stakeholder"],
                "Primary Category" : record["Primary Category"],
                "Secondary Stakeholder" : record["Secondary Stakeholder"],
                "Secondary Category" : record["Secondary Category"],
                "Tag" : record["Tag"],
                "Context" : record["Context"]
            })
        return table