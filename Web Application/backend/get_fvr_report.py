from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVR_LONE_MISSION)
        MATCH (m)-[:CARBON_FVR_LONE_MISSION_LINK]->(ms:CARBON_FVR_LONE_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVR_LONE_MISSIONGOAL_LINK]->(g:CARBON_FVR_LONE_GOAL)
        MATCH (g)-[:CARBON_FVR_LONE_GOAL_LINK]->(gs:CARBON_FVR_LONE_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVR_LONE_GOALACTION_LINK]->(a:CARBON_FVR_LONE_ACTION {name: $action})
        MATCH (a)-[:CARBON_FVR_LONE_ACTION_LINK]->(as:CARBON_FVR_LONE_ACTION_STATEMENT)
        MATCH (a)-[:CARBON_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:CARBON_FVR_LONE_PROGRAMME)
        MATCH (p)-[:CARBON_FVR_LONE_PROGRAMME_REPORT_LINK]->(rs:CARBON_FVR_LONE_REPORT_SUMMARY)
        MATCH (rs)-[:CARBON_FVR_LONE_REPORT_STAKE_LINK]->(fs:CARBON_FVR_LONE_Formal_Stakeholder)
        OPTIONAL MATCH (fs)-[:CARBON_FVR_LONE_HAS_REPORT_CATEGORY]->(rc:CARBON_FVR_LONE_Report_Category)

        WITH 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            fs.name AS formal_stakeholder,
            rc.name AS report_category,
            COLLECT(DISTINCT rs.text)[0] AS report_summary  // Pick the first summary

        RETURN 
            mission,
            mission_statement,
            goal,
            goal_statement,
            action,
            action_statement,
            programme,
            report_summary,
            formal_stakeholder,
            report_category
        ORDER BY mission, goal, action
        """
    
    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []
        
        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["formal_stakeholder"],
                record["report_category"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["formal_stakeholder"],
                    "Stakeholder Category": record["report_category"]
                })
        
        return table

def get_water_fvr_report_stakeholder(action: str):
    query = """
            MATCH (m:WATER_FVR_LONE_MISSION)
            MATCH (m)-[:WATER_FVR_LONE_MISSION_LINK]->(ms:WATER_FVR_LONE_MISSION_STATEMENT)
            MATCH (m)-[:WATER_FVR_LONE_MISSIONGOAL_LINK]->(g:WATER_FVR_LONE_GOAL)
            MATCH (g)-[:WATER_FVR_LONE_GOAL_LINK]->(gs:WATER_FVR_LONE_GOAL_STATEMENT)
            MATCH (g)-[:WATER_FVR_LONE_GOALACTION_LINK]->(a:WATER_FVR_LONE_ACTION {name: $action})
            MATCH (a)-[:WATER_FVR_LONE_ACTION_LINK]->(as:WATER_FVR_LONE_ACTION_STATEMENT)
            MATCH (a)-[:WATER_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:WATER_FVR_LONE_PROGRAMME)
            MATCH (p)-[:WATER_FVR_LONE_PROGRAMME_REPORT_LINK]->(rs:WATER_FVR_LONE_REPORT_SUMMARY)
            MATCH (rs)-[:WATER_FVR_LONE_REPORT_STAKE_LINK]->(fs:WATER_FVR_LONE_Formal_Stakeholder)
            OPTIONAL MATCH (fs)-[:WATER_FVR_LONE_HAS_REPORT_CATEGORY]->(rc:WATER_FVR_LONE_Report_Category)

            WITH 
                m.name AS mission,
                ms.text AS mission_statement,
                g.name AS goal,
                gs.text AS goal_statement,
                a.name AS action,
                as.text AS action_statement,
                p.name AS programme,
                fs.name AS formal_stakeholder,
                rc.name AS report_category,
                COLLECT(DISTINCT rs.text)[0] AS report_summary  // Pick the first summary

            RETURN 
                mission,
                mission_statement,
                goal,
                goal_statement,
                action,
                action_statement,
                programme,
                report_summary,
                formal_stakeholder,
                report_category
            ORDER BY mission, goal, action
    """
    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []
        
        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["formal_stakeholder"],
                record["report_category"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["formal_stakeholder"],
                    "Stakeholder Category": record["report_category"]
                })
        
        return table
    
def get_livelihood_fvr_report_stakeholder(action: str):
    query = """
            MATCH (m:LIVE_FVR_LONE_MISSION)
            MATCH (m)-[:LIVE_FVR_LONE_MISSION_LINK]->(ms:LIVE_FVR_LONE_MISSION_STATEMENT)
            MATCH (m)-[:LIVE_FVR_LONE_MISSIONGOAL_LINK]->(g:LIVE_FVR_LONE_GOAL)
            MATCH (g)-[:LIVE_FVR_LONE_GOAL_LINK]->(gs:LIVE_FVR_LONE_GOAL_STATEMENT)
            MATCH (g)-[:LIVE_FVR_LONE_GOALACTION_LINK]->(a:LIVE_FVR_LONE_ACTION {name: $action})
            MATCH (a)-[:LIVE_FVR_LONE_ACTION_LINK]->(as:LIVE_FVR_LONE_ACTION_STATEMENT)
            MATCH (a)-[:LIVE_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:LIVE_FVR_LONE_PROGRAMME)
            MATCH (p)-[:LIVE_FVR_LONE_PROGRAMME_REPORT_LINK]->(rs:LIVE_FVR_LONE_REPORT_SUMMARY)
            MATCH (rs)-[:LIVE_FVR_LONE_REPORT_STAKE_LINK]->(fs:LIVE_FVR_LONE_Formal_Stakeholder)
            OPTIONAL MATCH (fs)-[:LIVE_FVR_LONE_HAS_REPORT_CATEGORY]->(rc:LIVE_FVR_LONE_Report_Category)

            WITH 
                m.name AS mission,
                ms.text AS mission_statement,
                g.name AS goal,
                gs.text AS goal_statement,
                a.name AS action,
                as.text AS action_statement,
                p.name AS programme,
                fs.name AS formal_stakeholder,
                rc.name AS report_category,
                COLLECT(DISTINCT rs.text)[0] AS report_summary  // Pick the first summary

            RETURN 
                mission,
                mission_statement,
                goal,
                goal_statement,
                action,
                action_statement,
                programme,
                report_summary,
                formal_stakeholder,
                report_category
            ORDER BY mission, goal, action
        """
    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []
        
        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["formal_stakeholder"],
                record["report_category"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["formal_stakeholder"],
                    "Stakeholder Category": record["report_category"]
                })
        
        return table

def get_carbon2_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:CARBON_FVR_LTWO_MISSION)-[:CARBON_FVR_LTWO_MISSION_LINK]->(ms:CARBON_FVR_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVR_LTWO_MISSIONGOAL_LINK]->(g:CARBON_FVR_LTWO_GOAL)
        MATCH (g)-[:CARBON_FVR_LTWO_GOAL_LINK]->(gs:CARBON_FVR_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVR_LTWO_GOALACTION_LINK]->(a:CARBON_FVR_LTWO_ACTION {name: $action})
        MATCH (a)-[:CARBON_FVR_LTWO_ACTION_LINK]->(as:CARBON_FVR_LTWO_ACTION_STATEMENT)
        MATCH (a)-[:CARBON_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:CARBON_FVR_LTWO_PROGRAMME)
        MATCH (p)-[:CARBON_FVR_LTWO_PROGRAMME_REPORT_LINK]->(rs:CARBON_FVR_LTWO_REPORT_SUMMARY)
        MATCH (rs)-[:CARBON_FVR_LTWO_REPORT_LABEL_LINK]->(l:CARBON_FVR_LTWO_LABEL)

        WITH 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            l.name AS report_label,
            COLLECT(DISTINCT rs.text)[0] AS report_summary  // Get the first summary

        RETURN 
            mission,
            mission_statement,
            goal,
            goal_statement,
            action,
            action_statement,
            programme,
            report_summary,
            report_label
        ORDER BY mission, goal, action
    """

    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []

        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["report_label"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["report_label"]
                })

        return table

def get_water2_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:WATER_FVR_LTWO_MISSION)-[:WATER_FVR_LTWO_MISSION_LINK]->(ms:WATER_FVR_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVR_LTWO_MISSIONGOAL_LINK]->(g:WATER_FVR_LTWO_GOAL)
        MATCH (g)-[:WATER_FVR_LTWO_GOAL_LINK]->(gs:WATER_FVR_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVR_LTWO_GOALACTION_LINK]->(a:WATER_FVR_LTWO_ACTION {name: $action})
        MATCH (a)-[:WATER_FVR_LTWO_ACTION_LINK]->(as:WATER_FVR_LTWO_ACTION_STATEMENT)
        MATCH (a)-[:WATER_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:WATER_FVR_LTWO_PROGRAMME)
        MATCH (p)-[:WATER_FVR_LTWO_PROGRAMME_REPORT_LINK]->(rs:WATER_FVR_LTWO_REPORT_SUMMARY)
        MATCH (rs)-[:WATER_FVR_LTWO_REPORT_LABEL_LINK]->(l:WATER_FVR_LTWO_LABEL)

        WITH 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            l.name AS report_label,
            COLLECT(DISTINCT rs.text)[0] AS report_summary  // Get the first summary

        RETURN 
            mission,
            mission_statement,
            goal,
            goal_statement,
            action,
            action_statement,
            programme,
            report_summary,
            report_label
        ORDER BY mission, goal, action
    """

    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []

        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["report_label"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["report_label"]
                })

        return table

def get_live2_fvr_report_stakeholder(action: str):
    query = """
        MATCH (m:LIVE_FVR_LTWO_MISSION)-[:LIVE_FVR_LTWO_MISSION_LINK]->(ms:LIVE_FVR_LTWO_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVR_LTWO_MISSIONGOAL_LINK]->(g:LIVE_FVR_LTWO_GOAL)
        MATCH (g)-[:LIVE_FVR_LTWO_GOAL_LINK]->(gs:LIVE_FVR_LTWO_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVR_LTWO_GOALACTION_LINK]->(a:LIVE_FVR_LTWO_ACTION {name: $action})
        MATCH (a)-[:LIVE_FVR_LTWO_ACTION_LINK]->(as:LIVE_FVR_LTWO_ACTION_STATEMENT)
        MATCH (a)-[:LIVE_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:LIVE_FVR_LTWO_PROGRAMME)
        MATCH (p)-[:LIVE_FVR_LTWO_PROGRAMME_REPORT_LINK]->(rs:LIVE_FVR_LTWO_REPORT_SUMMARY)
        MATCH (rs)-[:LIVE_FVR_LTWO_REPORT_LABEL_LINK]->(l:LIVE_FVR_LTWO_LABEL)

        WITH 
            m.name AS mission,
            ms.text AS mission_statement,
            g.name AS goal,
            gs.text AS goal_statement,
            a.name AS action,
            as.text AS action_statement,
            p.name AS programme,
            l.name AS report_label,
            COLLECT(DISTINCT rs.text)[0] AS report_summary  // Get the first summary

        RETURN 
            mission,
            mission_statement,
            goal,
            goal_statement,
            action,
            action_statement,
            programme,
            report_summary,
            report_label
        ORDER BY mission, goal, action
    """

    with driver.session() as session:
        results = session.run(query, action=action)
        seen = set()
        table = []

        for record in results:
            row_tuple = (
                record["mission"],
                record["mission_statement"],
                record["goal"],
                record["goal_statement"],
                record["action"],
                record["action_statement"],
                record["programme"],
                record["report_summary"],
                record["report_label"],
            )
            if row_tuple not in seen:
                seen.add(row_tuple)
                table.append({
                    "Mission": record["mission"],
                    "Mission Statement": record["mission_statement"],
                    "Goal": record["goal"],
                    "Goal Statement": record["goal_statement"],
                    "Action": record["action"],
                    "Action Statement": record["action_statement"],
                    "Initiative": record["programme"],
                    "Report Summary": record["report_summary"],
                    "Report Stakeholder": record["report_label"]
                })

        return table

def get_fvr_report(query, action,access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvr_report_stakeholder(action)
    elif query == "wat" and access == 'levelone':
        return get_water_fvr_report_stakeholder(action)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fvr_report_stakeholder(action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvr_report_stakeholder(action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvr_report_stakeholder(action)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fvr_report_stakeholder(action)
    else:
        return []
