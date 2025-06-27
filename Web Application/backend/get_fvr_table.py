from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr():
    query = """
        MATCH (m:CARBON_FVRA_LONE_MISSION)-[:CARBON_FVRA_LONE_MISSION_LINK]->(ms:CARBON_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVRA_LONE_MISSIONGOAL_LINK]->(g:CARBON_FVRA_LONE_GOAL)-[:CARBON_FVRA_LONE_GOAL_LINK]->(gs:CARBON_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVRA_LONE_GOALACTION_LINK]->(a:CARBON_FVRA_LONE_ACTION)-[:CARBON_FVRA_LONE_ACTION_LINK]->(as:CARBON_FVRA_LONE_ACTION_STATEMENT)
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

def get_water_fvr():
    query = """
        MATCH (m:WATER_FVRA_LONE_MISSION)-[:WATER_FVRA_LONE_MISSION_LINK]->(ms:WATER_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_LONE_MISSIONGOAL_LINK]->(g:WATER_FVRA_LONE_GOAL)-[:WATER_FVRA_LONE_GOAL_LINK]->(gs:WATER_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_LONE_GOALACTION_LINK]->(a:WATER_FVRA_LONE_ACTION)-[:WATER_FVRA_LONE_ACTION_LINK]->(as:WATER_FVRA_LONE_ACTION_STATEMENT)
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
    
def get_livelihood_fvr():
    query = """
        MATCH (m:LIVE_FVRA_LONE_MISSION)-[:LIVE_FVRA_LONE_MISSION_LINK]->(ms:LIVE_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVRA_LONE_MISSIONGOAL_LINK]->(g:LIVE_FVRA_LONE_GOAL)-[:LIVE_FVRA_LONE_GOAL_LINK]->(gs:LIVE_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVRA_LONE_GOALACTION_LINK]->(a:LIVE_FVRA_LONE_ACTION)-[:LIVE_FVRA_LONE_ACTION_LINK]->(as:LIVE_FVRA_LONE_ACTION_STATEMENT)
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

def get_carbon2_fvr():
    query = """
        MATCH (m:CARBON_FVRA_LTWO_MISSION)-[:CARBON_FVRA_LTWO_MISSION_LINK]->(ms:CARBON_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVRA_LTWO_MISSIONGOAL_LINK]->(g:CARBON_FVRA_LTWO_GOAL)-[:CARBON_FVRA_LTWO_GOAL_LINK]->(gs:CARBON_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVRA_LTWO_GOALACTION_LINK]->(a:CARBON_FVRA_LTWO_ACTION)-[:CARBON_FVRA_LTWO_ACTION_LINK]->(as:CARBON_FVRA_LTWO_ACTION_STATEMENT)

        RETURN 
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
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"]
            })
        return table

def get_water2_fvr():
    query = """
        MATCH (m:WATER_FVRA_LTWO_MISSION)-[:WATER_FVRA_LTWO_MISSION_LINK]->(ms:WATER_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_LTWO_MISSIONGOAL_LINK]->(g:WATER_FVRA_LTWO_GOAL)-[:WATER_FVRA_LTWO_GOAL_LINK]->(gs:WATER_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_LTWO_GOALACTION_LINK]->(a:WATER_FVRA_LTWO_ACTION)-[:WATER_FVRA_LTWO_ACTION_LINK]->(as:WATER_FVRA_LTWO_ACTION_STATEMENT)

        RETURN 
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
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"]
            })
        return table
    
def get_livelihood2_fvr():
    query = """
        MATCH (m:LIVE_FVRA_LTWO_MISSION)-[:LIVE_FVRA_LTWO_MISSION_LINK]->(ms:LIVE_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVRA_LTWO_MISSIONGOAL_LINK]->(g:LIVE_FVRA_LTWO_GOAL)-[:LIVE_FVRA_LTWO_GOAL_LINK]->(gs:LIVE_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVRA_LTWO_GOALACTION_LINK]->(a:LIVE_FVRA_LTWO_ACTION)-[:LIVE_FVRA_LTWO_ACTION_LINK]->(as:LIVE_FVRA_LTWO_ACTION_STATEMENT)

        RETURN 
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
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"]
            })
        return table

def get_fvr_table(query,access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvr()
    elif query == "wat" and access == 'levelone':
        return get_water_fvr()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fvr()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvr()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvr()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fvr()
    else:
        return []
