from fastapi import Query, Request
from fastapi.responses import JSONResponse
from neo4j import GraphDatabase

# Neo4j connection setup
uri = "bolt://localhost:7687"
username = "neo4j"
password = "dairynet"
driver = GraphDatabase.driver(uri, auth=(username, password))

def get_complete_network(label, query):
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
        id(l) AS id_label, l.name AS label_name,
        id(a1) AS id_ap, a1.shortaction AS label_ap, 'Action Plan' AS source_ap, a1.name AS statement_ap,
        id(a2) AS id_fw, a2.shortaction AS label_fw, a2.source AS source_fw, a2.shortrecommendation AS reco_fw, a2.name AS action_fw,
        id(a4) AS id_fva, a4.name AS label_fva, a4.source AS source_fva, a4.mission AS mission_fva, a4.goal AS goal_fva, a4.actionstatement AS statement_fva,
        id(p5) AS id_fvr, p5.name AS label_fvr, p5.source AS source_fvr, p5.mission AS mission_fvr, p5.goal AS goal_fvr, p5.actionstatement AS statement_fvr,p5.reportsummary AS report_summary,
        id(t3) AS id_tag3, t3.name AS tag3,'Publications' AS source_tag3,t3.context AS context_tag3,
        id(s3) AS id_sec_label3, s3.name AS sec_label3,
        id(t4) AS id_tag4, t4.name AS tag4,'Publications' AS source_tag4, t4.context AS context_tag4,
        id(p4) AS id_prim4, p4.name AS prim_label4,
        id(d5) AS id_designation, d5.name AS designation_name, d5.sentiment AS sentiment, d5.thought AS thought
    """

    try:
        session = driver.session()
        results = session.run(cypher_query, parameters={"label": label, "topicFilter": topic_filter})

        nodes = {}
        links = []
        seen_links = set()  # Track unique links

        for record in results:
            id_label = record.get("id_label")
            label_name = record.get("label_name", label)

            # Add label node
            if id_label:
                nodes.setdefault(id_label, {
                    "id": id_label,
                    "label": label_name,
                    "type": "Label"
                })

            def add_node_and_link(node_id, label, node_type, source_id, link_type, tooltip=None):
                if node_id is None:
                    return
                if node_id not in nodes:
                    node = {
                        "id": node_id,
                        "label": label or "Unknown",
                        "type": node_type
                    }
                    if tooltip:
                        node["tooltip"] = tooltip
                    nodes[node_id] = node

                link_key = (source_id, node_id, link_type)
                if link_key not in seen_links:
                    links.append({"source": source_id, "target": node_id, "type": link_type})
                    seen_links.add(link_key)

            # Action Plan
            if record.get("id_ap"):
                add_node_and_link(
                    record["id_ap"],
                    record.get("label_ap"),
                    "AP_Action",
                    id_label,
                    "HAS_ACTION_AP",
                    {
                        "source": record.get("source_ap"),
                        "actionstatement": record.get("statement_ap")
                    }
                )

            # Food Wise
            if record.get("id_fw"):
                add_node_and_link(
                    record["id_fw"],
                    record.get("label_fw"),
                    "FW_Action",
                    id_label,
                    "HAS_ACTION_FW",
                    {
                        "source": record.get("source_fw"),
                        "shortrecommendation": record.get("reco_fw"),
                        "action": record.get("action_fw")
                    }
                )

            # Food Vision Action
            if record.get("id_fva"):
                add_node_and_link(
                    record["id_fva"],
                    record.get("label_fva"),
                    "FVA_Action",
                    id_label,
                    "HAS_ACTION_FVA",
                    {
                        "source": record.get("source_fva"),
                        "mission": record.get("mission_fva"),
                        "goal": record.get("goal_fva"),
                        "actionstatement": record.get("statement_fva")
                    }
                )

            # Food Vision Report
            if record.get("id_fvr"):
                add_node_and_link(
                    record["id_fvr"],
                    record.get("label_fvr"),
                    "FVR_Programme",
                    id_label,
                    "HAS_PROGRAMME_FVR",
                    {
                        "source": record.get("source_fvr"),
                        "mission": record.get("mission_fvr"),
                        "goal": record.get("goal_fvr"),
                        "actionstatement": record.get("statement_fvr"),
                        "reportsummary":record.get("report_summary")
                    }
                )

            # Publication - Tag
            if record.get("id_tag3"):
                add_node_and_link(
                    record["id_tag3"],
                    record.get("tag3"),
                    "Publication_Tag",
                    id_label,
                    "HAS_PUB_TAG",
                    {
                        "primsource": record.get("source_tag3"),
                        "primcontext": record.get("context_tag3")
                    }
                )

            # Publication - Secondary Label
            if record.get("id_sec_label3"):
                add_node_and_link(
                    record["id_sec_label3"],
                    record.get("sec_label3"),
                    "Publication_Secondary_Label",
                    record.get("id_tag3"),
                    "TAG_HAS_SEC_LABEL"
                )

            # Publication - Secondary Tag
            if record.get("id_tag4"):
                add_node_and_link(
                    record["id_tag4"],
                    record.get("tag4"),
                    "Publication_Secondary_Tag",
                    record.get("id_tag4"),  # This link might be different, confirm source node here
                    "SEC_TAG_HAS_LABEL",
                    {
                        "secsource" : record.get("source_tag4"),
                        "seccontext": record.get("context_tag4")
                    }
                )

            # Publication - Primary Label
            if record.get("id_prim4"):
                add_node_and_link(
                    record["id_prim4"],
                    record.get("prim_label4"),
                    "Publication_Primary_Label",
                    record.get("id_tag4"),
                    "SEC_PRIM_HAS_TAG"
                )

            # Sentiment Analysis
            if record.get("id_designation"):
                add_node_and_link(
                    record["id_designation"],
                    record.get("designation_name"),
                    "Designation",
                    id_label,
                    "HAS_DESIGNATION",
                    {
                        "sentiment": record.get("sentiment"),
                        "thought": record.get("thought")
                    }
                )

        return {
            "graph": {
                "nodes": list(nodes.values()),
                "links": links
            }
        }

    except Exception as e:
        print("❌ Error during get_complete_network:", str(e))
        raise
