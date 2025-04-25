from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_report_stakeholder(action: str):
    query = """
            MATCH (m:CARBON_FVR_MISSION)
            MATCH (m)-[:CARBON_FVR_MISSION_LINK]->(ms:CARBON_FVR_MISSION_STATEMENT)
            MATCH (g:CARBON_FVR_GOAL)
            MATCH (g)-[:CARBON_FVR_GOAL_LINK]->(gs:CARBON_FVR_GOAL_STATEMENT)
            MATCH (a:CARBON_FVR_ACTION)
            WHERE a.name = $action
            MATCH (a)-[:CARBON_FVR_ACTION_LINK]->(as:CARBON_FVR_ACTION_STATEMENT)
            MATCH (g)-[:CARBON_FVR_GOALACTION_LINK]->(a)
            MATCH (p:CARBON_FVR_PROGRAMME)
            MATCH (a)-[:CARBON_FVR_ACTION_PROGRAMME_LINK]->(p)
            MATCH (rs:CARBON_FVR_REPORT_SUMMARY)
            MATCH (p)-[:CARBON_FVR_PROGRAMME_REPORT_LINK]->(rs)
            MATCH (fs:CARBON_FVR_Formal_Stakeholder)
            MATCH (rs)-[:CARBON_FVR_REPORT_STAKE_LINK]->(fs)
            RETURN DISTINCT 
                m.name AS mission,
                ms.text AS mission_statement,
                g.name AS goal,
                gs.text AS goal_statement,
                a.name AS action,
                as.text AS action_statement,
                p.name AS programme,
                rs.text AS report_summary,
                fs.name AS formal_stakeholder
        """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["mission"],
                "Mission Statement": record["mission_statement"],
                "Goal" : record["goal"],
                "Goal Statement" : record["goal_statement"],
                "Action" : record["action"],
                "Action Statement" : record["action_statement"],
                "Programme" : record["programme"],
                "Report Summary" : record["report_summary"],
                "Report Stakeholder" : record["formal_stakeholder"]
            })
        return table

def get_water_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVR_MISSION)
        MATCH (m)-[:WATER_FVR_MISSION_LINK]->(ms:WATER_FVR_MISSION_STATEMENT)
        MATCH (g:WATER_FVR_GOAL)
        MATCH (g)-[:WATER_FVR_GOAL_LINK]->(gs:WATER_FVR_GOAL_STATEMENT)
        MATCH (a:WATER_FVR_ACTION)
        WHERE a.name = $action
        MATCH (a)-[:WATER_FVR_ACTION_LINK]->(as:WATER_FVR_ACTION_STATEMENT)
        MATCH (g)-[:WATER_FVR_GOALACTION_LINK]->(a)
        MATCH (p:WATER_FVR_PROGRAMME)
        MATCH (a)-[:WATER_FVR_ACTION_PROGRAMME_LINK]->(p)
        MATCH (rs:WATER_FVR_REPORT_SUMMARY)
        MATCH (p)-[:WATER_FVR_PROGRAMME_REPORT_LINK]->(rs)
        MATCH (fs:WATER_FVR_Formal_Stakeholder)
        MATCH (rs)-[:WATER_FVR_REPORT_STAKE_LINK]->(fs)
        RETURN DISTINCT 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            rs.text AS report_summary,
            fs.name AS formal_stakeholder
    """
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["mission"],
                "Mission Statement": record["mission_statement"],
                "Goal" : record["goal"],
                "Goal Statement" : record["goal_statement"],
                "Action" : record["action"],
                "Action Statement" : record["action_statement"],
                "Programme" : record["programme"],
                "Report Summary" : record["report_summary"],
                "Report Stakeholder" : record["formal_stakeholder"]
            })
        return table
    
def get_livelihood_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVR_MISSION)
        MATCH (m)-[:LIVE_FVR_MISSION_LINK]->(ms:LIVE_FVR_MISSION_STATEMENT)
        MATCH (g:LIVE_FVR_GOAL)
        MATCH (g)-[:LIVE_FVR_GOAL_LINK]->(gs:LIVE_FVR_GOAL_STATEMENT)
        MATCH (a:LIVE_FVR_ACTION)
        WHERE a.name = $action
        MATCH (a)-[:LIVE_FVR_ACTION_LINK]->(as:LIVE_FVR_ACTION_STATEMENT)
        MATCH (g)-[:LIVE_FVR_GOALACTION_LINK]->(a)
        MATCH (p:LIVE_FVR_PROGRAMME)
        MATCH (a)-[:LIVE_FVR_ACTION_PROGRAMME_LINK]->(p)
        MATCH (rs:LIVE_FVR_REPORT_SUMMARY)
        MATCH (p)-[:LIVE_FVR_PROGRAMME_REPORT_LINK]->(rs)
        MATCH (fs:LIVE_FVR_Formal_Stakeholder)
        MATCH (rs)-[:LIVE_FVR_REPORT_STAKE_LINK]->(fs)
        RETURN DISTINCT 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            rs.text AS report_summary,
            fs.name AS formal_stakeholder
        """
    with driver.session() as session:
        results = session.run(query, action=action)
        table = []
        for record in results:
            table.append({
                "Mission": record["mission"],
                "Mission Statement": record["mission_statement"],
                "Goal" : record["goal"],
                "Goal Statement" : record["goal_statement"],
                "Action" : record["action"],
                "Action Statement" : record["action_statement"],
                "Programme" : record["programme"],
                "Report Summary" : record["report_summary"],
                "Report Stakeholder" : record["formal_stakeholder"]
            })
        return table
    
def get_fvr_report(query, action):
    if query == "car":
        return get_carbon_fvr_report_stakeholder(action)
    elif query == "wat":
        return get_water_fvr_report_stakeholder(action)
    elif query == "liv":
        return get_livelihood_fvr_report_stakeholder(action)
    else:
        return []
