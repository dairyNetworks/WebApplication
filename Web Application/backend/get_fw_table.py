from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw():
    query = """
        MATCH (i:CARBON_FW_IDENTIFIER)
        MATCH (a:CARBON_FW_ACTION)-[:CARBON_FW_LINKED_TO]->(i)
        MATCH (r:CARBON_FW_RECOMMENDATION)-[:CARBON_FW_RECOMMENDS]->(a)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action
        ORDER BY Identifier, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water_fw():
    query = """
        MATCH (i:WATER_FW_IDENTIFIER)
        MATCH (a:WATER_FW_ACTION)-[:WATER_FW_LINKED_TO]->(i)
        MATCH (r:WATER_FW_RECOMMENDATION)-[:WATER_FW_RECOMMENDS]->(a)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action
        ORDER BY Identifier, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood_fw():
    query = """
        MATCH (i:LIVE_FW_IDENTIFIER)
        MATCH (a:LIVE_FW_ACTION)-[:LIVE_FW_LINKED_TO]->(i)
        MATCH (r:LIVE_FW_RECOMMENDATION)-[:LIVE_FW_RECOMMENDS]->(a)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action
        ORDER BY Identifier, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_fw_table(query):
    if query == "car":
        return get_carbon_fw()
    elif query == "wat":
        return get_water_fw()
    elif query == "liv":
        return get_livelihood_fw()
    else:
        return []
