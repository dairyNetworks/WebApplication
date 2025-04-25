from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw(identifier: str):
    query = """
        MATCH (i:CARBON_FW_IDENTIFIER {name: $identifier})
        MATCH (a:CARBON_FW_ACTION)-[:CARBON_FW_LINKED_TO]->(i)
        MATCH (r:CARBON_FW_RECOMMENDATION)-[:CARBON_FW_RECOMMENDS]->(a)
        MATCH (a)-[:CARBON_FW_INVOLVES]->(fs:CARBON_FW_Formal_Stakeholder)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action,
            fs.name AS Stakeholder
        ORDER BY Recommendation, Action, Stakeholder
        """
    
    with driver.session() as session:
        results = session.run(query, identifier=identifier)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Action Stakeholder" : record["Stakeholder"]
            })
        return table

def get_water_fw(identifier: str):
    query = """
        MATCH (i:WATER_FW_IDENTIFIER {name: $identifier})
        MATCH (a:WATER_FW_ACTION)-[:WATER_FW_LINKED_TO]->(i)
        MATCH (r:WATER_FW_RECOMMENDATION)-[:WATER_FW_RECOMMENDS]->(a)
        MATCH (a)-[:WATER_FW_INVOLVES]->(fs:WATER_FW_Formal_Stakeholder)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action,
            fs.name AS Stakeholder
        ORDER BY Recommendation, Action, Stakeholder
    """
    with driver.session() as session:
        results = session.run(query, identifier=identifier)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Action Stakeholder" : record["Stakeholder"]
            })
        return table
    
def get_livelihood_fw(identifier: str):
    query = """
        MATCH (i:LIVE_FW_IDENTIFIER {name: $identifier})
        MATCH (a:LIVE_FW_ACTION)-[:LIVE_FW_LINKED_TO]->(i)
        MATCH (r:LIVE_FW_RECOMMENDATION)-[:LIVE_FW_RECOMMENDS]->(a)
        MATCH (a)-[:LIVE_FW_INVOLVES]->(fs:LIVE_FW_Formal_Stakeholder)
        RETURN DISTINCT
            i.name AS Identifier,
            r.name AS Recommendation,
            a.name AS Action,
            fs.name AS Stakeholder
        ORDER BY Recommendation, Action, Stakeholder
        """
    with driver.session() as session:
        results = session.run(query, identifier=identifier)
        table = []
        for record in results:
            table.append({
                "Identifier" : record["Identifier"],
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Action Stakeholder" : record["Stakeholder"]
            })
        return table
    
def get_fw(query, identifier):
    if query == "car":
        return get_carbon_fw(identifier)
    elif query == "wat":
        return get_water_fw(identifier)
    elif query == "liv":
        return get_livelihood_fw(identifier)
    else:
        return []
