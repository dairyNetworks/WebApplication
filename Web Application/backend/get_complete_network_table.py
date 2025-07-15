from fastapi import Query, Request
from fastapi.responses import JSONResponse
from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_complete_network_table(label, query):
    topic_map = {
        "car": "carbon",
        "wat": "water",
        "liv": "live"
    }
    topic_filter = topic_map.get(query.lower(), query.lower())

    cypher_query = """
    MATCH (l:UG_LABELS)
    WHERE l.name = $label OR l.norm = $label
    WITH l, $topicFilter AS topicFilter

    OPTIONAL MATCH (l)-[:UG_LABEL_HAS_ACTION_AP]->(a1:UG_AP_ACTIONS {topic: topicFilter})
    OPTIONAL MATCH (l)-[:UG_LABEL_HAS_ACTION_FW]->(a2:UG_FW_ACTIONS {topic: topicFilter})
    OPTIONAL MATCH (l)-[:UG_LABEL_ACTION_FVA]->(a4:UG_FVA_ACTION {topic: topicFilter})
    OPTIONAL MATCH (l)-[:UG_LABEL_PROGRAMME_FVR]->(p5:UG_FVR_PROGRAMME {topic: topicFilter})

    OPTIONAL MATCH (l)-[:UG_PUB_PRIM_LABEL_HAS_TAG]->(t3:UG_PUB_TAG)
    OPTIONAL MATCH (t3)-[:UG_PUB_TAG_HAS_SEC_LABEL]->(s3:UG_PUB_SEC_LABEL)
    OPTIONAL MATCH (t4:UG_PUB_SEC_TAG)-[:UG_PUB_SEC_TAG_HAS_SEC_LABEL]->(l)
    OPTIONAL MATCH (p4:UG_PUB_PRIM_LABELS)-[:UG_PUB_SEC_PRIM_LABEL_HAS_TAG]->(t4)

    OPTIONAL MATCH (l)-[:UG_SENT_LABEL_HAS_DESIGNATION]->(d5:UG_SENT_DESIGNATION)
    WHERE d5.topic = topicFilter

    RETURN DISTINCT
        a1, a2, a4, p5, t3, s3, t4, p4, d5
    """

    try:
        session = driver.session()
        results = session.run(cypher_query, parameters={"label": label, "topicFilter": topic_filter})

        # Dictionaries to avoid duplicates
        action_plans = {}
        food_wise = {}
        food_vision_action = {}
        food_vision_report = {}
        pub_tag = {}
        pub_sec_label = {}
        pub_sec_tag = {}
        pub_prim_label = {}
        designation = {}

        for record in results:
            a1 = record.get("a1")
            if a1 and a1.id not in action_plans:
                action_plans[a1.id] = {
                    "id": a1.id,
                    "shortaction": a1.get("shortaction"),
                    "source": "Action Plan",
                    "name": a1.get("name")
                }
                print(f"Added Action Plan: id={a1.id}, shortaction={a1.get('shortaction')}")

            a2 = record.get("a2")
            if a2 and a2.id not in food_wise:
                food_wise[a2.id] = {
                    "id": a2.id,
                    "shortaction": a2.get("shortaction"),
                    "source": a2.get("source"),
                    "recommendation": a2.get("shortrecommendation"),
                    "name": a2.get("name")
                }
                print(f"Added Food Wise: id={a2.id}, shortaction={a2.get('shortaction')}")

            a4 = record.get("a4")
            if a4 and a4.id not in food_vision_action:
                food_vision_action[a4.id] = {
                    "id": a4.id,
                    "name": a4.get("name"),
                    "source": a4.get("source"),
                    "mission": a4.get("mission"),
                    "goal": a4.get("goal"),
                    "actionstatement": a4.get("actionstatement")
                }
                print(f"Added Food Vision Action: id={a4.id}, name={a4.get('name')}")

            p5 = record.get("p5")
            if p5 and p5.id not in food_vision_report:
                food_vision_report[p5.id] = {
                    "id": p5.id,
                    "name": p5.get("name"),
                    "source": p5.get("source"),
                    "mission": p5.get("mission"),
                    "goal": p5.get("goal"),
                    "actionstatement": p5.get("actionstatement"),
                    "reportsummary": p5.get("reportsummary")
                }
                print(f"Added Food Vision Report: id={p5.id}, name={p5.get('name')}")

            t3 = record.get("t3")
            if t3 and t3.id not in pub_tag:
                pub_tag[t3.id] = {
                    "id": t3.id,
                    "name": t3.get("name"),
                    "source": "Publications",
                    "context": t3.get("context")
                }
                print(f"Added Publication Tag: id={t3.id}, name={t3.get('name')}")

            s3 = record.get("s3")
            if s3 and s3.id not in pub_sec_label:
                pub_sec_label[s3.id] = {
                    "id": s3.id,
                    "name": s3.get("name")
                }
                print(f"Added Publication Secondary Label: id={s3.id}, name={s3.get('name')}")

            t4 = record.get("t4")
            if t4 and t4.id not in pub_sec_tag:
                pub_sec_tag[t4.id] = {
                    "id": t4.id,
                    "name": t4.get("name"),
                    "source": "Publications",
                    "context": t4.get("context")
                }
                print(f"Added Publication Secondary Tag: id={t4.id}, name={t4.get('name')}")

            p4 = record.get("p4")
            if p4 and p4.id not in pub_prim_label:
                pub_prim_label[p4.id] = {
                    "id": p4.id,
                    "name": p4.get("name")
                }
                print(f"Added Publication Primary Label: id={p4.id}, name={p4.get('name')}")

            d5 = record.get("d5")
            if d5 and d5.id not in designation:
                designation[d5.id] = {
                    "id": d5.id,
                    "name": d5.get("name"),
                    "sentiment": d5.get("sentiment"),
                    "thought": d5.get("thought")
                }
                print(f"Added Sentiment Designation: id={d5.id}, name={d5.get('name')}")

        session.close()

        return {
            "Action_Plans": list(action_plans.values()),
            "Food_Wise": list(food_wise.values()),
            "Food_Vision_Actions": list(food_vision_action.values()),
            "Food_Vision_Reports": list(food_vision_report.values()),
            "Publication_Tags": list(pub_tag.values()),
            "Publication_Secondary_Labels": list(pub_sec_label.values()),
            "Publication_Secondary_Tags": list(pub_sec_tag.values()),
            "Publication_Primary_Labels": list(pub_prim_label.values()),
            "Sentiment_Designations": list(designation.values())
        }

    except Exception as e:
        print("Error in get_complete_network_table:", e)
        raise
