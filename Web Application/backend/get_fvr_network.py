from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:CARBON_FVRA_MISSION)-[:CARBON_FVRA_MISSION_LINK]->(ms:CARBON_FVRA_MISSION_STATEMENT)
        MATCH (m)-[:CARBON_FVRA_MISSIONGOAL_LINK]->(g:CARBON_FVRA_GOAL)-[:CARBON_FVRA_GOAL_LINK]->(gs:CARBON_FVRA_GOAL_STATEMENT)
        MATCH (g)-[:CARBON_FVRA_GOALACTION_LINK]->(a:CARBON_FVRA_ACTION {name: $action})-[:CARBON_FVRA_ACTION_LINK]->(as:CARBON_FVRA_ACTION_STATEMENT)
        MATCH (a)-[:CARBON_FVRA_ACTION_STAKE_LINK]->(s:CARBON_FVRA_Formal_Stakeholder)
        WHERE s.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(ms) AS id_ms, ms.text AS label_ms, 'Mission Statement' AS type_ms,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(gs) AS id_gs, gs.text AS label_gs, 'Goal Statement' AS type_gs,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(as) AS id_as, as.text AS label_as, 'Action Statement' AS type_as,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
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

def get_water_fvr_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:WATER_FVRA_MISSION)-[:WATER_FVRA_MISSION_LINK]->(ms:WATER_FVRA_MISSION_STATEMENT)
        MATCH (m)-[:WATER_FVRA_MISSIONGOAL_LINK]->(g:WATER_FVRA_GOAL)-[:WATER_FVRA_GOAL_LINK]->(gs:WATER_FVRA_GOAL_STATEMENT)
        MATCH (g)-[:WATER_FVRA_GOALACTION_LINK]->(a:WATER_FVRA_ACTION {name: $action})-[:WATER_FVRA_ACTION_LINK]->(as:WATER_FVRA_ACTION_STATEMENT)
        MATCH (a)-[:WATER_FVRA_ACTION_STAKE_LINK]->(s:WATER_FVRA_Formal_Stakeholder)
        WHERE s.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(ms) AS id_ms, ms.text AS label_ms, 'Mission Statement' AS type_ms,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(gs) AS id_gs, gs.text AS label_gs, 'Goal Statement' AS type_gs,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(as) AS id_as, as.text AS label_as, 'Action Statement' AS type_as,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
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


def get_live_fvr_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:LIVE_FVRA_MISSION)-[:LIVE_FVRA_MISSION_LINK]->(ms:LIVE_FVRA_MISSION_STATEMENT)
        MATCH (m)-[:LIVE_FVRA_MISSIONGOAL_LINK]->(g:LIVE_FVRA_GOAL)-[:LIVE_FVRA_GOAL_LINK]->(gs:LIVE_FVRA_GOAL_STATEMENT)
        MATCH (g)-[:LIVE_FVRA_GOALACTION_LINK]->(a:LIVE_FVRA_ACTION {name: $action})-[:LIVE_FVRA_ACTION_LINK]->(as:LIVE_FVRA_ACTION_STATEMENT)
        MATCH (a)-[:LIVE_FVRA_ACTION_STAKE_LINK]->(s:LIVE_FVRA_Formal_Stakeholder)
        WHERE s.name <> 'null'
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(ms) AS id_ms, ms.text AS label_ms, 'Mission Statement' AS type_ms,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(gs) AS id_gs, gs.text AS label_gs, 'Goal Statement' AS type_gs,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(as) AS id_as, as.text AS label_as, 'Action Statement' AS type_as,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
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

def get_fvr_network(query, action):
    if query == "car":
        return get_carbon_fvr_stakeholder_network(action)
    elif query == "wat":
        return get_water_fvr_stakeholder_network(action)
    elif query == "liv":
        return get_live_fvr_stakeholder_network(action)
    else:
        return []