from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:CARBON_FVSTAKEHOLDER_HAS_MISSION]->(m:CARBON_FVSTAKEHOLDER_Mission {stakeholder: $formalStakeholder})
            -[:CARBON_FVSTAKEHOLDER_HAS_GOAL]->(g:CARBON_FVSTAKEHOLDER_Goal {stakeholder: $formalStakeholder})
            -[:CARBON_FVSTAKEHOLDER_HAS_ACTION]->(a:CARBON_FVSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
            id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_mission, label_goal, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'mission', 'goal', 'action']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links
            links.append({
                "source": record["id_stakeholder"],
                "target": record["id_mission"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_MISSION"
            })
            links.append({
                "source": record["id_mission"],
                "target": record["id_goal"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_GOAL"
            })
            links.append({
                "source": record["id_goal"],
                "target": record["id_action"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_ACTION"
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


def get_water_fvstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:WATER_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:WATER_FVSTAKEHOLDER_HAS_MISSION]->(m:WATER_FVSTAKEHOLDER_Mission {stakeholder: $formalStakeholder})
            -[:WATER_FVSTAKEHOLDER_HAS_GOAL]->(g:WATER_FVSTAKEHOLDER_Goal {stakeholder: $formalStakeholder})
            -[:WATER_FVSTAKEHOLDER_HAS_ACTION]->(a:WATER_FVSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
            id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_mission, label_goal, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'mission', 'goal', 'action']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links
            links.append({
                "source": record["id_stakeholder"],
                "target": record["id_mission"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_MISSION"
            })
            links.append({
                "source": record["id_mission"],
                "target": record["id_goal"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_GOAL"
            })
            links.append({
                "source": record["id_goal"],
                "target": record["id_action"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_ACTION"
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

def get_live_fvstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:LIVE_FVSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:LIVE_FVSTAKEHOLDER_HAS_MISSION]->(m:LIVE_FVSTAKEHOLDER_Mission {stakeholder: $formalStakeholder})
            -[:LIVE_FVSTAKEHOLDER_HAS_GOAL]->(g:LIVE_FVSTAKEHOLDER_Goal {stakeholder: $formalStakeholder})
            -[:LIVE_FVSTAKEHOLDER_HAS_ACTION]->(a:LIVE_FVSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Formal Stakeholder' AS type_stakeholder,
            id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
            id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_mission, label_goal, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'mission', 'goal', 'action']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links
            links.append({
                "source": record["id_stakeholder"],
                "target": record["id_mission"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_MISSION"
            })
            links.append({
                "source": record["id_mission"],
                "target": record["id_goal"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_GOAL"
            })
            links.append({
                "source": record["id_goal"],
                "target": record["id_action"],
                "type": "CARBON_FVSTAKEHOLDER_HAS_ACTION"
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

def get_fvstakeholder_network(query, formalStakeholder):
    if query == "car":
        return get_carbon_fvstakeholder_network(formalStakeholder)
    elif query == "wat":
        return get_water_fvstakeholder_network(formalStakeholder)
    elif query == "liv":
        return get_live_fvstakeholder_network(formalStakeholder)
    else:
        return []