from tools.job_search_tool import find_jobs
from tools.product_search_tool import find_products

def execute_tool(tool, query):
    if tool == "JOB_SEARCH_TOOL":
        return find_jobs(query)

    elif tool == "PRODUCT_SEARCH_TOOL":
        return find_products(query)

    else:
        return {"message": "I can answer questions or help search jobs/products."}
