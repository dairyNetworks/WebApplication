from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fv_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:CARBON_FVNR_MISSION)-[:CARBON_FVNR_MISSIONGOAL_LINK]->(g:CARBON_FVNR_GOAL)-[:CARBON_FVNR_GOALACTION_LINK]->(a:CARBON_FVNR_ACTION {name: $action})
        MATCH (a)-[:CARBON_FVNR_ACTION_STAKE_LINK]->(stakeholder:CARBON_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(stakeholder) AS id_s, stakeholder.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Stakeholder
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('s', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links between Mission -> Goal -> Action -> Stakeholder
            links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
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

def get_water_fv_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:WATER_FVNR_MISSION)-[:WATER_FVNR_MISSIONGOAL_LINK]->(g:WATER_FVNR_GOAL)-[:WATER_FVNR_GOALACTION_LINK]->(a:WATER_FVNR_ACTION {name: $action})
        MATCH (a)-[:WATER_FVNR_ACTION_STAKE_LINK]->(stakeholder:WATER_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(stakeholder) AS id_s, stakeholder.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Stakeholder
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('s', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links between Mission -> Goal -> Action -> Stakeholder
            links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
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


def get_live_fv_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:LIVE_FVNR_MISSION)-[:LIVE_FVNR_MISSIONGOAL_LINK]->(g:LIVE_FVNR_GOAL)-[:LIVE_FVNR_GOALACTION_LINK]->(a:LIVE_FVNR_ACTION {name: $action})
        MATCH (a)-[:LIVE_FVNR_ACTION_STAKE_LINK]->(stakeholder:LIVE_FVNR_Formal_Stakeholder)
        WHERE stakeholder.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(stakeholder) AS id_s, stakeholder.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Stakeholder
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('s', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links between Mission -> Goal -> Action -> Stakeholder
            links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
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

def get_fv_network(query, action):
    if query == "car":
        return get_carbon_fv_stakeholder_network(action)
    elif query == "wat":
        return get_water_fv_stakeholder_network(action)
    elif query == "liv":
        return get_live_fv_stakeholder_network(action)
    else:
        return []