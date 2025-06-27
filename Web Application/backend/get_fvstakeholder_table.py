from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvstakeholder():
    query = """
        MATCH (s:CARBON_FVSTAKEHOLDER_Stakeholder)
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

def get_water_fvstakeholder():
    query = """
        MATCH (s:WATER_FVSTAKEHOLDER_Stakeholder)
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
    
def get_livelihood_fvstakeholder():
    query = """
        MATCH (s:LIVE_FVSTAKEHOLDER_Stakeholder)
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

def get_carbon2_fvstakeholder():
    query = """
        MATCH (s:CARBON_FVRA_LTWO_LABEL)
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

def get_water2_fvstakeholder():
    query = """
        MATCH (s:WATER_FVRA_LTWO_LABEL)
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
    
def get_livelihood2_fvstakeholder():
    query = """
        MATCH (s:LIVE_FVRA_LTWO_LABEL)
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
    
def get_fvstakeholder_table(query, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvstakeholder()
    elif query == "wat" and access == 'levelone':
        return get_water_fvstakeholder()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fvstakeholder()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvstakeholder()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvstakeholder()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fvstakeholder()
    else:
        return []
