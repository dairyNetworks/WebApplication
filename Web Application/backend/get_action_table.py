from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_action_plan():
    query = """
        MATCH (f:CARBON_AP_LONE_FILE)-[:CARBON_AP_LONE_HAS_ACTION]->(a:CARBON_AP_LONE_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table

def get_water_action_plan():
    query = """
        MATCH (f:WATER_AP_LONE_FILE)-[:WATER_AP_LONE_HAS_ACTION]->(a:WATER_AP_LONE_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood_action_plan():
    query = """
        MATCH (f:LIVE_AP_LONE_FILE)-[:LIVE_AP_LONE_HAS_ACTION]->(a:LIVE_AP_LONE_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table

def get_carbon2_action_plan():
    query = """
        MATCH (f:CARBON_AP_LTWO_FILE)-[:CARBON_AP_LTWO_HAS_ACTION]->(a:CARBON_AP_LTWO_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table

def get_water2_action_plan():
    query = """
        MATCH (f:WATER_AP_LTWO_FILE)-[:WATER_AP_LTWO_HAS_ACTION]->(a:WATER_AP_LTWO_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood2_action_plan():
    query = """
        MATCH (f:LIVE_AP_LTWO_FILE)-[:LIVE_AP_LTWO_HAS_ACTION]->(a:LIVE_AP_LTWO_ACTION)
        RETURN DISTINCT f.name AS `File Name`, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Action Plan File": record["File Name"],
                "Action": record["Action"]
            })
        return table
    
def get_action_table(query, access):
    if query == "car" and access == 'levelone':
        return get_carbon_action_plan()
    elif query == "wat" and access == 'levelone':
        return get_water_action_plan()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_action_plan()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_action_plan()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_action_plan()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_action_plan()
    else:
        return []
