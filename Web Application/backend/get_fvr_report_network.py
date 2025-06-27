from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:CARBON_FVR_LONE_ACTION {name: $action})
        MATCH (g:CARBON_FVR_LONE_GOAL)-[:CARBON_FVR_LONE_GOALACTION_LINK]->(a)
        MATCH (m:CARBON_FVR_LONE_MISSION)-[:CARBON_FVR_LONE_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:CARBON_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:CARBON_FVR_LONE_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:CARBON_FVR_LONE_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:CARBON_FVR_LONE_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:CARBON_FVR_LONE_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_water_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:WATER_FVR_LONE_ACTION {name: $action})
        MATCH (g:WATER_FVR_LONE_GOAL)-[:WATER_FVR_LONE_GOALACTION_LINK]->(a)
        MATCH (m:WATER_FVR_LONE_MISSION)-[:WATER_FVR_LONE_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:WATER_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:WATER_FVR_LONE_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:WATER_FVR_LONE_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:WATER_FVR_LONE_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:WATER_FVR_LONE_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_live_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:LIVE_FVR_LONE_ACTION {name: $action})
        MATCH (g:LIVE_FVR_LONE_GOAL)-[:LIVE_FVR_LONE_GOALACTION_LINK]->(a)
        MATCH (m:LIVE_FVR_LONE_MISSION)-[:LIVE_FVR_LONE_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:LIVE_FVR_LONE_ACTION_PROGRAMME_LINK]->(p:LIVE_FVR_LONE_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:LIVE_FVR_LONE_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:LIVE_FVR_LONE_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:LIVE_FVR_LONE_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_carbon2_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:CARBON_FVR_LTWO_ACTION {name: $action})
        MATCH (g:CARBON_FVR_LTWO_GOAL)-[:CARBON_FVR_LTWO_GOALACTION_LINK]->(a)
        MATCH (m:CARBON_FVR_LTWO_MISSION)-[:CARBON_FVR_LTWO_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:CARBON_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:CARBON_FVR_LTWO_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:CARBON_FVR_LTWO_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:CARBON_FVR_LTWO_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:CARBON_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_water2_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:WATER_FVR_LTWO_ACTION {name: $action})
        MATCH (g:WATER_FVR_LTWO_GOAL)-[:WATER_FVR_LTWO_GOALACTION_LINK]->(a)
        MATCH (m:WATER_FVR_LTWO_MISSION)-[:WATER_FVR_LTWO_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:WATER_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:WATER_FVR_LTWO_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:WATER_FVR_LTWO_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:WATER_FVR_LTWO_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:WATER_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_live2_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (a:LIVE_FVR_LTWO_ACTION {name: $action})
        MATCH (g:LIVE_FVR_LTWO_GOAL)-[:LIVE_FVR_LTWO_GOALACTION_LINK]->(a)
        MATCH (m:LIVE_FVR_LTWO_MISSION)-[:LIVE_FVR_LTWO_MISSIONGOAL_LINK]->(g)
        MATCH (a)-[:LIVE_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p:LIVE_FVR_LTWO_PROGRAMME)

        RETURN DISTINCT
        id(m) AS id_mission, m.name AS label_mission, 'Mission' AS type_mission,
        id(g) AS id_goal, g.name AS label_goal, 'Goal' AS type_goal,
        id(a) AS id_action, a.name AS label_action, 'Action' AS type_action,
        id(p) AS id_programme, p.name AS label_programme, 'Programme' AS type_programme,

        [(m)-[:LIVE_FVR_LTWO_MISSIONGOAL_LINK]->(g) | {source:id(m), target:id(g), type: 'MISSION_GOAL'}][0] AS rel_mission_goal,
        [(g)-[:LIVE_FVR_LTWO_GOALACTION_LINK]->(a) | {source:id(g), target:id(a), type: 'GOAL_ACTION'}][0] AS rel_goal_action,
        [(a)-[:LIVE_FVR_LTWO_ACTION_PROGRAMME_LINK]->(p) | {source:id(a), target:id(p), type: 'ACTION_PROGRAMME'}][0] AS rel_action_programme
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme
            for prefix in ['mission', 'goal', 'action', 'programme']:
                node_id = record[f"id_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": record[f"label_{prefix}"],
                        "type": record[f"type_{prefix}"]
                    }

            # Add links from relationships if present
            for rel_key in ['rel_mission_goal', 'rel_goal_action', 'rel_action_programme']:
                rel = record.get(rel_key)
                if rel:
                    links.append({
                        "source": rel['source'],
                        "target": rel['target'],
                        "type": rel['type']
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

def get_fvr_report_network(query, action,access):
    if query == "car" and access == 'levelone':
        return get_carbon_fvr_report_stakeholder_network(action)
    elif query == "wat" and access == 'levelone':
        return get_water_fvr_report_stakeholder_network(action)
    elif query == "liv" and access == 'levelone':
        return get_live_fvr_report_stakeholder_network(action)
    elif query == "car" and access == 'leveltwo':
        return get_carbon2_fvr_report_stakeholder_network(action)
    elif query == "wat" and access == 'leveltwo':
        return get_water2_fvr_report_stakeholder_network(action)
    elif query == "liv" and access == 'leveltwo':
        return get_live2_fvr_report_stakeholder_network(action)
    else:
        return []