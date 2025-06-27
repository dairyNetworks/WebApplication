from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fv():
    query = """
        MATCH (m:CARBON_FVNR_LONE_MISSION)
        MATCH (m)-[:CARBON_FVNR_LONE_MISSIONGOAL_LINK]->(g:CARBON_FVNR_LONE_GOAL)
        MATCH (g)-[:CARBON_FVNR_LONE_GOALACTION_LINK]->(a:CARBON_FVNR_LONE_ACTION)

        OPTIONAL MATCH (m)-[:CARBON_FVNR_LONE_MISSION_LINK]->(ms:CARBON_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_LONE_GOAL_LINK]->(gs:CARBON_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_LONE_ACTION_LINK]->(as:CARBON_FVNR_LONE_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN DISTINCT 
            MISSION,
            `MISSION STATEMENT`,
            GOAL,
            `GOAL STATEMENT`,
            ACTION,
            `ACTION STATEMENT`
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

def get_water_fv():
    query = """
        MATCH (m:WATER_FVNR_LONE_MISSION)
        MATCH (m)-[:WATER_FVNR_LONE_MISSIONGOAL_LINK]->(g:WATER_FVNR_LONE_GOAL)
        MATCH (g)-[:WATER_FVNR_LONE_GOALACTION_LINK]->(a:WATER_FVNR_LONE_ACTION)

        OPTIONAL MATCH (m)-[:WATER_FVNR_LONE_MISSION_LINK]->(ms:WATER_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:WATER_FVNR_LONE_GOAL_LINK]->(gs:WATER_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVNR_LONE_ACTION_LINK]->(as:WATER_FVNR_LONE_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN DISTINCT 
            MISSION,
            `MISSION STATEMENT`,
            GOAL,
            `GOAL STATEMENT`,
            ACTION,
            `ACTION STATEMENT`
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
    
def get_livelihood_fv():
    query = """
        MATCH (m:LIVE_FVNR_LONE_MISSION)
        MATCH (m)-[:LIVE_FVNR_LONE_MISSIONGOAL_LINK]->(g:LIVE_FVNR_LONE_GOAL)
        MATCH (g)-[:LIVE_FVNR_LONE_GOALACTION_LINK]->(a:LIVE_FVNR_LONE_ACTION)

        OPTIONAL MATCH (m)-[:LIVE_FVNR_LONE_MISSION_LINK]->(ms:LIVE_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:LIVE_FVNR_LONE_GOAL_LINK]->(gs:LIVE_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVNR_LONE_ACTION_LINK]->(as:LIVE_FVNR_LONE_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN DISTINCT 
            MISSION,
            `MISSION STATEMENT`,
            GOAL,
            `GOAL STATEMENT`,
            ACTION,
            `ACTION STATEMENT`
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
    
def get_carbon2_fv():
    query = """
        MATCH (m:CARBON_FVNR_LTWO_MISSION)
        MATCH (m)-[:CARBON_FVNR_LTWO_MISSIONGOAL_LINK]->(g:CARBON_FVNR_LTWO_GOAL)
        MATCH (g)-[:CARBON_FVNR_LTWO_GOALACTION_LINK]->(a:CARBON_FVNR_LTWO_ACTION)

        OPTIONAL MATCH (m)-[:CARBON_FVNR_LTWO_MISSION_LINK]->(ms:CARBON_FVNR_LTWO_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_LTWO_GOAL_LINK]->(gs:CARBON_FVNR_LTWO_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_LTWO_ACTION_LINK]->(as:CARBON_FVNR_LTWO_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            collect(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            collect(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            collect(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN DISTINCT
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`
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

def get_water2_fv():
    query = """
        MATCH (m:WATER_FVNR_LTWO_MISSION)
        OPTIONAL MATCH (m)-[:WATER_FVNR_LTWO_MISSION_LINK]->(ms:WATER_FVNR_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVNR_LTWO_MISSIONGOAL_LINK]->(g:WATER_FVNR_LTWO_GOAL)
        OPTIONAL MATCH (g)-[:WATER_FVNR_LTWO_GOAL_LINK]->(gs:WATER_FVNR_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVNR_LTWO_GOALACTION_LINK]->(a:WATER_FVNR_LTWO_ACTION)
        OPTIONAL MATCH (a)-[:WATER_FVNR_LTWO_ACTION_LINK]->(as:WATER_FVNR_LTWO_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN 
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`
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
    
def get_livelihood2_fv():
    query = """
        MATCH (m:LIVE_FVNR_LTWO_MISSION)
        OPTIONAL MATCH (m)-[:LIVE_FVNR_LTWO_MISSION_LINK]->(ms:LIVE_FVNR_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVNR_LTWO_MISSIONGOAL_LINK]->(g:LIVE_FVNR_LTWO_GOAL)
        OPTIONAL MATCH (g)-[:LIVE_FVNR_LTWO_GOAL_LINK]->(gs:LIVE_FVNR_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVNR_LTWO_GOALACTION_LINK]->(a:LIVE_FVNR_LTWO_ACTION)
        OPTIONAL MATCH (a)-[:LIVE_FVNR_LTWO_ACTION_LINK]->(as:LIVE_FVNR_LTWO_ACTION_STATEMENT)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`

        RETURN 
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`
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

def get_fv_table(query, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fv()
    elif query == "wat" and access == 'levelone':
        return get_water_fv()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fv()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fv()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fv()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fv()
    else:
        return []
