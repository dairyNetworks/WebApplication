from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:CARBON_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:CARBON_LONE_FWSTAKEHOLDER_Action)-[:CARBON_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:CARBON_LONE_FWSTAKEHOLDER_Recommendation)-[:CARBON_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS Stakeholder
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:WATER_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:WATER_LONE_FWSTAKEHOLDER_Action)-[:WATER_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:WATER_LONE_FWSTAKEHOLDER_Recommendation)-[:WATER_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS Stakeholder
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:LIVE_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:LIVE_LONE_FWSTAKEHOLDER_Action)-[:LIVE_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:LIVE_LONE_FWSTAKEHOLDER_Recommendation)-[:LIVE_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)

        RETURN DISTINCT
            r.name AS Recommendation,
            a.name AS Action,
            s.name AS Stakeholder
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_carbon2_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:CARBON_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:CARBON_LTWO_FWSTAKEHOLDER_Action)-[:CARBON_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(l)
        MATCH (r:CARBON_LTWO_FWSTAKEHOLDER_Recommendation)-[:CARBON_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Labels
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Labels"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water2_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:WATER_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:WATER_LTWO_FWSTAKEHOLDER_Action)-[:WATER_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(l)
        MATCH (r:WATER_LTWO_FWSTAKEHOLDER_Recommendation)-[:WATER_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Labels
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Labels"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_live2_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (l:LIVE_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:LIVE_LTWO_FWSTAKEHOLDER_Action)-[:LIVE_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(l)
        MATCH (r:LIVE_LTWO_FWSTAKEHOLDER_Recommendation)-[:LIVE_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            r.name AS Recommendation,
            a.name AS Action,
            l.name AS Labels
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Labels"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_fwstakeholder_plan(query, formalStakeholder, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fwstakeholder(formalStakeholder)
    elif query == "wat" and access == 'levelone':
        return get_water_fwstakeholder(formalStakeholder)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fwstakeholder(formalStakeholder)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fwstakeholder(formalStakeholder)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fwstakeholder(formalStakeholder)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fwstakeholder(formalStakeholder)
    else:
        return []
