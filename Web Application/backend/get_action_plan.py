from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:CARBON_AP_FILE)-[:CARBON_AP_ACTION]->(a:CARBON_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:CARBON_AP_ACTION_STAKEHOLDER]->(s:CARBON_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table

def get_water_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:WATER_AP_FILE)-[:WATER_AP_ACTION]->(a:WATER_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:WATER_AP_ACTION_STAKEHOLDER]->(s:WATER_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table
    
def get_livelihood_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:LIVE_AP_FILE)-[:LIVE_AP_ACTION]->(a:LIVE_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:LIVE_AP_ACTION_STAKEHOLDER]->(s:LIVE_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table
    
def get_action_plan(query, file_name, action):
    if query == "car":
        return get_carbon_action_plan_stakeholder(file_name, action)
    elif query == "wat":
        return get_water_action_plan_stakeholder(file_name, action)
    elif query == "liv":
        return get_livelihood_action_plan_stakeholder(file_name, action)
    else:
        return []
