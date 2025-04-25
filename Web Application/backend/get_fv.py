from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fv_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVNR_MISSION)-[:CARBON_FVNR_MISSIONGOAL_LINK]->(g:CARBON_FVNR_GOAL)-[:CARBON_FVNR_GOALACTION_LINK]->(a:CARBON_FVNR_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:CARBON_FVNR_MISSION_LINK]->(ms:CARBON_FVNR_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_GOAL_LINK]->(gs:CARBON_FVNR_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_ACTION_LINK]->(as:CARBON_FVNR_ACTION_STATEMENT)
        MATCH (a)-[:CARBON_FVNR_ACTION_STAKE_LINK]->(stakeholder:CARBON_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`

        RETURN MISSION, `MISSION STATEMENT`, GOAL, `GOAL STATEMENT`, ACTION, `ACTION STATEMENT`, `STAKEHOLDER`
        ORDER BY MISSION, GOAL, ACTION
    """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"],
                "Stakeholder" : record["STAKEHOLDER"]
            })
        return table

def get_water_fv_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVNR_MISSION)-[:WATER_FVNR_MISSIONGOAL_LINK]->(g:WATER_FVNR_GOAL)-[:WATER_FVNR_GOALACTION_LINK]->(a:WATER_FVNR_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:WATER_FVNR_MISSION_LINK]->(ms:WATER_FVNR_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:WATER_FVNR_GOAL_LINK]->(gs:WATER_FVNR_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVNR_ACTION_LINK]->(as:WATER_FVNR_ACTION_STATEMENT)
        MATCH (a)-[stakeLink:WATER_FVNR_ACTION_STAKE_LINK]->(stakeholder:WATER_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'
        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`
        ORDER BY MISSION, GOAL, ACTION
    """
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"],
                "Stakeholder" : record["STAKEHOLDER"]
            })
        return table
    
def get_livelihood_fv_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVNR_MISSION)-[:LIVE_FVNR_MISSIONGOAL_LINK]->(g:LIVE_FVNR_GOAL)-[:LIVE_FVNR_GOALACTION_LINK]->(a:LIVE_FVNR_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:LIVE_FVNR_MISSION_LINK]->(ms:LIVE_FVNR_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:LIVE_FVNR_GOAL_LINK]->(gs:LIVE_FVNR_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVNR_ACTION_LINK]->(as:LIVE_FVNR_ACTION_STATEMENT)
        MATCH (a)-[stakeLink:LIVE_FVNR_ACTION_STAKE_LINK]->(stakeholder:LIVE_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'
        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`
        ORDER BY MISSION, GOAL, ACTION
    """
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal" : record["GOAL"],
                "Goal Statement" : record["GOAL STATEMENT"],
                "Action" : record["ACTION"],
                "Action Statement" : record["ACTION STATEMENT"],
                "Stakeholder" : record["STAKEHOLDER"]
            })
        return table
    
def get_fv(query, action):
    if query == "car":
        return get_carbon_fv_stakeholder(action)
    elif query == "wat":
        return get_water_fv_stakeholder(action)
    elif query == "liv":
        return get_livelihood_fv_stakeholder(action)
    else:
        return []
