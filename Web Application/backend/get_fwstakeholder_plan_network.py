from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:CARBON_LONE_FWSTAKEHOLDER_Action)-[:CARBON_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:CARBON_LONE_FWSTAKEHOLDER_Recommendation)-[:CARBON_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }
            
            # Add Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }
            
            # Add Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }
            
            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "CARBON_LONE_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "CARBON_LONE_FWSTAKEHOLDER_HAS_ACTION"
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
        MATCH (s:WATER_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:WATER_LONE_FWSTAKEHOLDER_Action)-[:WATER_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:WATER_LONE_FWSTAKEHOLDER_Recommendation)-[:WATER_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }
            
            # Add Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }
            
            # Add Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }
            
            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "WATER_LONE_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "WATER_LONE_FWSTAKEHOLDER_HAS_ACTION"
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
        MATCH (s:LIVE_LONE_FWSTAKEHOLDER_Stakeholder {name: $formalStakeholder})
        MATCH (a:LIVE_LONE_FWSTAKEHOLDER_Action)-[:LIVE_LONE_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:LIVE_LONE_FWSTAKEHOLDER_Recommendation)-[:LIVE_LONE_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Add Stakeholder node
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }
            
            # Add Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }
            
            # Add Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }
            
            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "LIVE_LONE_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "LIVE_LONE_FWSTAKEHOLDER_HAS_ACTION"
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
def get_carbon2_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:CARBON_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:CARBON_LTWO_FWSTAKEHOLDER_Action)-[:CARBON_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:CARBON_LTWO_FWSTAKEHOLDER_Recommendation)-[:CARBON_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Stakeholder node (Label)
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }

            # Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "CARBON_LTWO_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "CARBON_LTWO_FWSTAKEHOLDER_HAS_ACTION"
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
def get_water2_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:WATER_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:WATER_LTWO_FWSTAKEHOLDER_Action)-[:WATER_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:WATER_LTWO_FWSTAKEHOLDER_Recommendation)-[:WATER_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Stakeholder node (Label)
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }

            # Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "WATER_LTWO_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "WATER_LTWO_FWSTAKEHOLDER_HAS_ACTION"
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

def get_live2_fwstakeholder_network(formalStakeholder: str):
    cypher_query = """
        MATCH (s:LIVE_LTWO_FWSTAKEHOLDER_Labels {name: $formalStakeholder})
        MATCH (a:LIVE_LTWO_FWSTAKEHOLDER_Action)-[:LIVE_LTWO_FWSTAKEHOLDER_ACTION_ASSIGNED_TO]->(s)
        MATCH (r:LIVE_LTWO_FWSTAKEHOLDER_Recommendation)-[:LIVE_LTWO_FWSTAKEHOLDER_RECOMMENDATION_HAS_ACTION]->(a)
        RETURN DISTINCT 
            id(s) AS id_stakeholder, 
            s.name AS label_stakeholder, 
            'Stakeholder' AS type_stakeholder,

            id(r) AS id_recommendation, 
            r.name AS fullRecommendation, 
            r.shortRecommendation AS shortRecommendation, 
            'Recommendation' AS type_recommendation,

            id(a) AS id_action, 
            a.name AS fullAction, 
            a.shortAction AS shortAction,
            'Action' AS type_action
        ORDER BY label_stakeholder, fullRecommendation, fullAction
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, formalStakeholder=formalStakeholder)

        nodes = {}
        links = []

        for record in results:
            # Stakeholder node (Label)
            s_id = record["id_stakeholder"]
            if s_id not in nodes:
                nodes[s_id] = {
                    "id": s_id,
                    "label": record["label_stakeholder"],
                    "fullLabel": record["label_stakeholder"],
                    "type": record["type_stakeholder"]
                }

            # Recommendation node
            r_id = record["id_recommendation"]
            if r_id not in nodes:
                nodes[r_id] = {
                    "id": r_id,
                    "label": record["shortRecommendation"] or record["fullRecommendation"],
                    "fullLabel": record["fullRecommendation"],
                    "type": record["type_recommendation"]
                }

            # Action node
            a_id = record["id_action"]
            if a_id not in nodes:
                nodes[a_id] = {
                    "id": a_id,
                    "label": record["shortAction"] or record["fullAction"],
                    "fullLabel": record["fullAction"],
                    "type": record["type_action"]
                }

            # Add links
            links.append({
                "source": s_id,
                "target": r_id,
                "type": "LIVE_LTWO_FWSTAKEHOLDER_HAS_RECOMMENDATION"
            })
            links.append({
                "source": r_id,
                "target": a_id,
                "type": "LIVE_LTWO_FWSTAKEHOLDER_HAS_ACTION"
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

def get_fwstakeholder_plan_network(query, formalStakeholder, access):
    if query == "car" and access == 'levelone':
        return get_carbon_fwstakeholder_network(formalStakeholder)
    elif query == "wat" and access == 'levelone':
        return get_water_fwstakeholder_network(formalStakeholder)
    elif query == "liv" and access == 'levelone':
        return get_live_fwstakeholder_network(formalStakeholder)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fwstakeholder_network(formalStakeholder)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fwstakeholder_network(formalStakeholder)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fwstakeholder_network(formalStakeholder)
    else:
        return []