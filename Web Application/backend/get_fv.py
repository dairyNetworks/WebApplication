from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fv_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVNR_LONE_MISSION)-[:CARBON_FVNR_LONE_MISSIONGOAL_LINK]->(g:CARBON_FVNR_LONE_GOAL)-[:CARBON_FVNR_LONE_GOALACTION_LINK]->(a:CARBON_FVNR_LONE_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:CARBON_FVNR_LONE_MISSION_LINK]->(ms:CARBON_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_LONE_GOAL_LINK]->(gs:CARBON_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_LONE_ACTION_LINK]->(as:CARBON_FVNR_LONE_ACTION_STATEMENT)
        MATCH (a)-[:CARBON_FVNR_LONE_ACTION_STAKE_LINK]->(stakeholder:CARBON_FVNR_LONE_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'

        OPTIONAL MATCH (stakeholder)-[:CARBON_FVNR_LONE_HAS_CATEGORY]->(category:CARBON_FVNR_LONE_Category)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`,
            COLLECT(DISTINCT category.name)[0] AS `CATEGORY`

        RETURN 
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`, 
            `STAKEHOLDER`,
            `CATEGORY`
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
                "Stakeholder" : record["STAKEHOLDER"],
                "Category" : record["CATEGORY"]
            })
        return table

def get_water_fv_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVNR_LONE_MISSION)-[:WATER_FVNR_LONE_MISSIONGOAL_LINK]->(g:WATER_FVNR_LONE_GOAL)-[:WATER_FVNR_LONE_GOALACTION_LINK]->(a:WATER_FVNR_LONE_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:WATER_FVNR_LONE_MISSION_LINK]->(ms:WATER_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:WATER_FVNR_LONE_GOAL_LINK]->(gs:WATER_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVNR_LONE_ACTION_LINK]->(as:WATER_FVNR_LONE_ACTION_STATEMENT)
        MATCH (a)-[:WATER_FVNR_LONE_ACTION_STAKE_LINK]->(stakeholder:WATER_FVNR_LONE_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'

        OPTIONAL MATCH (stakeholder)-[:WATER_FVNR_LONE_HAS_CATEGORY]->(category:WATER_FVNR_LONE_Category)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`,
            COLLECT(DISTINCT category.name)[0] AS `CATEGORY`

        RETURN 
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`, 
            `STAKEHOLDER`,
            `CATEGORY`
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
                "Stakeholder" : record["STAKEHOLDER"],
                "Category" : record["CATEGORY"]
            })
        return table
    
def get_livelihood_fv_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVNR_LONE_MISSION)-[:LIVE_FVNR_LONE_MISSIONGOAL_LINK]->(g:LIVE_FVNR_LONE_GOAL)-[:LIVE_FVNR_LONE_GOALACTION_LINK]->(a:LIVE_FVNR_LONE_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:LIVE_FVNR_LONE_MISSION_LINK]->(ms:LIVE_FVNR_LONE_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:LIVE_FVNR_LONE_GOAL_LINK]->(gs:LIVE_FVNR_LONE_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVNR_LONE_ACTION_LINK]->(as:LIVE_FVNR_LONE_ACTION_STATEMENT)
        MATCH (a)-[:LIVE_FVNR_LONE_ACTION_STAKE_LINK]->(stakeholder:LIVE_FVNR_LONE_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'

        OPTIONAL MATCH (stakeholder)-[:LIVE_FVNR_LONE_HAS_CATEGORY]->(category:LIVE_FVNR_LONE_Category)

        WITH 
            m.name AS MISSION,
            COLLECT(DISTINCT ms.text)[0] AS `MISSION STATEMENT`,
            g.name AS GOAL,
            COLLECT(DISTINCT gs.text)[0] AS `GOAL STATEMENT`,
            a.name AS ACTION,
            COLLECT(DISTINCT as.text)[0] AS `ACTION STATEMENT`,
            stakeholder.name AS `STAKEHOLDER`,
            COLLECT(DISTINCT category.name)[0] AS `CATEGORY`

        RETURN 
            MISSION, 
            `MISSION STATEMENT`, 
            GOAL, 
            `GOAL STATEMENT`, 
            ACTION, 
            `ACTION STATEMENT`, 
            `STAKEHOLDER`,
            `CATEGORY`
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
                "Stakeholder" : record["STAKEHOLDER"],
                "Category" : record["CATEGORY"]
            })
        return table

def get_carbon2_fv_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVNR_LTWO_MISSION)-[:CARBON_FVNR_LTWO_MISSIONGOAL_LINK]->(g:CARBON_FVNR_LTWO_GOAL)
              -[:CARBON_FVNR_LTWO_GOALACTION_LINK]->(a:CARBON_FVNR_LTWO_ACTION {name: $action})
        OPTIONAL MATCH (m)-[:CARBON_FVNR_LTWO_MISSION_LINK]->(ms:CARBON_FVNR_LTWO_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVNR_LTWO_GOAL_LINK]->(gs:CARBON_FVNR_LTWO_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_LTWO_ACTION_LINK]->(as:CARBON_FVNR_LTWO_ACTION_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVNR_LTWO_ACTION_LABELS_LINK]->(label:CARBON_FVNR_LTWO_LABELS)

        RETURN DISTINCT 
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            label.name AS LABEL
        ORDER BY MISSION, GOAL, ACTION, LABEL
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
                "Stakeholder": record["LABEL"] or ""  # Handle null labels
            })
        return table

def get_water2_fv_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVNR_LTWO_MISSION)-[:WATER_FVNR_LTWO_MISSIONGOAL_LINK]->(g:WATER_FVNR_LTWO_GOAL)-[:WATER_FVNR_LTWO_GOALACTION_LINK]->(a:WATER_FVNR_LTWO_ACTION {name: $action})
        MATCH (m)-[:WATER_FVNR_LTWO_MISSION_LINK]->(ms:WATER_FVNR_LTWO_MISSION_STATEMENT)
        MATCH (g)-[:WATER_FVNR_LTWO_GOAL_LINK]->(gs:WATER_FVNR_LTWO_GOAL_STATEMENT)
        MATCH (a)-[:WATER_FVNR_LTWO_ACTION_LINK]->(as:WATER_FVNR_LTWO_ACTION_STATEMENT)
        MATCH (a)-[:WATER_FVNR_LTWO_ACTION_LABELS_LINK]->(label:WATER_FVNR_LTWO_LABELS)

        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            label.name AS LABEL
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
                "Stakeholder": record["LABEL"]
            })
        return table

def get_livelihood2_fv_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVNR_LTWO_MISSION)-[:LIVE_FVNR_LTWO_MISSIONGOAL_LINK]->(g:LIVE_FVNR_LTWO_GOAL)-[:LIVE_FVNR_LTWO_GOALACTION_LINK]->(a:LIVE_FVNR_LTWO_ACTION {name: $action})
        MATCH (m)-[:LIVE_FVNR_LTWO_MISSION_LINK]->(ms:LIVE_FVNR_LTWO_MISSION_STATEMENT)
        MATCH (g)-[:LIVE_FVNR_LTWO_GOAL_LINK]->(gs:LIVE_FVNR_LTWO_GOAL_STATEMENT)
        MATCH (a)-[:LIVE_FVNR_LTWO_ACTION_LINK]->(as:LIVE_FVNR_LTWO_ACTION_STATEMENT)
        MATCH (a)-[:LIVE_FVNR_LTWO_ACTION_LABELS_LINK]->(label:LIVE_FVNR_LTWO_LABELS)

        RETURN DISTINCT
            m.name AS MISSION,
            ms.text AS `MISSION STATEMENT`,
            g.name AS GOAL,
            gs.text AS `GOAL STATEMENT`,
            a.name AS ACTION,
            as.text AS `ACTION STATEMENT`,
            label.name AS LABEL
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
                "Stakeholder": record["LABEL"]
            })
        return table

def get_fv(query, action, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fv_stakeholder(action)
    elif query == "wat" and access == 'levelone':
        return get_water_fv_stakeholder(action)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fv_stakeholder(action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fv_stakeholder(action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fv_stakeholder(action)
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fv_stakeholder(action)
    else:
        return []
