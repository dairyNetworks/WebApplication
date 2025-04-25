from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend import query_module_combined
from backend import query_doc
from backend import query_module
from backend import network_com
from backend import network_query
from backend import get_action_table
from backend import get_fv_table
from backend import get_fvr_table
from backend import get_fw_table
from backend import get_action_plan
from backend import get_action_plan_network
from backend import get_fv
from backend import get_fv_network
from backend import get_fvr
from backend import get_fvr_network
from backend import get_fvr_report
from backend import get_fvr_report_network
from backend import get_fw_network
from backend import get_fw
from backend import get_sentiment_network
from backend import get_sentiment
from backend import get_primary_stakeholders
from backend import get_secondary_stakeholder
from backend import get_secondary_stakeholder_network
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Optional: Serve static files if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def read_search(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/network", response_class=HTMLResponse)
async def network_page(request: Request):
    return templates.TemplateResponse("network.html", {"request": request})

@app.get("/networkquery", response_class=HTMLResponse)
async def networkquery_page(request: Request):
    return templates.TemplateResponse("networkquery.html", {"request": request})

@app.get("/actionquery", response_class=HTMLResponse)
async def networkquery_page(request: Request):
    return templates.TemplateResponse("actionquery.html", {"request": request})

@app.get("/actionplan.html", response_class=HTMLResponse)
async def load_action_plan_page(request: Request, query: str, file_name: str, action: str):
    return templates.TemplateResponse("actionplan.html", {
        "request": request,
        "query": query,
        "file_name": file_name,
        "action": action
    })

@app.get("/foodvision.html", response_class=HTMLResponse)
async def load_fv_page(request: Request, query: str, action: str):
    return templates.TemplateResponse("foodvision.html", {
        "request": request,
        "query": query,
        "action": action
    })

@app.get("/foodvisionreportstake.html", response_class=HTMLResponse)
async def load_fv_stake_page(request: Request, query: str, action: str):
    return templates.TemplateResponse("foodvisionreportstake.html", {
        "request": request,
        "query": query,
        "action": action
    })

@app.get("/foodvisionreport.html", response_class=HTMLResponse)
async def load_fvr_page(request: Request, query: str, action: str):
    return templates.TemplateResponse("foodvisionreport.html", {
        "request": request,
        "query": query,
        "action": action
    })

@app.get("/foodwise.html", response_class=HTMLResponse)
async def load_fw_page(request: Request, query: str, identifier: str):
    return templates.TemplateResponse("foodwise.html", {
        "request": request,
        "identifier": identifier
        })

@app.get("/sentimentstats", response_class=HTMLResponse)
async def sentimentstats_page(request: Request):
    return templates.TemplateResponse("sentimentstats.html", {"request": request})

@app.get("/speakersentiment.html", response_class=HTMLResponse)
async def load_fw_page(request: Request, query: str, category: str, sentiment: str):
    return templates.TemplateResponse("speakersentiment.html", {
        "request": request,
        "category": category,
        "sentiment" : sentiment
        })


@app.get("/stakeholdermapping", response_class=HTMLResponse)
async def stakeholdermapping_page(request: Request):
    return templates.TemplateResponse("stakeholdermapping.html", {"request": request})

@app.get("/secondarystakeholder.html", response_class=HTMLResponse)
async def secondarystakeholder_page(request: Request, query: str, primaryStakeholder : str):
    return templates.TemplateResponse("secondarystakeholder.html", {
        "request": request,
        "query": query,
        "primaryStakeholder" : primaryStakeholder
    })

@app.get("/search/speaker", response_class=HTMLResponse)
async def search_speaker(request: Request, keywords: str = Query(..., description="Keywords to search for")):
    try:
        results = query_module_combined.function_call_combined(keywords)
        formatted_results = [
            {
                "Speaker": result["Speaker"],
                "Sliding_year": result["Sliding_year"],
                "Organisation": result.get("Organisation", "N/A"),
                "Designation": result.get("Designation", "N/A"),
                "Region": result.get("Region", "N/A"),
                "Keywords": ', '.join([f"{key}: {value}" for key, value in result.items() if key not in [
                    "Speaker", "Sliding_year", "Organisation", "Designation", "Region", "TotalFrequency", "_id"]])
            }
            for result in results if "Speaker" in result and "Sliding_year" in result
        ]
        return templates.TemplateResponse("speakerresult.html", {"request": request, "search_keywords": keywords, "results": formatted_results})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/search/document")
async def search_document(request: Request, keywords: str = Query(..., description="Keywords to search for")):
    try:
        results = query_doc.function_call(keywords)
        
        formatted_results = []
        for result in results:
            if "File Name" in result:
                keywords_dict = {k: v for k, v in result.items() if k not in ["File Name", "_id"]}
                keywords_str = ', '.join([f"{key}: {value}" for key, value in keywords_dict.items()])
                formatted_results.append({
                    "File Name": result["File Name"],
                    "Keywords": keywords_str
                })
        
        return templates.TemplateResponse("documentresult.html", {
            "request": request, 
            "results": formatted_results,
            "search_keywords": keywords
        })
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/speaker/details", response_class=HTMLResponse)
async def speaker_details(request: Request, keywords: str = Query(...), speaker: str = Query(...)):
    try:
        # Call the backend function for speaker details
        results = query_module.function_call_speaker(keywords, speaker)

        # Check if the results are empty
        if not results:
            return templates.TemplateResponse("speakerdetail.html", {
                "request": request,
                "keywords": keywords,
                "speaker": speaker,
                "results": None
            })
        
        # Render the details template with results
        return templates.TemplateResponse("speakerdetail.html", {
            "request": request,
            "keywords": keywords,
            "speaker": speaker,
            "results": results
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get("/get_network")
async def get_network():
    try:
        data = network_com.fetch_network_data()
        return JSONResponse(content=data)
    except Exception as e:
        print("Error in /get_network:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/get_network_graph")
async def get_network_graph(request: Request, query: str = Query(...)):
    try:
        print('Query:', query)
        graph_data = network_query.get_network_data(query)  # Existing network data
        table_data = network_query.get_table_data()         # New table data
        return JSONResponse(content={
            "graph": graph_data,
            "table": table_data
        })
    except Exception as e:
        print(f"Error fetching network data: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/get_action_table")
async def get_action_table_route(request: Request, query: str = Query(...)):
    try:
        print('Query:', query)
        table_data = get_action_table.get_action_table(query) 
        return {"table": table_data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_fv_table")
async def get_fv_table_route(request: Request, query: str = Query(...)):
    try:
        print('Query:', query)
        table_data = get_fv_table.get_fv_table(query) 
        return {"table": table_data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_fvr_table")
async def get_fvr_table_route(request: Request, query: str = Query(...)):
    try:
        print('Query:', query)
        table_data = get_fvr_table.get_fvr_table(query) 
        return {"table": table_data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_fw_table")
async def get_fw_table_route(request: Request, query: str = Query(...)):
    try:
        print('Query:', query)
        table_data = get_fw_table.get_fw_table(query) 
        return {"table": table_data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_action_plan")
async def get_action_plan_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    file_name: str = Query(..., description="Name of the action plan file"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('File Name:', file_name)
        print('Action:', action)
        table_data = get_action_plan.get_action_plan(query, file_name, action)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_action_plan_network")
async def get_action_plan_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    file_name: str = Query(..., description="Name of the action plan file"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('File Name:', file_name)
        print('Action:', action)
        graph_data = get_action_plan_network.get_action_plan_network(query, file_name, action)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_fv")
async def get_fv_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        table_data = get_fv.get_fv(query, action)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_fv_network")
async def get_fv_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        graph_data = get_fv_network.get_fv_network(query, action)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
@app.get("/get_fvr")
async def get_fvr_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        table_data = get_fvr.get_fvr(query, action)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_fvr_network")
async def get_fvr_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        graph_data = get_fvr_network.get_fvr_network(query, action)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_fvr_report")
async def get_fvr_report_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        table_data = get_fvr_report.get_fvr_report(query, action)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_fvr_report_network")
async def get_fvr_report_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    action: str = Query(..., description="Name of the action")
):
    try:
        print('Query:', query)
        print('Action:', action)
        graph_data = get_fvr_report_network.get_fvr_report_network(query, action)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/get_fw")
async def get_fw_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    identifier: str = Query(..., description="Name of the identifier")
):
    try:
        print('FW Query:', query)
        print('Identifier: ', identifier)
        table_data = get_fw.get_fw(query, identifier)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_fw_network")
async def get_fw_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    identifier: str = Query(..., description="Name of the identifier")
    ):
    try:
        print('FW Query Network:', query)
        print('Identifier: ', identifier)
        graph_data = get_fw_network.get_fw_network(query,identifier)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/get_sentiment")
async def get_sentiment_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    category: str = Query(..., description="Query category"),
    sentiment: str = Query(..., description="Query sentiment")
    ):
    try:
        print('Sentiment Query Network:', query)
        print('Category: ', category)
        print('Sentiment: ', sentiment)
        table_data = get_sentiment.get_sentiment(query, category, sentiment)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_sentiment_network")
async def get_sentiment_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    category: str = Query(..., description="Query category"),
    sentiment: str = Query(..., description="Query sentiment")
    ):
    try:
        print('Sentiment Query Network:', query)
        print('Category: ', category)
        print('Sentiment: ', sentiment)
        graph_data = get_sentiment_network.get_sentiment_network(query, category, sentiment)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/get_primary_stakeholders")
async def get_primary_stakeholders_route(
    request: Request,
    query: str = Query(..., description="Query identifier Document Name'")
    ):
    try:
        print('Sentiment Query Network:', query)
        primary_stakeholders = get_primary_stakeholders.get_primary_stakeholders(query)
        print("Primary Stakeholders:", primary_stakeholders)
        return JSONResponse(content={
            "stakeholders": primary_stakeholders
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
   
@app.get("/get_secondary_stakeholder")
async def get_secondary_stakeholder_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    primaryStakeholder : str = Query(..., description="Query primaryStakeholder")
):
    try:
        print('Query:', query)
        print('Primary Stakeholder:', primaryStakeholder)
        table_data = get_secondary_stakeholder.get_secondary_stakeholder(query, primaryStakeholder)
        return JSONResponse(content={
            "table": table_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/get_secondary_stakeholder_network")
async def get_secondary_stakeholder_network_route(
    request: Request,
    query: str = Query(..., description="Query identifier like 'car', 'wat', or 'liv'"),
    primaryStakeholder : str = Query(..., description="Query primaryStakeholder")
    ):
    try:
        print('Sentiment Query Network:', query)
        print('Primary Stakeholder:', primaryStakeholder)
        graph_data = get_secondary_stakeholder_network.get_secondary_stakeholder_network(query, primaryStakeholder)
        print("Graph Data:", graph_data)
        return JSONResponse(content={
            "graph": graph_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
