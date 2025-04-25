from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_secondary_stakeholder(query: str, primaryStakeholder: str):
    cypher = """
        MATCH (doc:PUBLICATION_Document {identifier: $query})
            -[:PUBLICATION_HAS_AUTHOR]->(author:PUBLICATION_Author)
            -[:PUBLICATION_HAS_YEAR]->(year:PUBLICATION_Year)
            -[:PUBLICATION_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_PrimaryStakeholder {name: $primaryStakeholder})
            -[:PUBLICATION_HAS_TAG]->(tag:PUBLICATION_Tag)
            -[:PUBLICATION_POINTS_TO_SECONDARY]->(secondary:PUBLICATION_SecondaryStakeholder)
            -[:PUBLICATION_HAS_CONTEXT]->(context:PUBLICATION_Context)
        RETURN DISTINCT
            doc.name AS Document,
            author.name AS Author,
            year.value AS Year,
            primary.name AS `Primary Stakeholder`,
            secondary.name AS `Secondary Stakeholder`,
            tag.name AS Tag,
            context.text AS Context
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
                "Secondary Stakeholder" : record["Secondary Stakeholder"],
                "Tag" : record["Tag"],
                "Context" : record["Context"]
            })
        return table