from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fwstakeholder():
    query = """
        MATCH (s:CARBON_LONE_FWSTAKEHOLDER_Stakeholder)
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

def get_water_fwstakeholder():
    query = """
        MATCH (s:WATER_LONE_FWSTAKEHOLDER_Stakeholder)
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
    
def get_livelihood_fwstakeholder():
    query = """
        MATCH (s:LIVE_LONE_FWSTAKEHOLDER_Stakeholder)
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

def get_carbon2_fwstakeholder():
    query = """
        MATCH (s:CARBON_LTWO_FWSTAKEHOLDER_Labels)
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

def get_water2_fwstakeholder():
    query = """
        MATCH (s:WATER_LTWO_FWSTAKEHOLDER_Labels)
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
    
def get_livelihood2_fwstakeholder():
    query = """
        MATCH (s:LIVE_LTWO_FWSTAKEHOLDER_Labels)
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

def get_fwstakeholder_table(query, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fwstakeholder()
    elif query == "wat" and access == 'levelone':
        return get_water_fwstakeholder()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fwstakeholder()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fwstakeholder()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fwstakeholder()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fwstakeholder()
    else:
        return []
