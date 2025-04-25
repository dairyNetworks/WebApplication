from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"  # Replace with your Neo4j password
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_carbon_sentiment(category, sentiment):
    query = """
        MATCH (carbon:CARBON_SENTIMENT_Topic {name: 'carbon'})
            -[:CARBON_SENTIMENT_HAS_LABEL]->(label:CARBON_SENTIMENT_Label)
        MATCH (label)-[:CARBON_SENTIMENT_HAS_THOUGHT]->(thought:CARBON_SENTIMENT_Thought)
        MATCH (thought)-[:CARBON_SENTIMENT_HAS_SENTIMENT]->(sentiment:CARBON_SENTIMENT_Sentiment)
        MATCH (label)-[:CARBON_SENTIMENT_HAS_CATEGORY]->(category:CARBON_SENTIMENT_Category)
        WHERE category.name = $category AND sentiment.type = $sentiment
        RETURN DISTINCT
            label.name AS Label,
            thought.text AS Thought
    """
    
    with driver.session() as session:
        results = session.run(query, category = category, sentiment = sentiment)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "Thought": record["Thought"]
            })
        return table


def get_water_sentiment(category, sentiment):
    query = """
        MATCH (WATER:WATER_SENTIMENT_Topic {name: 'water'})
            -[:WATER_SENTIMENT_HAS_LABEL]->(label:WATER_SENTIMENT_Label)
        MATCH (label)-[:WATER_SENTIMENT_HAS_THOUGHT]->(thought:WATER_SENTIMENT_Thought)
        MATCH (thought)-[:WATER_SENTIMENT_HAS_SENTIMENT]->(sentiment:WATER_SENTIMENT_Sentiment)
        MATCH (label)-[:WATER_SENTIMENT_HAS_CATEGORY]->(category:WATER_SENTIMENT_Category)
        WHERE category.name = $category AND sentiment.type = $sentiment
        RETURN DISTINCT
            label.name AS Label,
            thought.text AS Thought
    """
    
    with driver.session() as session:
        results = session.run(query, category = category, sentiment = sentiment)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "Thought": record["Thought"]
            })
        return table


def get_live_sentiment(category, sentiment):
    query = """
        MATCH (LIVE:LIVE_SENTIMENT_Topic {name: 'live'})
            -[:LIVE_SENTIMENT_HAS_LABEL]->(label:LIVE_SENTIMENT_Label)
        MATCH (label)-[:LIVE_SENTIMENT_HAS_THOUGHT]->(thought:LIVE_SENTIMENT_Thought)
        MATCH (thought)-[:LIVE_SENTIMENT_HAS_SENTIMENT]->(sentiment:LIVE_SENTIMENT_Sentiment)
        MATCH (label)-[:LIVE_SENTIMENT_HAS_CATEGORY]->(category:LIVE_SENTIMENT_Category)
        WHERE category.name = $category AND sentiment.type = $sentiment
        RETURN DISTINCT
            label.name AS Label,
            thought.text AS Thought
    """
    
    with driver.session() as session:
        results = session.run(query, category = category, sentiment = sentiment)
        table = []
        for record in results:
            table.append({
                "Label": record["Label"],
                "Thought": record["Thought"]
            })
        return table

def get_sentiment(query, category, sentiment):
    if query == "car":
        return get_carbon_sentiment(category, sentiment)
    elif query == "wat":
        return get_water_sentiment(category, sentiment)
    elif query == "liv":
        return get_live_sentiment(category, sentiment)
    else:
        return []