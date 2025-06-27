from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw(recommendation:str, action: str):
    query = """
        MATCH (r:CARBON_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:CARBON_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:CARBON_LONE_FWSTAKEHOLDER_Action {name: $action})
            -[:CARBON_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (s:CARBON_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS `Stakeholder`
        ORDER BY s.name
        """
    
    with driver.session() as session:
        results = session.run(query, recommendation = recommendation, action = action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table

def get_water_fw(recommendation:str, action: str):
    query = """
        MATCH (r:WATER_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:WATER_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:WATER_LONE_FWSTAKEHOLDER_Action {name: $action})
            -[:WATER_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (s:WATER_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS `Stakeholder`
        ORDER BY s.name
        """
    
    with driver.session() as session:
        results = session.run(query, recommendation = recommendation, action = action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table
    
def get_livelihood_fw(recommendation:str, action: str):
    query = """
        MATCH (r:LIVE_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:LIVE_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:LIVE_LONE_FWSTAKEHOLDER_Action {name: $action})
            -[:LIVE_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (s:LIVE_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS `Stakeholder`
        ORDER BY s.name
        """
    with driver.session() as session:
        results = session.run(query, recommendation = recommendation, action = action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action" : record["Action"],
                "Stakeholder" : record["Stakeholder"]
            })
        return table

def get_carbon2_fw(recommendation: str, action: str):
    query = """
        MATCH (r:CARBON_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:CARBON_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:CARBON_LTWO_FWSTAKEHOLDER_Action {name: $action})
            -[:CARBON_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (l:CARBON_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Label
        ORDER BY Recommendation, Action, Label
    """
    
    with driver.session() as session:
        results = session.run(query, recommendation=recommendation, action=action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"],
                "Stakeholder": record["Label"]
            })
        return table


def get_water2_fw(recommendation: str, action: str):
    print(f"Searching for Recommendation: '{recommendation}', Action: '{action}'")
    query = """
        MATCH (r:WATER_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:WATER_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:WATER_LTWO_FWSTAKEHOLDER_Action {name: $action})
            -[:WATER_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (l:WATER_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Label
        ORDER BY Recommendation, Action, Label
    """
    
    with driver.session() as session:
        results = session.run(query, recommendation=recommendation, action=action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"],
                "Stakeholder": record["Label"]
            })
        return table

def get_live2_fw(recommendation: str, action: str):
    query = """
        MATCH (r:LIVE_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:LIVE_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
            (a:LIVE_LTWO_FWSTAKEHOLDER_Action {name: $action})
            -[:LIVE_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
            (l:LIVE_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Label
        ORDER BY Recommendation, Action, Label
    """
    
    with driver.session() as session:
        results = session.run(query, recommendation=recommendation, action=action)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"],
                "Stakeholder": record["Label"]
            })
        return table

def get_fw(query, recommendation, action, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fw(recommendation, action)
    elif query == "wat" and access == 'levelone':
        return get_water_fw(recommendation, action)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fw(recommendation, action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fw(recommendation, action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fw(recommendation, action)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fw(recommendation, action)
    else:
        return []
