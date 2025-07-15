from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:CARBON_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:CARBON_FVSTAKEHOLDER_HAS_MISSION]->(m:CARBON_FVSTAKEHOLDER_Mission)
            -[:CARBON_FVSTAKEHOLDER_HAS_GOAL]->(g:CARBON_FVSTAKEHOLDER_Goal)
            -[:CARBON_FVSTAKEHOLDER_HAS_ACTION]->(a:CARBON_FVSTAKEHOLDER_Action)
        OPTIONAL MATCH (m)-[:CARBON_FVSTAKEHOLDER_HAS_STATEMENT]->(ms:CARBON_FVSTAKEHOLDER_MissionStatement)
        OPTIONAL MATCH (g)-[:CARBON_FVSTAKEHOLDER_HAS_STATEMENT]->(gs:CARBON_FVSTAKEHOLDER_GoalStatement)
        OPTIONAL MATCH (a)-[:CARBON_FVSTAKEHOLDER_HAS_STATEMENT]->(as:CARBON_FVSTAKEHOLDER_ActionStatement)

        RETURN DISTINCT 
            s.name AS FormalStakeholder,
            m.name AS Mission,
            ms.name AS MissionStatement,
            g.name AS Goal,
            gs.name AS GoalStatement,
            a.name AS Action,
            as.name AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table

def get_water_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:WATER_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:WATER_FVSTAKEHOLDER_HAS_MISSION]->(m:WATER_FVSTAKEHOLDER_Mission)
            -[:WATER_FVSTAKEHOLDER_HAS_GOAL]->(g:WATER_FVSTAKEHOLDER_Goal)
            -[:WATER_FVSTAKEHOLDER_HAS_ACTION]->(a:WATER_FVSTAKEHOLDER_Action)
        OPTIONAL MATCH (m)-[:WATER_FVSTAKEHOLDER_HAS_STATEMENT]->(ms:WATER_FVSTAKEHOLDER_MissionStatement)
        OPTIONAL MATCH (g)-[:WATER_FVSTAKEHOLDER_HAS_STATEMENT]->(gs:WATER_FVSTAKEHOLDER_GoalStatement)
        OPTIONAL MATCH (a)-[:WATER_FVSTAKEHOLDER_HAS_STATEMENT]->(as:WATER_FVSTAKEHOLDER_ActionStatement)

        RETURN DISTINCT 
            s.name AS FormalStakeholder,
            m.name AS Mission,
            ms.name AS MissionStatement,
            g.name AS Goal,
            gs.name AS GoalStatement,
            a.name AS Action,
            as.name AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table
    
def get_livelihood_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:LIVE_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:LIVE_FVSTAKEHOLDER_HAS_MISSION]->(m:LIVE_FVSTAKEHOLDER_Mission)
            -[:LIVE_FVSTAKEHOLDER_HAS_GOAL]->(g:LIVE_FVSTAKEHOLDER_Goal)
            -[:LIVE_FVSTAKEHOLDER_HAS_ACTION]->(a:LIVE_FVSTAKEHOLDER_Action)
        OPTIONAL MATCH (m)-[:LIVE_FVSTAKEHOLDER_HAS_STATEMENT]->(ms:LIVE_FVSTAKEHOLDER_MissionStatement)
        OPTIONAL MATCH (g)-[:LIVE_FVSTAKEHOLDER_HAS_STATEMENT]->(gs:LIVE_FVSTAKEHOLDER_GoalStatement)
        OPTIONAL MATCH (a)-[:LIVE_FVSTAKEHOLDER_HAS_STATEMENT]->(as:LIVE_FVSTAKEHOLDER_ActionStatement)

        RETURN DISTINCT 
            s.name AS FormalStakeholder,
            m.name AS Mission,
            ms.name AS MissionStatement,
            g.name AS Goal,
            gs.name AS GoalStatement,
            a.name AS Action,
            as.name AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table

def get_carbon2_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:CARBON_FVRA_LTWO_LABEL {name: $formalStakeholder})
            <-[:CARBON_FVRA_LTWO_ACTION_LABEL_LINK]-(a:CARBON_FVRA_LTWO_ACTION)
            <-[:CARBON_FVRA_LTWO_GOALACTION_LINK]-(g:CARBON_FVRA_LTWO_GOAL)
            <-[:CARBON_FVRA_LTWO_MISSIONGOAL_LINK]-(m:CARBON_FVRA_LTWO_MISSION)

        OPTIONAL MATCH (m)-[:CARBON_FVRA_LTWO_MISSION_LINK]->(ms:CARBON_FVRA_LTWO_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:CARBON_FVRA_LTWO_GOAL_LINK]->(gs:CARBON_FVRA_LTWO_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:CARBON_FVRA_LTWO_ACTION_LINK]->(as:CARBON_FVRA_LTWO_ACTION_STATEMENT)

        RETURN DISTINCT 
            l.name AS FormalStakeholder,
            m.name AS Mission,
            ms.text AS MissionStatement,
            g.name AS Goal,
            gs.text AS GoalStatement,
            a.name AS Action,
            as.text AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table
    
def get_water2_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:WATER_FVRA_LTWO_LABEL {name: $formalStakeholder})
            <-[:WATER_FVRA_LTWO_ACTION_LABEL_LINK]-(a:WATER_FVRA_LTWO_ACTION)
            <-[:WATER_FVRA_LTWO_GOALACTION_LINK]-(g:WATER_FVRA_LTWO_GOAL)
            <-[:WATER_FVRA_LTWO_MISSIONGOAL_LINK]-(m:WATER_FVRA_LTWO_MISSION)

        OPTIONAL MATCH (m)-[:WATER_FVRA_LTWO_MISSION_LINK]->(ms:WATER_FVRA_LTWO_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:WATER_FVRA_LTWO_GOAL_LINK]->(gs:WATER_FVRA_LTWO_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:WATER_FVRA_LTWO_ACTION_LINK]->(as:WATER_FVRA_LTWO_ACTION_STATEMENT)

        RETURN DISTINCT 
            l.name AS FormalStakeholder,
            m.name AS Mission,
            ms.text AS MissionStatement,
            g.name AS Goal,
            gs.text AS GoalStatement,
            a.name AS Action,
            as.text AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table
    
def get_live2_fvstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:LIVE_FVRA_LTWO_LABEL {name: $formalStakeholder})
            <-[:LIVE_FVRA_LTWO_ACTION_LABEL_LINK]-(a:LIVE_FVRA_LTWO_ACTION)
            <-[:LIVE_FVRA_LTWO_GOALACTION_LINK]-(g:LIVE_FVRA_LTWO_GOAL)
            <-[:LIVE_FVRA_LTWO_MISSIONGOAL_LINK]-(m:LIVE_FVRA_LTWO_MISSION)

        OPTIONAL MATCH (m)-[:LIVE_FVRA_LTWO_MISSION_LINK]->(ms:LIVE_FVRA_LTWO_MISSION_STATEMENT)
        OPTIONAL MATCH (g)-[:LIVE_FVRA_LTWO_GOAL_LINK]->(gs:LIVE_FVRA_LTWO_GOAL_STATEMENT)
        OPTIONAL MATCH (a)-[:LIVE_FVRA_LTWO_ACTION_LINK]->(as:LIVE_FVRA_LTWO_ACTION_STATEMENT)

        RETURN DISTINCT 
            l.name AS FormalStakeholder,
            m.name AS Mission,
            ms.text AS MissionStatement,
            g.name AS Goal,
            gs.text AS GoalStatement,
            a.name AS Action,
            as.text AS ActionStatement
        ORDER BY Mission, Goal, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["FormalStakeholder"],
                "Mission": record["Mission"],
                "Mission Statement": record.get("MissionStatement"),
                "Goal": record["Goal"],
                "Goal Statement": record.get("GoalStatement"),
                "Action": record["Action"],
                "Action Statement": record.get("ActionStatement")
            })
        return table
    

def get_fvstakeholder_plan(query, formalStakeholder, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvstakeholder(formalStakeholder)
    elif query == "wat" and access == 'levelone':
        return get_water_fvstakeholder(formalStakeholder)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fvstakeholder(formalStakeholder)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvstakeholder(formalStakeholder)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvstakeholder(formalStakeholder)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fvstakeholder(formalStakeholder)
    else:
        return []
