from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVRA_LONE_MISSION)
        MATCH (m)-[:CARBON_FVRA_LONE_MISSION_LINK]->(ms:CARBON_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVRA_LONE_MISSIONGOAL_LINK]->(g:CARBON_FVRA_LONE_GOAL)
        MATCH (g)-[:CARBON_FVRA_LONE_GOAL_LINK]->(gs:CARBON_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVRA_LONE_GOALACTION_LINK]->(a:CARBON_FVRA_LONE_ACTION {name: $action})
        MATCH (a)-[:CARBON_FVRA_LONE_ACTION_LINK]->(as:CARBON_FVRA_LONE_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVRA_LONE_ACTION_STAKE_LINK]->(s:CARBON_FVRA_LONE_Formal_Stakeholder)
        OPTIONAL MATCH (s)-[:CARBON_FVRA_LONE_HAS_CATEGORY]->(c:CARBON_FVRA_LONE_Category)

        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            s.name AS `FORMAL STAKEHOLDER`,
            c.name AS CATEGORY
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
                "Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table

def get_water_fvr_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVRA_LONE_MISSION)
        MATCH (m)-[:WATER_FVRA_LONE_MISSION_LINK]->(ms:WATER_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_LONE_MISSIONGOAL_LINK]->(g:WATER_FVRA_LONE_GOAL)
        MATCH (g)-[:WATER_FVRA_LONE_GOAL_LINK]->(gs:WATER_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_LONE_GOALACTION_LINK]->(a:WATER_FVRA_LONE_ACTION {name: $action})
        MATCH (a)-[:WATER_FVRA_LONE_ACTION_LINK]->(as:WATER_FVRA_LONE_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVRA_LONE_ACTION_STAKE_LINK]->(s:WATER_FVRA_LONE_Formal_Stakeholder)
        OPTIONAL MATCH (s)-[:WATER_FVRA_LONE_HAS_CATEGORY]->(c:WATER_FVRA_LONE_Category)

        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            s.name AS `FORMAL STAKEHOLDER`,
            c.name AS CATEGORY
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
                "Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table
    
def get_livelihood_fvr_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVRA_LONE_MISSION)
        MATCH (m)-[:LIVE_FVRA_LONE_MISSION_LINK]->(ms:LIVE_FVRA_LONE_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVRA_LONE_MISSIONGOAL_LINK]->(g:LIVE_FVRA_LONE_GOAL)
        MATCH (g)-[:LIVE_FVRA_LONE_GOAL_LINK]->(gs:LIVE_FVRA_LONE_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVRA_LONE_GOALACTION_LINK]->(a:LIVE_FVRA_LONE_ACTION {name: $action})
        MATCH (a)-[:LIVE_FVRA_LONE_ACTION_LINK]->(as:LIVE_FVRA_LONE_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVRA_LONE_ACTION_STAKE_LINK]->(s:LIVE_FVRA_LONE_Formal_Stakeholder)
        OPTIONAL MATCH (s)-[:LIVE_FVRA_LONE_HAS_CATEGORY]->(c:LIVE_FVRA_LONE_Category)

        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            s.name AS `FORMAL STAKEHOLDER`,
            c.name AS CATEGORY
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
                "Stakeholder" : record["FORMAL STAKEHOLDER"]
            })
        return table

def get_carbon2_fvr_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVRA_LTWO_MISSION)-[:CARBON_FVRA_LTWO_MISSION_LINK]->(ms:CARBON_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVRA_LTWO_MISSIONGOAL_LINK]->(g:CARBON_FVRA_LTWO_GOAL)
        MATCH (g)-[:CARBON_FVRA_LTWO_GOAL_LINK]->(gs:CARBON_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVRA_LTWO_GOALACTION_LINK]->(a:CARBON_FVRA_LTWO_ACTION {name: $action})
        MATCH (a)-[:CARBON_FVRA_LTWO_ACTION_LINK]->(as:CARBON_FVRA_LTWO_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVRA_LTWO_ACTION_LABEL_LINK]->(l:CARBON_FVRA_LTWO_LABEL)
        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            l.name AS LABEL
        ORDER BY MISSION, GOAL, ACTION
    """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"],
                "Stakeholder": record["LABEL"]  # This could be None if no label is linked
            })
        return table

def get_water2_fvr_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVRA_LTWO_MISSION)-[:WATER_FVRA_LTWO_MISSION_LINK]->(ms:WATER_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_LTWO_MISSIONGOAL_LINK]->(g:WATER_FVRA_LTWO_GOAL)
        MATCH (g)-[:WATER_FVRA_LTWO_GOAL_LINK]->(gs:WATER_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_LTWO_GOALACTION_LINK]->(a:WATER_FVRA_LTWO_ACTION {name: $action})
        MATCH (a)-[:WATER_FVRA_LTWO_ACTION_LINK]->(as:WATER_FVRA_LTWO_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVRA_LTWO_ACTION_LABEL_LINK]->(l:WATER_FVRA_LTWO_LABEL)
        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            l.name AS LABEL
        ORDER BY MISSION, GOAL, ACTION
    """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"],
                "Stakeholder": record["LABEL"]  # This could be None if no label is linked
            })
        return table
    

def get_live2_fvr_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVRA_LTWO_MISSION)-[:LIVE_FVRA_LTWO_MISSION_LINK]->(ms:LIVE_FVRA_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVRA_LTWO_MISSIONGOAL_LINK]->(g:LIVE_FVRA_LTWO_GOAL)
        MATCH (g)-[:LIVE_FVRA_LTWO_GOAL_LINK]->(gs:LIVE_FVRA_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVRA_LTWO_GOALACTION_LINK]->(a:LIVE_FVRA_LTWO_ACTION {name: $action})
        MATCH (a)-[:LIVE_FVRA_LTWO_ACTION_LINK]->(as:LIVE_FVRA_LTWO_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVRA_LTWO_ACTION_LABEL_LINK]->(l:LIVE_FVRA_LTWO_LABEL)
        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            l.name AS LABEL
        ORDER BY MISSION, GOAL, ACTION
    """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["MISSION"],
                "Mission Statement": record["MISSION STATEMENT"],
                "Goal": record["GOAL"],
                "Goal Statement": record["GOAL STATEMENT"],
                "Action": record["ACTION"],
                "Action Statement": record["ACTION STATEMENT"],
                "Stakeholder": record["LABEL"]  # This could be None if no label is linked
            })
        return table
    
def get_fvr(query, action,access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvr_stakeholder(action)
    elif query == "wat" and access == 'levelone':
        return get_water_fvr_stakeholder(action)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fvr_stakeholder(action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvr_stakeholder(action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvr_stakeholder(action)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fvr_stakeholder(action)
    else:
        return []
