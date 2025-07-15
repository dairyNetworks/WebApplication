from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:CARBON_AP_LONE_FILE)-[:CARBON_AP_LONE_HAS_ACTION]->(a:CARBON_AP_LONE_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:CARBON_AP_LONE_HAS_STAKEHOLDER]->(s:CARBON_AP_LONE_STAKEHOLDERS)
        OPTIONAL MATCH (s)-[:CARBON_AP_LONE_HAS_CATEGORY]->(c:CARBON_AP_LONE_CATEGORY)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder, 
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"],
                "Category" : record["Category"]
            })
        return table

def get_water_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:WATER_AP_LONE_FILE)-[:WATER_AP_LONE_HAS_ACTION]->(a:WATER_AP_LONE_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:WATER_AP_LONE_HAS_STAKEHOLDER]->(s:WATER_AP_LONE_STAKEHOLDERS)
        OPTIONAL MATCH (s)-[:WATER_AP_LONE_HAS_CATEGORY]->(c:WATER_AP_LONE_CATEGORY)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder, 
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"],
                "Category" : record["Category"]

            })
        return table
    
def get_livelihood_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:LIVE_AP_LONE_FILE)-[:LIVE_AP_LONE_HAS_ACTION]->(a:LIVE_AP_LONE_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:LIVE_AP_LONE_HAS_STAKEHOLDER]->(s:LIVE_AP_LONE_STAKEHOLDERS)
        OPTIONAL MATCH (s)-[:LIVE_AP_LONE_HAS_CATEGORY]->(c:LIVE_AP_LONE_CATEGORY)
        RETURN DISTINCT 
            f.name AS `File Name`, 
            a.name AS Action, 
            s.name AS Stakeholder, 
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Stakeholder"],
                "Category" : record["Category"]
            })
        return table
    
def get_carbon2_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:CARBON_AP_LTWO_FILE {name: $file_name})
            -[:CARBON_AP_LTWO_HAS_ACTION]->(a:CARBON_AP_LTWO_ACTION {name: $action})
            -[:CARBON_AP_LTWO_HAS_LABELS]->(l:CARBON_AP_LTWO_LABELS)
        RETURN DISTINCT 
            f.name AS `File Name`,
            a.name AS Action,
            l.name AS Labels
        ORDER BY `File Name`, Action, Labels
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Labels"]
            })
        return table

def get_water2_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:WATER_AP_LTWO_FILE {name: $file_name})
            -[:WATER_AP_LTWO_HAS_ACTION]->(a:WATER_AP_LTWO_ACTION {name: $action})
            -[:WATER_AP_LTWO_HAS_LABELS]->(l:WATER_AP_LTWO_LABELS)
        RETURN DISTINCT 
            f.name AS `File Name`,
            a.name AS Action,
            l.name AS Labels
        ORDER BY `File Name`, Action, Labels
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Labels"]
            })
        return table
    
   
def get_livelihood2_action_plan_stakeholder(file_name: str, action: str):
    query = """
        MATCH (f:LIVE_AP_LTWO_FILE {name: $file_name})
            -[:LIVE_AP_LTWO_HAS_ACTION]->(a:LIVE_AP_LTWO_ACTION {name: $action})
            -[:LIVE_AP_LTWO_HAS_LABELS]->(l:LIVE_AP_LTWO_LABELS)
        RETURN DISTINCT 
            f.name AS `File Name`,
            a.name AS Action,
            l.name AS Labels
        ORDER BY `File Name`, Action, Labels
    """
    with driver.session() as session:
        results = session.run(query, file_name=file_name, action=action)
        table = []
        for record in results:
            table.append({
                "File Name": record["File Name"],
                "Action": record["Action"],
                "Stakeholder" : record["Labels"]
            })
        return table
    
def get_action_plan(query, file_name, action,access):
    if query == "car" and access == 'levelone':
        return get_carbon_action_plan_stakeholder(file_name, action)
    elif query == "wat" and access == 'levelone':
        return get_water_action_plan_stakeholder(file_name, action)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_action_plan_stakeholder(file_name, action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_action_plan_stakeholder(file_name, action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_action_plan_stakeholder(file_name, action)
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_action_plan_stakeholder(file_name, action)
    else:
        return []