from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:CARBON_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:CARBON_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:CARBON_LONE_FWSTAKEHOLDER_Action {name: $action})
        MATCH (a)-[:CARBON_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s:CARBON_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Recommendation
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],  # label uses short version, fallback to full
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add nodes for Action
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add nodes for Stakeholder
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add edges
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "HAS_ACTION"
            })
            links.append({
                "source": record["id_s"],
                "target": record["id_a"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_water_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:WATER_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:WATER_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:WATER_LONE_FWSTAKEHOLDER_Action {name: $action})
        MATCH (a)-[:WATER_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s:WATER_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Recommendation
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],  # label uses short version, fallback to full
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add nodes for Action
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add nodes for Stakeholder
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add edges
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "HAS_ACTION"
            })
            links.append({
                "source": record["id_s"],
                "target": record["id_a"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_live_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:LIVE_LONE_FWSTAKEHOLDER_Recommendation {name: $recommendation})
            -[:LIVE_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a:LIVE_LONE_FWSTAKEHOLDER_Action {name: $action})
        MATCH (a)-[:LIVE_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s:LIVE_LONE_FWSTAKEHOLDER_Stakeholder)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Recommendation
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],  # label uses short version, fallback to full
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add nodes for Action
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add nodes for Stakeholder
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add edges
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "HAS_ACTION"
            })
            links.append({
                "source": record["id_s"],
                "target": record["id_a"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_carbon2_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:CARBON_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
              -[:CARBON_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
              (a:CARBON_LTWO_FWSTAKEHOLDER_Action {name: $action})
              -[:CARBON_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
              (s:CARBON_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add Recommendation node
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add Action node
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add Stakeholder/Label node
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add relationships
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "RECOMMENDATION_HAS_ACTION"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_s"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_water2_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:WATER_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
              -[:WATER_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
              (a:WATER_LTWO_FWSTAKEHOLDER_Action {name: $action})
              -[:WATER_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
              (s:WATER_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add Recommendation node
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add Action node
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add Stakeholder/Label node
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add relationships
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "RECOMMENDATION_HAS_ACTION"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_s"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_live2_fw_network(recommendation: str, action: str):
    cypher_query = """
        MATCH (r:LIVE_LTWO_FWSTAKEHOLDER_Recommendation {name: $recommendation})
              -[:LIVE_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->
              (a:LIVE_LTWO_FWSTAKEHOLDER_Action {name: $action})
              -[:LIVE_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->
              (s:LIVE_LTWO_FWSTAKEHOLDER_Labels)

        RETURN DISTINCT 
            id(r) AS id_r, r.shortRecommendation AS shortRecommendation, r.name AS fullRecommendation, 'Recommendation' AS type_r,
            id(a) AS id_a, a.shortAction AS shortAction, a.name AS fullAction, 'Action' AS type_a,
            id(s) AS id_s, s.name AS label_s, 'Stakeholder' AS type_s
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, recommendation=recommendation, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add Recommendation node
            if record["id_r"] not in nodes:
                nodes[record["id_r"]] = {
                    "id": record["id_r"],
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "tooltip": record["fullRecommendation"],
                    "type": record["type_r"]
                }
            # Add Action node
            if record["id_a"] not in nodes:
                nodes[record["id_a"]] = {
                    "id": record["id_a"],
                    "label": record["shortAction"] or record["fullAction"],
                    "tooltip": record["fullAction"],
                    "type": record["type_a"]
                }
            # Add Stakeholder/Label node
            if record["id_s"] not in nodes:
                nodes[record["id_s"]] = {
                    "id": record["id_s"],
                    "label": record["label_s"],
                    "tooltip": record["label_s"],
                    "type": record["type_s"]
                }

            # Add relationships
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "RECOMMENDATION_HAS_ACTION"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_s"],
                "type": "ACTION_ASSIGNED_TO"
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

def get_fw_network(query, recommendation, action, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fw_network(recommendation, action)
    elif query == "wat" and access == 'levelone':
        return get_water_fw_network(recommendation, action)
    elif query == "liv" and access == 'levelone':
        return get_live_fw_network(recommendation, action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fw_network(recommendation, action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fw_network(recommendation, action)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fw_network(recommendation, action)
    else:
        return []