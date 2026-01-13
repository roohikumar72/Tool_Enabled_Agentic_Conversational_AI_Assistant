def select_tool(task):
    if task == "job search":
        return "JOB_SEARCH_TOOL"
    elif task == "product price search":
        return "PRODUCT_SEARCH_TOOL"
    else:
        return "NO_TOOL"
