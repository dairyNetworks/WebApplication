from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_action_plan_stakeholder_network(file_name: str, action: str):
    cypher_query = """
        MATCH (f:CARBON_AP_FILE)-[:CARBON_AP_ACTION]->(a:CARBON_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:CARBON_AP_ACTION_STAKEHOLDER]->(s:CARBON_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            id(f) AS id_f, f.name AS label_f, 'File Name' AS type_f, 
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a, 
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, file_name=file_name, action=action)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['f', 'a', 's']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            links.append({"source": record["id_f"], "target": record["id_a"], "type": "HAS_ACTION"})
            links.append({"source": record["id_a"], "target": record["id_s"], "type": "INVOLVES"})

        print(f"\n✅ Total nodes: {len(nodes)}, Total links: {len(links)}")

        return {
            "graph": {
                "nodes": list(nodes.values()),
                "links": links
            }
        }

    except Exception as e:
        print("❌ Error fetching network data:", e)
        raise

def get_water_action_plan_stakeholder_network(file_name: str, action: str):
    cypher_query = """
        MATCH (f:WATER_AP_FILE)-[:WATER_AP_ACTION]->(a:WATER_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:WATER_AP_ACTION_STAKEHOLDER]->(s:WATER_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            id(f) AS id_f, f.name AS label_f, 'File Name' AS type_f, 
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a, 
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, file_name=file_name, action=action)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['f', 'a', 's']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            links.append({"source": record["id_f"], "target": record["id_a"], "type": "HAS_ACTION"})
            links.append({"source": record["id_a"], "target": record["id_s"], "type": "INVOLVES"})

        print(f"\n✅ Total nodes: {len(nodes)}, Total links: {len(links)}")

        return {
            "graph": {
                "nodes": list(nodes.values()),
                "links": links
            }
        }

    except Exception as e:
        print("❌ Error fetching network data:", e)
        raise

def get_live_action_plan_stakeholder_network(file_name: str, action: str):
    cypher_query = """
        MATCH (f:LIVE_AP_FILE)-[:LIVE_AP_ACTION]->(a:LIVE_AP_ACTION)
        WHERE f.name = $file_name AND a.name = $action
        WITH f, a
        MATCH (a)-[:LIVE_AP_ACTION_STAKEHOLDER]->(s:LIVE_AP_ACTION_STAKEHOLDER)
        RETURN DISTINCT 
            id(f) AS id_f, f.name AS label_f, 'File Name' AS type_f, 
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a, 
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, file_name=file_name, action=action)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['f', 'a', 's']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            links.append({"source": record["id_f"], "target": record["id_a"], "type": "HAS_ACTION"})
            links.append({"source": record["id_a"], "target": record["id_s"], "type": "INVOLVES"})

        print(f"\n✅ Total nodes: {len(nodes)}, Total links: {len(links)}")

        return {
            "graph": {
                "nodes": list(nodes.values()),
                "links": links
            }
        }

    except Exception as e:
        print("❌ Error fetching network data:", e)
        raise

def get_action_plan_network(query, file_name, action):
    if query == "car":
        return get_carbon_action_plan_stakeholder_network(file_name, action)
    elif query == "wat":
        return get_water_action_plan_stakeholder_network(file_name, action)
    elif query == "liv":
        return get_live_action_plan_stakeholder_network(file_name, action)
    else:
        return []