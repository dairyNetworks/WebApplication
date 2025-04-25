from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_stakeholder(action: str):
    query = """
            MATCH (m:CARBON_FVRA_MISSION)-[:CARBON_FVRA_MISSION_LINK]->(ms:CARBON_FVRA_MISSION_STATEMENT)
            MATCH (m)-[:CARBON_FVRA_MISSIONGOAL_LINK]->(g:CARBON_FVRA_GOAL)-[:CARBON_FVRA_GOAL_LINK]->(gs:CARBON_FVRA_GOAL_STATEMENT)
            MATCH (g)-[:CARBON_FVRA_GOALACTION_LINK]->(a:CARBON_FVRA_ACTION)-[:CARBON_FVRA_ACTION_LINK]->(as:CARBON_FVRA_ACTION_STATEMENT)
            MATCH (a)-[:CARBON_FVRA_ACTION_STAKE_LINK]->(s:CARBON_FVRA_Formal_Stakeholder)
            WHERE a.name = $action AND s.name IS NOT NULL
            RETURN DISTINCT
                m.name AS MISSION,
                ms.text AS `MISSION STATEMENT`,
                g.name AS GOAL,
                gs.text AS `GOAL STATEMENT`,
                a.name AS ACTION,
                as.text AS `ACTION STATEMENT`,
                s.name AS `FORMAL STAKEHOLDER`
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
                "Action Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table

def get_water_fvr_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVRA_MISSION)-[:WATER_FVRA_MISSION_LINK]->(ms:WATER_FVRA_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_MISSIONGOAL_LINK]->(g:WATER_FVRA_GOAL)-[:WATER_FVRA_GOAL_LINK]->(gs:WATER_FVRA_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_GOALACTION_LINK]->(a:WATER_FVRA_ACTION)-[:WATER_FVRA_ACTION_LINK]->(as:WATER_FVRA_ACTION_STATEMENT)
        MATCH (a)-[:WATER_FVRA_ACTION_STAKE_LINK]->(s:WATER_FVRA_Formal_Stakeholder)
        WHERE a.name = $action AND s.name IS NOT NULL
        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            s.name AS `FORMAL STAKEHOLDER`
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
                "Action Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table
    
def get_livelihood_fvr_stakeholder(action: str):
    query = """
            MATCH (m:LIVE_FVRA_MISSION)-[:LIVE_FVRA_MISSION_LINK]->(ms:LIVE_FVRA_MISSION_STATEMENT)
            MATCH (m)-[:LIVE_FVRA_MISSIONGOAL_LINK]->(g:LIVE_FVRA_GOAL)-[:LIVE_FVRA_GOAL_LINK]->(gs:LIVE_FVRA_GOAL_STATEMENT)
            MATCH (g)-[:LIVE_FVRA_GOALACTION_LINK]->(a:LIVE_FVRA_ACTION)-[:LIVE_FVRA_ACTION_LINK]->(as:LIVE_FVRA_ACTION_STATEMENT)
            MATCH (a)-[:LIVE_FVRA_ACTION_STAKE_LINK]->(s:LIVE_FVRA_Formal_Stakeholder)
            WHERE a.name = $action AND s.name IS NOT NULL
            RETURN DISTINCT
                m.name AS MISSION,
                ms.text AS `MISSION STATEMENT`,
                g.name AS GOAL,
                gs.text AS `GOAL STATEMENT`,
                a.name AS ACTION,
                as.text AS `ACTION STATEMENT`,
                s.name AS `FORMAL STAKEHOLDER`
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
                "Action Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table
    
def get_fvr(query, action):
    if query == "car":
        return get_carbon_fvr_stakeholder(action)
    elif query == "wat":
        return get_water_fvr_stakeholder(action)
    elif query == "liv":
        return get_livelihood_fvr_stakeholder(action)
    else:
        return []
