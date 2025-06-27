from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:CARBON_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
            -[:CARBON_AP_LONE_HAS_CATEGORY]->(c:CARBON_AP_LONE_CATEGORY),
            (s)<-[:CARBON_AP_LONE_HAS_STAKEHOLDER]-(a:CARBON_AP_LONE_ACTION)
            <-[:CARBON_AP_LONE_HAS_ACTION]-(f:CARBON_AP_LONE_FILE)
        RETURN 
            s.name AS Stakeholder,
            f.name AS File,
            a.name AS Action,
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"],
                "Category" : record["Category"]
            })
        return table

def get_water_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:WATER_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
            -[:WATER_AP_LONE_HAS_CATEGORY]->(c:WATER_AP_LONE_CATEGORY),
            (s)<-[:WATER_AP_LONE_HAS_STAKEHOLDER]-(a:WATER_AP_LONE_ACTION)
            <-[:WATER_AP_LONE_HAS_ACTION]-(f:WATER_AP_LONE_FILE)
        RETURN 
            s.name AS Stakeholder,
            f.name AS File,
            a.name AS Action,
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"],
                "Category" : record["Category"]
            })
        return table
    
def get_livelihood_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (s:LIVE_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
            -[:LIVE_AP_LONE_HAS_CATEGORY]->(c:LIVE_AP_LONE_CATEGORY),
            (s)<-[:LIVE_AP_LONE_HAS_STAKEHOLDER]-(a:LIVE_AP_LONE_ACTION)
            <-[:LIVE_AP_LONE_HAS_ACTION]-(f:LIVE_AP_LONE_FILE)
        RETURN 
            s.name AS Stakeholder,
            f.name AS File,
            a.name AS Action,
            c.name AS Category
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Stakeholder": record["Stakeholder"],
                "File": record["File"],
                "Action" : record["Action"],
                "Category" : record["Category"]
            })
        return table

def get_carbon_l2_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (l:CARBON_AP_LTWO_LABELS {name: $formalStakeholder})
            <-[:CARBON_AP_LTWO_HAS_LABELS]-(a:CARBON_AP_LTWO_ACTION)
            <-[:CARBON_AP_LTWO_HAS_ACTION]-(f:CARBON_AP_LTWO_FILE)
        RETURN DISTINCT
            l.name AS Label,
            f.name AS File,
            a.name AS Action
        ORDER BY Label, File, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table
    
def get_water_l2_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (l:WATER_AP_LTWO_LABELS {name: $formalStakeholder})
            <-[:WATER_AP_LTWO_HAS_LABELS]-(a:WATER_AP_LTWO_ACTION)
            <-[:WATER_AP_LTWO_HAS_ACTION]-(f:WATER_AP_LTWO_FILE)
        RETURN DISTINCT
            l.name AS Label,
            f.name AS File,
            a.name AS Action
        ORDER BY Label, File, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table
    
def get_live_l2_actionstakeholder_plan_stakeholder(formalStakeholder: str):
    query = """
        MATCH (l:LIVE_AP_LTWO_LABELS {name: $formalStakeholder})
            <-[:LIVE_AP_LTWO_HAS_LABELS]-(a:LIVE_AP_LTWO_ACTION)
            <-[:LIVE_AP_LTWO_HAS_ACTION]-(f:LIVE_AP_LTWO_FILE)
        RETURN DISTINCT
            l.name AS Label,
            f.name AS File,
            a.name AS Action
        ORDER BY Label, File, Action
    """
    with driver.session() as session:
        results = session.run(query, formalStakeholder = formalStakeholder)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "File": record["File"],
                "Action" : record["Action"]
            })
        return table
    
def get_actionstakeholder_plan(query, formalStakeholder, access):
    if query == "car" and access == 'levelone':
        return get_carbon_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "wat" and access == 'levelone':
        return get_water_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "liv" and access == 'levelone':
        return get_livelihood_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "car" and access == 'leveltwo':
        return get_carbon_l2_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "wat" and access == 'leveltwo':
        return get_water_l2_actionstakeholder_plan_stakeholder(formalStakeholder)
    elif query == "liv" and access == 'leveltwo':
        return get_live_l2_actionstakeholder_plan_stakeholder(formalStakeholder)
    else:
        return []
