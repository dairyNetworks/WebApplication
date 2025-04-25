from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fvr_report_stakeholder_network(action: str):
    cypher_query = """
        MATCH (m:CARBON_FVR_MISSION)
        MATCH (m)-[:CARBON_FVR_MISSION_LINK]->(ms:CARBON_FVR_MISSION_STATEMENT)
        MATCH (g:CARBON_FVR_GOAL)
        MATCH (g)-[:CARBON_FVR_GOAL_LINK]->(gs:CARBON_FVR_GOAL_STATEMENT)
        MATCH (a:CARBON_FVR_ACTION)
        WHERE a.name = $action
        MATCH (a)-[:CARBON_FVR_ACTION_LINK]->(as:CARBON_FVR_ACTION_STATEMENT)
        MATCH (g)-[:CARBON_FVR_GOALACTION_LINK]->(a)
        MATCH (p:CARBON_FVR_PROGRAMME)
        MATCH (a)-[:CARBON_FVR_ACTION_PROGRAMME_LINK]->(p)
        MATCH (rs:CARBON_FVR_REPORT_SUMMARY)
        MATCH (p)-[:CARBON_FVR_PROGRAMME_REPORT_LINK]->(rs)
        MATCH (fs:CARBON_FVR_Formal_Stakeholder)
        MATCH (rs)-[:CARBON_FVR_REPORT_STAKE_LINK]->(fs)
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(p) AS id_p, p.name AS label_p, 'Programme' AS type_p,
            id(rs) AS id_rs, rs.name AS label_rs, 'Report Summary' AS type_rs,
            id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
        """


    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('p', 'Programme'), ('rs', 'Report Summary'), ('fs', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            if 'id_m' in record and 'id_g' in record:
                links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            if 'id_g' in record and 'id_a' in record:
                links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
            if 'id_a' in record and 'id_p' in record:
                links.append({"source": record["id_a"], "target": record["id_p"], "type": "HAS_PROGRAMME"})
            if 'id_p' in record and 'id_rs' in record:
                links.append({"source": record["id_p"], "target": record["id_rs"], "type": "HAS_REPORT"})
            if 'id_rs' in record and 'id_fs' in record:
                links.append({"source": record["id_rs"], "target": record["id_fs"], "type": "HAS_STAKEHOLDER"})

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
        MATCH (m:WATER_FVR_MISSION)
        MATCH (m)-[:WATER_FVR_MISSION_LINK]->(ms:WATER_FVR_MISSION_STATEMENT)
        MATCH (g:WATER_FVR_GOAL)
        MATCH (g)-[:WATER_FVR_GOAL_LINK]->(gs:WATER_FVR_GOAL_STATEMENT)
        MATCH (a:WATER_FVR_ACTION)
        WHERE a.name = $action
        MATCH (a)-[:WATER_FVR_ACTION_LINK]->(as:WATER_FVR_ACTION_STATEMENT)
        MATCH (g)-[:WATER_FVR_GOALACTION_LINK]->(a)
        MATCH (p:WATER_FVR_PROGRAMME)
        MATCH (a)-[:WATER_FVR_ACTION_PROGRAMME_LINK]->(p)
        MATCH (rs:WATER_FVR_REPORT_SUMMARY)
        MATCH (p)-[:WATER_FVR_PROGRAMME_REPORT_LINK]->(rs)
        MATCH (fs:WATER_FVR_Formal_Stakeholder)
        MATCH (rs)-[:WATER_FVR_REPORT_STAKE_LINK]->(fs)
        RETURN 
                id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
                id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
                id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
                id(p) AS id_p, p.name AS label_p, 'Programme' AS type_p,
                id(rs) AS id_rs, rs.name AS label_rs, 'Report Summary' AS type_rs,
                id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
        """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme, Report Summary, and Stakeholder
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('p', 'Programme'), ('rs', 'Report Summary'), ('fs', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links between Mission -> Goal -> Action -> Programme -> Report Summary -> Stakeholder
            if 'id_m' in record and 'id_g' in record:
                links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            if 'id_g' in record and 'id_a' in record:
                links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
            if 'id_a' in record and 'id_p' in record:
                links.append({"source": record["id_a"], "target": record["id_p"], "type": "HAS_PROGRAMME"})
            if 'id_p' in record and 'id_rs' in record:
                links.append({"source": record["id_p"], "target": record["id_rs"], "type": "HAS_REPORT"})
            if 'id_rs' in record and 'id_fs' in record:
                links.append({"source": record["id_rs"], "target": record["id_fs"], "type": "HAS_STAKEHOLDER"})

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
        MATCH (m:LIVE_FVR_MISSION)
        MATCH (m)-[:LIVE_FVR_MISSION_LINK]->(ms:LIVE_FVR_MISSION_STATEMENT)
        MATCH (g:LIVE_FVR_GOAL)
        MATCH (g)-[:LIVE_FVR_GOAL_LINK]->(gs:LIVE_FVR_GOAL_STATEMENT)
        MATCH (a:LIVE_FVR_ACTION)
        WHERE a.name = $action
        MATCH (a)-[:LIVE_FVR_ACTION_LINK]->(as:LIVE_FVR_ACTION_STATEMENT)
        MATCH (g)-[:LIVE_FVR_GOALACTION_LINK]->(a)
        MATCH (p:LIVE_FVR_PROGRAMME)
        MATCH (a)-[:LIVE_FVR_ACTION_PROGRAMME_LINK]->(p)
        MATCH (rs:LIVE_FVR_REPORT_SUMMARY)
        MATCH (p)-[:LIVE_FVR_PROGRAMME_REPORT_LINK]->(rs)
        MATCH (fs:LIVE_FVR_Formal_Stakeholder)
        MATCH (rs)-[:LIVE_FVR_REPORT_STAKE_LINK]->(fs)
        RETURN DISTINCT
            id(m) AS id_m, m.name AS label_m, 'Mission' AS type_m,
            id(g) AS id_g, g.name AS label_g, 'Goal' AS type_g,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(p) AS id_p, p.name AS label_p, 'Programme' AS type_p,
            id(rs) AS id_rs, rs.name AS label_rs, 'Report Summary' AS type_rs,
            id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
        """

    session = driver.session()
    try:
        results = session.run(cypher_query, action=action)

        nodes = {}
        links = []

        for record in results:
            # Add nodes for Mission, Goal, Action, Programme, Report Summary, and Stakeholder
            for prefix, label in [('m', 'Mission'), ('g', 'Goal'), ('a', 'Action'), ('p', 'Programme'), ('rs', 'Report Summary'), ('fs', 'Stakeholder')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links between Mission -> Goal -> Action -> Programme -> Report Summary -> Stakeholder
            if 'id_m' in record and 'id_g' in record:
                links.append({"source": record["id_m"], "target": record["id_g"], "type": "HAS_GOAL"})
            if 'id_g' in record and 'id_a' in record:
                links.append({"source": record["id_g"], "target": record["id_a"], "type": "HAS_ACTION"})
            if 'id_a' in record and 'id_p' in record:
                links.append({"source": record["id_a"], "target": record["id_p"], "type": "HAS_PROGRAMME"})
            if 'id_p' in record and 'id_rs' in record:
                links.append({"source": record["id_p"], "target": record["id_rs"], "type": "HAS_REPORT"})
            if 'id_rs' in record and 'id_fs' in record:
                links.append({"source": record["id_rs"], "target": record["id_fs"], "type": "HAS_STAKEHOLDER"})

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

def get_fvr_report_network(query, action):
    if query == "car":
        return get_carbon_fvr_report_stakeholder_network(action)
    elif query == "wat":
        return get_water_fvr_report_stakeholder_network(action)
    elif query == "liv":
        return get_live_fvr_report_stakeholder_network(action)
    else:
        return []