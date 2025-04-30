from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:CARBON_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:CARBON_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:CARBON_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:CARBON_FWSTAKEHOLDER_HAS_ACTION]->(a:CARBON_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            s.name AS FormalStakeholder, 
            r.name AS Recommendation, 
            a.name AS Action
        ORDER BY FormalStakeholder, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:WATER_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:WATER_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:WATER_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:WATER_FWSTAKEHOLDER_HAS_ACTION]->(a:WATER_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            s.name AS FormalStakeholder, 
            r.name AS Recommendation, 
            a.name AS Action
        ORDER BY FormalStakeholder, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood_fwstakeholder(formalStakeholder: str):
    query = """
        MATCH (s:LIVE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:LIVE_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:LIVE_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:LIVE_FWSTAKEHOLDER_HAS_ACTION]->(a:LIVE_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            s.name AS FormalStakeholder, 
            r.name AS Recommendation, 
            a.name AS Action
        ORDER BY FormalStakeholder, Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder=formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"],
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_fwstakeholder_plan(query, formalStakeholder):
    if query == "car":
        return get_carbon_fwstakeholder(formalStakeholder)
    elif query == "wat":
        return get_water_fwstakeholder(formalStakeholder)
    elif query == "liv":
        return get_livelihood_fwstakeholder(formalStakeholder)
    else:
        return []
