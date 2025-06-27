from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw():
    query = """
        MATCH (r:CARBON_LONE_FWSTAKEHOLDER_Recommendation)-[:CARBON_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:CARBON_LONE_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water_fw():
    query = """
        MATCH (r:WATER_LONE_FWSTAKEHOLDER_Recommendation)-[:WATER_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:WATER_LONE_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood_fw():
    query = """
        MATCH (r:LIVE_LONE_FWSTAKEHOLDER_Recommendation)-[:LIVE_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:LIVE_LONE_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_carbon2_fw():
    query = """
        MATCH (r:CARBON_LTWO_FWSTAKEHOLDER_Recommendation)-[:CARBON_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:CARBON_LTWO_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table

def get_water2_fw():
    query = """
        MATCH (r:WATER_LTWO_FWSTAKEHOLDER_Recommendation)-[:WATER_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:WATER_LTWO_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_livelihood2_fw():
    query = """
        MATCH (r:LIVE_LTWO_FWSTAKEHOLDER_Recommendation)-[:LIVE_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:LIVE_LTWO_FWSTAKEHOLDER_Action)
        RETURN DISTINCT 
        r.name AS Recommendation, 
        r.shortRecommendation AS ShortRecommendation, 
        a.name AS Action, 
        a.shortAction AS ShortAction
        ORDER BY Recommendation, Action
    """
    with driver.session() as session:
        results = session.run(query)
        table = []
        for record in results:
            table.append({
                "Recommendation": record["Recommendation"],
                "Action": record["Action"]
            })
        return table
    
def get_fw_table(query,access):
    if query == "car" and access == 'levelone':
        return get_carbon_fw()
    elif query == "wat" and access == 'levelone':
        return get_water_fw()
    elif query == "liv" and access == 'levelone':
        return get_livelihood_fw()
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fw()
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fw()
    elif query == "liv" and access == 'leveltwo':
        return get_livelihood2_fw()
    else:
        return []
