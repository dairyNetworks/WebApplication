from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_primary_stakeholders(query: str, access:str):
    if access == 'levelone':
         cypher = """
            MATCH (doc:PUBLICATION_LONE_Document {name: $query})
            MATCH (doc)-[:PUBLICATION_LONE_HAS_AUTHOR]->(:PUBLICATION_LONE_Author)
                -[:PUBLICATION_LONE_HAS_YEAR]->(:PUBLICATION_LONE_Year)
                -[:PUBLICATION_LONE_HAS_PRIMARY_STAKEHOLDER]->(primary:PUBLICATION_LONE_PrimaryFormalName)
            RETURN DISTINCT primary.name AS PrimaryFormalName
            ORDER BY PrimaryFormalName
        """
    elif access == 'leveltwo':
        cypher = """
            MATCH (doc:PUBLICATION_LTWO_Document {name: $query})
            MATCH (doc)-[:PUBLICATION_LTWO_HAS_AUTHOR]->(:PUBLICATION_LTWO_Author)
                -[:PUBLICATION_LTWO_HAS_YEAR]->(:PUBLICATION_LTWO_Year)
                -[:PUBLICATION_LTWO_HAS_PRIMARY_LABEL]->(primary:PUBLICATION_LTWO_PrimaryLabel)
            RETURN DISTINCT primary.name AS PrimaryFormalName
            ORDER BY PrimaryFormalName
        """
    with driver.session() as session:
        result = session.run(cypher, {"query": query})
        stakeholders = [record["PrimaryFormalName"] for record in result]  # <-- fix here
        return stakeholders
