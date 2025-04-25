from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fv():
    query = """
        MATCH (m:CARBON_FVNR_MISSION)
        OPTIONAL MATCH (m)-[:CARBON_FVNR_MISSION_LINK]->(ms:CARBON_FVNR_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVNR_MISSIONGOAL_LINK]->(g:CARBON_FVNR_GOAL)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_GOAL_LINK]->(gs:CARBON_FVNR_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVNR_GOALACTION_LINK]->(a:CARBON_FVNR_ACTION)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_ACTION_LINK]->(as:CARBON_FVNR_ACTION_STATEMENT)
        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`
        ORDER BY MISSION, GOAL, ACTION
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"]
            })
        return table

def get_water_fv():
    query = """
        MATCH (m:WATER_FVNR_MISSION)
        OPTIONAL MATCH (m)-[:WATER_FVNR_MISSION_LINK]->(ms:WATER_FVNR_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVNR_MISSIONGOAL_LINK]->(g:WATER_FVNR_GOAL)
        OPTIONAL MATCH (g)-[:WATER_FVNR_GOAL_LINK]->(gs:WATER_FVNR_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVNR_GOALACTION_LINK]->(a:WATER_FVNR_ACTION)
        OPTIONAL MATCH (a)-[:WATER_FVNR_ACTION_LINK]->(as:WATER_FVNR_ACTION_STATEMENT)
        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`
        ORDER BY MISSION, GOAL, ACTION
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"]
            })
        return table
    
def get_livelihood_fv():
    query = """
        MATCH (m:LIVE_FVNR_MISSION)
        OPTIONAL MATCH (m)-[:LIVE_FVNR_MISSION_LINK]->(ms:LIVE_FVNR_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVNR_MISSIONGOAL_LINK]->(g:LIVE_FVNR_GOAL)
        OPTIONAL MATCH (g)-[:LIVE_FVNR_GOAL_LINK]->(gs:LIVE_FVNR_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVNR_GOALACTION_LINK]->(a:LIVE_FVNR_ACTION)
        OPTIONAL MATCH (a)-[:LIVE_FVNR_ACTION_LINK]->(as:LIVE_FVNR_ACTION_STATEMENT)
        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`
        ORDER BY MISSION, GOAL, ACTION
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"]
            })
        return table

def get_fv_table(query):
    if query == "car":
        return get_carbon_fv()
    elif query == "wat":
        return get_water_fv()
    elif query == "liv":
        return get_livelihood_fv()
    else:
        return []
