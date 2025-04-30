from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:CARBON_ACTIONBYSTAKE_HAS_FILE]->(f:CARBON_ACTIONBYSTAKE_File)
            -[:CARBON_ACTIONBYSTAKE_HAS_ACTION]->(a:CARBON_ACTIONBYSTAKE_Action)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            stakeholder_id = record["id_stakeholder"]
            if stakeholder_id not in nodes:
                nodes[stakeholder_id] = {
                    "id": stakeholder_id,
                    "label": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Add File node
            file_id = record["id_file"]
            if file_id not in nodes:
                nodes[file_id] = {
                    "id": file_id,
                    "label": record["label_file"],
                    "type": record["type_file"]
                }

            # Add Action node
            action_id = record["id_action"]
            if action_id not in nodes:
                nodes[action_id] = {
                    "id": action_id,
                    "label": record["label_action"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": stakeholder_id,
                "target": file_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_FILE"
            })
            links.append({
                "source": file_id,
                "target": action_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_ACTION"
            })

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


def get_water_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:WATER_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:WATER_ACTIONBYSTAKE_HAS_FILE]->(f:WATER_ACTIONBYSTAKE_File)
            -[:WATER_ACTIONBYSTAKE_HAS_ACTION]->(a:WATER_ACTIONBYSTAKE_Action)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            stakeholder_id = record["id_stakeholder"]
            if stakeholder_id not in nodes:
                nodes[stakeholder_id] = {
                    "id": stakeholder_id,
                    "label": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Add File node
            file_id = record["id_file"]
            if file_id not in nodes:
                nodes[file_id] = {
                    "id": file_id,
                    "label": record["label_file"],
                    "type": record["type_file"]
                }

            # Add Action node
            action_id = record["id_action"]
            if action_id not in nodes:
                nodes[action_id] = {
                    "id": action_id,
                    "label": record["label_action"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": stakeholder_id,
                "target": file_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_FILE"
            })
            links.append({
                "source": file_id,
                "target": action_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_ACTION"
            })

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

def get_live_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:LIVE_ACTIONBYSTAKE_Stakeholder {name: $formalStakeholder})
            -[:LIVE_ACTIONBYSTAKE_HAS_FILE]->(f:LIVE_ACTIONBYSTAKE_File)
            -[:LIVE_ACTIONBYSTAKE_HAS_ACTION]->(a:LIVE_ACTIONBYSTAKE_Action)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            stakeholder_id = record["id_stakeholder"]
            if stakeholder_id not in nodes:
                nodes[stakeholder_id] = {
                    "id": stakeholder_id,
                    "label": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Add File node
            file_id = record["id_file"]
            if file_id not in nodes:
                nodes[file_id] = {
                    "id": file_id,
                    "label": record["label_file"],
                    "type": record["type_file"]
                }

            # Add Action node
            action_id = record["id_action"]
            if action_id not in nodes:
                nodes[action_id] = {
                    "id": action_id,
                    "label": record["label_action"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": stakeholder_id,
                "target": file_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_FILE"
            })
            links.append({
                "source": file_id,
                "target": action_id,
                "type": "CARBON_ACTIONBYSTAKE_HAS_ACTION"
            })

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

def get_actionstakeholder_plan_network(query, formalStakeholder):
    if query == "car":
        return get_carbon_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "wat":
        return get_water_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "liv":
        return get_live_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    else:
        return []