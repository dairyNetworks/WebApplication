from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
              -[:CARBON_AP_LONE_HAS_CATEGORY]->(c:CARBON_AP_LONE_CATEGORY),
              (s)<-[:CARBON_AP_LONE_HAS_STAKEHOLDER]-(a:CARBON_AP_LONE_ACTION)
              <-[:CARBON_AP_LONE_HAS_ACTION]-(f:CARBON_AP_LONE_FILE)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, a.shortAction AS short_action_text, 'Action' AS type_action,
            id(c) AS id_category, c.name AS label_category, 'Category' AS type_category
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['stakeholder', 'file', 'action', 'category']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    # Use short label and tooltip for action node
                    if prefix == "action":
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record["short_action_text"],   # corrected key name
                            "action": record["label_action"],       # full text for tooltip
                            "type": "Short Action"
                        }
                    else:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record[f"label_{prefix}"],
                            "type": record[f"type_{prefix}"]
                        }

            links.extend([
                {"source": record["id_file"], "target": record["id_action"], "type": "CARBON_AP_LONE_HAS_ACTION"},
                {"source": record["id_action"], "target": record["id_stakeholder"], "type": "CARBON_AP_LONE_HAS_STAKEHOLDER"},
                {"source": record["id_stakeholder"], "target": record["id_category"], "type": "CARBON_AP_LONE_HAS_CATEGORY"},
            ])

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
        MATCH (s:WATER_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
              -[:WATER_AP_LONE_HAS_CATEGORY]->(c:WATER_AP_LONE_CATEGORY),
              (s)<-[:WATER_AP_LONE_HAS_STAKEHOLDER]-(a:WATER_AP_LONE_ACTION)
              <-[:WATER_AP_LONE_HAS_ACTION]-(f:WATER_AP_LONE_FILE)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, a.shortAction AS short_action_text, 'Action' AS type_action,
            id(c) AS id_category, c.name AS label_category, 'Category' AS type_category
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['stakeholder', 'file', 'action', 'category']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    # Use short label and tooltip for action node
                    if prefix == "action":
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record["short_action_text"],   # corrected key name
                            "action": record["label_action"],       # full text for tooltip
                            "type": "Short Action"
                        }
                    else:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record[f"label_{prefix}"],
                            "type": record[f"type_{prefix}"]
                        }

            links.extend([
                {"source": record["id_file"], "target": record["id_action"], "type": "WATER_AP_LONE_HAS_ACTION"},
                {"source": record["id_action"], "target": record["id_stakeholder"], "type": "WATER_AP_LONE_HAS_STAKEHOLDER"},
                {"source": record["id_stakeholder"], "target": record["id_category"], "type": "WATER_AP_LONE_HAS_CATEGORY"},
            ])

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
        MATCH (s:LIVE_AP_LONE_STAKEHOLDERS {name: $formalStakeholder})
              -[:LIVE_AP_LONE_HAS_CATEGORY]->(c:LIVE_AP_LONE_CATEGORY),
              (s)<-[:LIVE_AP_LONE_HAS_STAKEHOLDER]-(a:LIVE_AP_LONE_ACTION)
              <-[:LIVE_AP_LONE_HAS_ACTION]-(f:LIVE_AP_LONE_FILE)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(f) AS id_file, f.name AS label_file, 'File Name' AS type_file,
            id(a) AS id_action, a.name AS label_action, a.shortAction AS short_action_text, 'Action' AS type_action,
            id(c) AS id_category, c.name AS label_category, 'Category' AS type_category
        ORDER BY label_stakeholder, label_file, label_action
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['stakeholder', 'file', 'action', 'category']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    # Use short label and tooltip for action node
                    if prefix == "action":
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record["short_action_text"],   # corrected key name
                            "action": record["label_action"],       # full text for tooltip
                            "type": "Short Action"
                        }
                    else:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": record[f"label_{prefix}"],
                            "type": record[f"type_{prefix}"]
                        }

            links.extend([
                {"source": record["id_file"], "target": record["id_action"], "type": "LIVE_AP_LONE_HAS_ACTION"},
                {"source": record["id_action"], "target": record["id_stakeholder"], "type": "LIVE_AP_LONE_HAS_STAKEHOLDER"},
                {"source": record["id_stakeholder"], "target": record["id_category"], "type": "LIVE_AP_LONE_HAS_CATEGORY"},
            ])

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

def get_carbonl2_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (f:CARBON_AP_LTWO_FILE)-[:CARBON_AP_LTWO_HAS_ACTION]->(a:CARBON_AP_LTWO_ACTION)
        MATCH (a)-[:CARBON_AP_LTWO_HAS_LABELS]->(l:CARBON_AP_LTWO_LABELS)
        WHERE l.name = $formalStakeholder
        RETURN f.name AS fileName, a.shortAction AS shortAction, a.name AS action, collect(l.name) AS labels
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            file_name_val = record["fileName"]
            short_action_val = record["shortAction"]
            action_val = record["action"]
            labels_list = record["labels"] or []

            # Create node IDs (replace spaces with underscores for simplicity)
            file_node_id = f"file_{file_name_val.replace(' ', '_')}"
            short_action_node_id = f"shortaction_{short_action_val.replace(' ', '_')}"

            # Add File node
            if file_node_id not in nodes:
                nodes[file_node_id] = {
                    "id": file_node_id,
                    "label": file_name_val,
                    "type": "File"
                }

            # Add Short Action node
            if short_action_node_id not in nodes:
                nodes[short_action_node_id] = {
                    "id": short_action_node_id,
                    "label": short_action_val,
                    "type": "Short Action",
                    "action": action_val  # Include full Action text
                }

            # Link File -> Short Action
            links.append({
                "source": file_node_id,
                "target": short_action_node_id,
                "type": "HAS_SHORTACTION"
            })

            # Add Label nodes and link Short Action -> Label
            for label in labels_list:
                label_node_id = f"label_{label.replace(' ', '_')}"
                if label_node_id not in nodes:
                    nodes[label_node_id] = {
                        "id": label_node_id,
                        "label": label,
                        "type": "Label"
                    }
                links.append({
                    "source": short_action_node_id,
                    "target": label_node_id,
                    "type": "HAS_LABEL"
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

def get_waterl2_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (f:WATER_AP_LTWO_FILE)-[:WATER_AP_LTWO_HAS_ACTION]->(a:WATER_AP_LTWO_ACTION)
        MATCH (a)-[:WATER_AP_LTWO_HAS_LABELS]->(l:WATER_AP_LTWO_LABELS)
        WHERE l.name = $formalStakeholder
        RETURN f.name AS fileName, a.shortAction AS shortAction, a.name AS action, collect(l.name) AS labels
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            file_name_val = record["fileName"]
            short_action_val = record["shortAction"]
            action_val = record["action"]
            labels_list = record["labels"] or []

            # Create node IDs (replace spaces with underscores for simplicity)
            file_node_id = f"file_{file_name_val.replace(' ', '_')}"
            short_action_node_id = f"shortaction_{short_action_val.replace(' ', '_')}"

            # Add File node
            if file_node_id not in nodes:
                nodes[file_node_id] = {
                    "id": file_node_id,
                    "label": file_name_val,
                    "type": "File"
                }

            # Add Short Action node
            if short_action_node_id not in nodes:
                nodes[short_action_node_id] = {
                    "id": short_action_node_id,
                    "label": short_action_val,
                    "type": "Short Action",
                    "action": action_val  # Include full Action text
                }

            # Link File -> Short Action
            links.append({
                "source": file_node_id,
                "target": short_action_node_id,
                "type": "HAS_SHORTACTION"
            })

            # Add Label nodes and link Short Action -> Label
            for label in labels_list:
                label_node_id = f"label_{label.replace(' ', '_')}"
                if label_node_id not in nodes:
                    nodes[label_node_id] = {
                        "id": label_node_id,
                        "label": label,
                        "type": "Label"
                    }
                links.append({
                    "source": short_action_node_id,
                    "target": label_node_id,
                    "type": "HAS_LABEL"
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

def get_livel2_actionstakeholder_plan_stakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (f:LIVE_AP_LTWO_FILE)-[:LIVE_AP_LTWO_HAS_ACTION]->(a:LIVE_AP_LTWO_ACTION)
        MATCH (a)-[:LIVE_AP_LTWO_HAS_LABELS]->(l:LIVE_AP_LTWO_LABELS)
        WHERE l.name = $formalStakeholder
        RETURN f.name AS fileName, a.shortAction AS shortAction, a.name AS action, collect(l.name) AS labels
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            file_name_val = record["fileName"]
            short_action_val = record["shortAction"]
            action_val = record["action"]
            labels_list = record["labels"] or []

            # Create node IDs (replace spaces with underscores for simplicity)
            file_node_id = f"file_{file_name_val.replace(' ', '_')}"
            short_action_node_id = f"shortaction_{short_action_val.replace(' ', '_')}"

            # Add File node
            if file_node_id not in nodes:
                nodes[file_node_id] = {
                    "id": file_node_id,
                    "label": file_name_val,
                    "type": "File"
                }

            # Add Short Action node
            if short_action_node_id not in nodes:
                nodes[short_action_node_id] = {
                    "id": short_action_node_id,
                    "label": short_action_val,
                    "type": "Short Action",
                    "action": action_val  # Include full Action text
                }

            # Link File -> Short Action
            links.append({
                "source": file_node_id,
                "target": short_action_node_id,
                "type": "HAS_SHORTACTION"
            })

            # Add Label nodes and link Short Action -> Label
            for label in labels_list:
                label_node_id = f"label_{label.replace(' ', '_')}"
                if label_node_id not in nodes:
                    nodes[label_node_id] = {
                        "id": label_node_id,
                        "label": label,
                        "type": "Label"
                    }
                links.append({
                    "source": short_action_node_id,
                    "target": label_node_id,
                    "type": "HAS_LABEL"
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

def get_actionstakeholder_plan_network(query, formalStakeholder,access):
    if query == "car" and access == 'levelone':
        return get_carbon_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "wat" and access == 'levelone':
        return get_water_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "liv" and access == 'levelone':
        return get_live_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "car" and access == 'leveltwo':
        return get_carbonl2_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "wat" and access == 'leveltwo':
        return get_waterl2_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    elif query == "liv" and access == 'leveltwo':
        return get_livel2_actionstakeholder_plan_stakeholder_network(formalStakeholder)
    else:
        return []