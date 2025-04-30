from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:CARBON_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:CARBON_ACTIONBYSTAKE_HAS_FILE]->(f:CARBON_ACTIONBYSTAKE_File)
            -[:CARBON_ACTIONBYSTAKE_HAS_ACTION]->(a:CARBON_ACTIONBYSTAKE_Action)
        RETURN s.name AS Stakeholder, f.name AS File, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table

def get_water_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:WATER_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:WATER_ACTIONBYSTAKE_HAS_FILE]->(f:WATER_ACTIONBYSTAKE_File)
            -[:WATER_ACTIONBYSTAKE_HAS_ACTION]->(a:WATER_ACTIONBYSTAKE_Action)
        RETURN s.name AS Stakeholder, f.name AS File, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table
    
def get_livelihood_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:LIVE_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:LIVE_ACTIONBYSTAKE_HAS_FILE]->(f:LIVE_ACTIONBYSTAKE_File)
            -[:LIVE_ACTIONBYSTAKE_HAS_ACTION]->(a:LIVE_ACTIONBYSTAKE_Action)
        RETURN s.name AS Stakeholder, f.name AS File, a.name AS Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table
    
def get_actionstakeholder_plan(query, formalStakeholder):
    if query == "car":
        return get_carbon_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "wat":
        return get_water_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "liv":
        return get_livelihood_actionstakeholder_plan_stakeholder(formalStakeholder)
    else:
        return []
