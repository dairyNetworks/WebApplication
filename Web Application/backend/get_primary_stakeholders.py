from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_primary_stakeholders(query: str):
    cypher = """
        MATCH (doc:PUBLICATION_Document {identifier: $query})-[:PUBLICATION_HAS_AUTHOR]->(:PUBLICATION_Author)
            -[:PUBLICATION_HAS_YEAR]->(:PUBLICATION_Year)
            -[:PUBLICATION_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_PrimaryStakeholder)
        RETURN DISTINCT primary.name AS PrimaryStakeholder
        ORDER BY primary.name
    """

    with driver.session() as session:
        
        result = session.run(cypher, {"query": query})
        stakeholders = [record["PrimaryStakeholder"] for record in result]
        return stakeholders
