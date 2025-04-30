from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:CARBON_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:CARBON_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:CARBON_FWSTAKEHOLDER_HAS_ACTION]->(a:CARBON_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Stakeholder' AS type_stakeholder,
            id(r) AS id_recommendation, r.name AS label_recommendation, 'Recommendation' AS type_recommendation,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_recommendation, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'recommendation', 'action']:
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
                "target": record["id_recommendation"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": record["id_recommendation"],
                "target": record["id_action"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_ACTION"
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

def get_water_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:WATER_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:WATER_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:WATER_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:WATER_FWSTAKEHOLDER_HAS_ACTION]->(a:WATER_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Stakeholder' AS type_stakeholder,
            id(r) AS id_recommendation, r.name AS label_recommendation, 'Recommendation' AS type_recommendation,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_recommendation, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'recommendation', 'action']:
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
                "target": record["id_recommendation"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": record["id_recommendation"],
                "target": record["id_action"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_ACTION"
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

def get_live_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:LIVE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
            -[:LIVE_FWSTAKEHOLDER_HAS_RECOMMENDATION]->(r:LIVE_FWSTAKEHOLDER_Recommendation {stakeholder: $formalStakeholder})
            -[:LIVE_FWSTAKEHOLDER_HAS_ACTION]->(a:LIVE_FWSTAKEHOLDER_Action {stakeholder: $formalStakeholder})
        RETURN DISTINCT 
            id(s) AS id_stakeholder, s.name AS label_stakeholder, 'Stakeholder' AS type_stakeholder,
            id(r) AS id_recommendation, r.name AS label_recommendation, 'Recommendation' AS type_recommendation,
            id(a) AS id_action, a.name AS label_action, 'Action' AS type_action
        ORDER BY label_stakeholder, label_recommendation, label_action
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix in ['stakeholder', 'recommendation', 'action']:
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
                "target": record["id_recommendation"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": record["id_recommendation"],
                "target": record["id_action"],
                "type": "CARBON_FWSTAKEHOLDER_HAS_ACTION"
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
    
def get_fwstakeholder_plan_network(query, formalStakeholder):
    if query == "car":
        return get_carbon_fwstakeholder_network(formalStakeholder)
    elif query == "wat":
        return get_water_fwstakeholder_network(formalStakeholder)
    elif query == "liv":
        return get_live_fwstakeholder_network(formalStakeholder)
    else:
        return []