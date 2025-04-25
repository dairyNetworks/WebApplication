from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_sentiment_network(category, sentiment):
    cypher_query = """
        MATCH (carbon:CARBON_SENTIMENT_Topic {name: 'carbon'})-[:CARBON_SENTIMENT_HAS_LABEL]->(label:CARBON_SENTIMENT_Label)
        MATCH (label)-[:CARBON_SENTIMENT_HAS_CATEGORY]->(category:CARBON_SENTIMENT_Category)
        MATCH (label)-[:CARBON_SENTIMENT_HAS_THOUGHT]->(thought:CARBON_SENTIMENT_Thought)
        MATCH (thought)-[:CARBON_SENTIMENT_HAS_SENTIMENT]->(sentiment:CARBON_SENTIMENT_Sentiment)
        WHERE category.name = $category AND sentiment.type = $sentiment

        MATCH (label)-[:CARBON_SENTIMENT_HAS_ORGANISATION]->(org:CARBON_SENTIMENT_Organisation)
        MATCH (label)-[:CARBON_SENTIMENT_HAS_DESIGNATION]->(desig:CARBON_SENTIMENT_Designation)

        RETURN DISTINCT
            id(carbon) AS id_c, carbon.name AS label_c, 'Topic' AS type_c,
            id(label) AS id_l, label.name AS label_l, 'Label' AS type_l,
            id(org) AS id_o, org.name AS label_o, 'Organisation' AS type_o,
            id(desig) AS id_d, desig.name AS label_d, 'Designation' AS type_d
    """
    
    session = driver.session()
    try:
        results = session.run(cypher_query, category=category, sentiment=sentiment)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix, label in [('c', 'Topic'), ('l', 'Label'), ('o', 'Organisation'), ('d', 'Designation')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links
            links.append({"source": record["id_c"], "target": record["id_l"], "type": "HAS_LABEL"})
            links.append({"source": record["id_l"], "target": record["id_o"], "type": "HAS_ORGANISATION"})
            links.append({"source": record["id_l"], "target": record["id_d"], "type": "HAS_DESIGNATION"})

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

def get_water_sentiment_network(category, sentiment):
    cypher_query = """
        MATCH (water:WATER_SENTIMENT_Topic {name: 'water'})-[:WATER_SENTIMENT_HAS_LABEL]->(label:WATER_SENTIMENT_Label)
        MATCH (label)-[:WATER_SENTIMENT_HAS_CATEGORY]->(category:WATER_SENTIMENT_Category)
        MATCH (label)-[:WATER_SENTIMENT_HAS_THOUGHT]->(thought:WATER_SENTIMENT_Thought)
        MATCH (thought)-[:WATER_SENTIMENT_HAS_SENTIMENT]->(sentiment:WATER_SENTIMENT_Sentiment)
        WHERE category.name = $category AND sentiment.type = $sentiment

        MATCH (label)-[:WATER_SENTIMENT_HAS_ORGANISATION]->(org:WATER_SENTIMENT_Organisation)
        MATCH (label)-[:WATER_SENTIMENT_HAS_DESIGNATION]->(desig:WATER_SENTIMENT_Designation)

        RETURN DISTINCT
            id(water) AS id_c, water.name AS label_c, 'Topic' AS type_c,
            id(label) AS id_l, label.name AS label_l, 'Label' AS type_l,
            id(org) AS id_o, org.name AS label_o, 'Organisation' AS type_o,
            id(desig) AS id_d, desig.name AS label_d, 'Designation' AS type_d
    """
    
    session = driver.session()
    try:
        results = session.run(cypher_query, category=category, sentiment=sentiment)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix, label in [('c', 'Topic'), ('l', 'Label'), ('o', 'Organisation'), ('d', 'Designation')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links
            links.append({"source": record["id_c"], "target": record["id_l"], "type": "HAS_LABEL"})
            links.append({"source": record["id_l"], "target": record["id_o"], "type": "HAS_ORGANISATION"})
            links.append({"source": record["id_l"], "target": record["id_d"], "type": "HAS_DESIGNATION"})

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

def get_live_sentiment_network(category, sentiment):
    cypher_query = """
        MATCH (live:LIVE_SENTIMENT_Topic {name: 'live'})-[:LIVE_SENTIMENT_HAS_LABEL]->(label:LIVE_SENTIMENT_Label)
        MATCH (label)-[:LIVE_SENTIMENT_HAS_CATEGORY]->(category:LIVE_SENTIMENT_Category)
        MATCH (label)-[:LIVE_SENTIMENT_HAS_THOUGHT]->(thought:LIVE_SENTIMENT_Thought)
        MATCH (thought)-[:LIVE_SENTIMENT_HAS_SENTIMENT]->(sentiment:LIVE_SENTIMENT_Sentiment)
        WHERE category.name = $category AND sentiment.type = $sentiment

        MATCH (label)-[:LIVE_SENTIMENT_HAS_ORGANISATION]->(org:LIVE_SENTIMENT_Organisation)
        MATCH (label)-[:LIVE_SENTIMENT_HAS_DESIGNATION]->(desig:LIVE_SENTIMENT_Designation)

        RETURN DISTINCT
            id(live) AS id_c, live.name AS label_c, 'Topic' AS type_c,
            id(label) AS id_l, label.name AS label_l, 'Label' AS type_l,
            id(org) AS id_o, org.name AS label_o, 'Organisation' AS type_o,
            id(desig) AS id_d, desig.name AS label_d, 'Designation' AS type_d
    """
    
    session = driver.session()
    try:
        results = session.run(cypher_query, category=category, sentiment=sentiment)

        nodes = {}
        links = []

        for record in results:
            # Add nodes
            for prefix, label in [('c', 'Topic'), ('l', 'Label'), ('o', 'Organisation'), ('d', 'Designation')]:
                node_id = record[f"id_{prefix}"]
                node_label = record[f"label_{prefix}"]
                node_type = record[f"type_{prefix}"]
                if node_id not in nodes:
                    nodes[node_id] = {
                        "id": node_id,
                        "label": node_label,
                        "type": node_type
                    }

            # Create links
            links.append({"source": record["id_c"], "target": record["id_l"], "type": "HAS_LABEL"})
            links.append({"source": record["id_l"], "target": record["id_o"], "type": "HAS_ORGANISATION"})
            links.append({"source": record["id_l"], "target": record["id_d"], "type": "HAS_DESIGNATION"})

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

def get_sentiment_network(query, category, sentiment):
    if query == "car":
        return get_carbon_sentiment_network(category, sentiment)
    elif query == "wat":
        return get_water_sentiment_network(category, sentiment)
    elif query == "liv":
        return get_live_sentiment_network(category, sentiment)
    else:
        return []