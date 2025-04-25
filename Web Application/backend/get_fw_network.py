from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_fw_network(identifier: str):
    cypher_query = """
        MATCH (i:CARBON_FW_IDENTIFIER {name: $identifier})
        MATCH (a:CARBON_FW_ACTION)-[:CARBON_FW_LINKED_TO]->(i)
        MATCH (r:CARBON_FW_RECOMMENDATION)-[:CARBON_FW_RECOMMENDS]->(a)
        MATCH (a)-[:CARBON_FW_INVOLVES]->(fs:CARBON_FW_Formal_Stakeholder)
        RETURN DISTINCT
            id(i) AS id_i, i.name AS label_i, 'Identifier' AS type_i,
            id(r) AS id_r, r.name AS label_r, 'Recommendation' AS type_r,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
    """
    session = driver.session()
    try:
        results = session.run(cypher_query, identifier=identifier)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['i', 'r', 'a','fs']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Add links based on the structure
            links.append({
                "source": record["id_i"],
                "target": record["id_r"],
                "type": "RECOMMENDS"
            })
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "ACTS_ON"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_fs"],
                "type": "INVOLVES"
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

def get_water_fw_network(identifier: str):
    cypher_query = """
        MATCH (i:WATER_FW_IDENTIFIER {name: $identifier})
        MATCH (a:WATER_FW_ACTION)-[:WATER_FW_LINKED_TO]->(i)
        MATCH (r:WATER_FW_RECOMMENDATION)-[:WATER_FW_RECOMMENDS]->(a)
        MATCH (a)-[:WATER_FW_INVOLVES]->(fs:WATER_FW_Formal_Stakeholder)
        RETURN DISTINCT
            id(i) AS id_i, i.name AS label_i, 'Identifier' AS type_i,
            id(r) AS id_r, r.name AS label_r, 'Recommendation' AS type_r,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, identifier=identifier)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['i', 'r', 'a', 'fs']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Add links based on the structure
            links.append({
                "source": record["id_i"],
                "target": record["id_r"],
                "type": "RECOMMENDS"
            })
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "ACTS_ON"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_fs"],
                "type": "INVOLVES"
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

def get_live_fw_network(identifier: str):
    cypher_query = """
        MATCH (i:LIVE_FW_IDENTIFIER {name: $identifier})
        MATCH (a:LIVE_FW_ACTION)-[:LIVE_FW_LINKED_TO]->(i)
        MATCH (r:LIVE_FW_RECOMMENDATION)-[:LIVE_FW_RECOMMENDS]->(a)
        MATCH (a)-[:LIVE_FW_INVOLVES]->(fs:LIVE_FW_Formal_Stakeholder)
        RETURN DISTINCT
            id(i) AS id_i, i.name AS label_i, 'Identifier' AS type_i,
            id(r) AS id_r, r.name AS label_r, 'Recommendation' AS type_r,
            id(a) AS id_a, a.name AS label_a, 'Action' AS type_a,
            id(fs) AS id_fs, fs.name AS label_fs, 'Formal Stakeholder' AS type_fs
    """

    session = driver.session()
    try:
        results = session.run(cypher_query, identifier=identifier)

        nodes = {}
        links = []

        for record in results:
            for prefix in ['i', 'r', 'a', 'fs']:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Add links based on the structure
            links.append({
                "source": record["id_i"],
                "target": record["id_r"],
                "type": "RECOMMENDS"
            })
            links.append({
                "source": record["id_r"],
                "target": record["id_a"],
                "type": "ACTS_ON"
            })
            links.append({
                "source": record["id_a"],
                "target": record["id_fs"],
                "type": "INVOLVES"
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

def get_fw_network(query, identifier):
    if query == "car":
        return get_carbon_fw_network(identifier)
    elif query == "wat":
        return get_water_fw_network(identifier)
    elif query == "liv":
        return get_live_fw_network(identifier)
    else:
        return []