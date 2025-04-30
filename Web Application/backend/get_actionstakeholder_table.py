from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_actionstakeholder_plan():
    query = """
        MATCH (s:CARBON_ACTIONBYSTAKE_Stakeholder)
        RETURN DISTINCT s.name AS FormalStakeholder
        ORDER BY FormalStakeholder
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"]
            })
        return table

def get_water_actionstakeholder_plan():
    query = """
        MATCH (s:WATER_ACTIONBYSTAKE_Stakeholder)
        RETURN DISTINCT s.name AS FormalStakeholder
        ORDER BY FormalStakeholder
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"]
            })
        return table
    
def get_livelihood_actionstakeholder_plan():
    query = """
        MATCH (s:LIVE_ACTIONBYSTAKE_Stakeholder)
        RETURN DISTINCT s.name AS FormalStakeholder
        ORDER BY FormalStakeholder
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Formal Stakeholder": record["FormalStakeholder"]
            })
        return table
    
def get_actionstakeholder_table(query):
    if query == "car":
        return get_carbon_actionstakeholder_plan()
    elif query == "wat":
        return get_water_actionstakeholder_plan()
    elif query == "liv":
        return get_livelihood_actionstakeholder_plan()
    else:
        return []
