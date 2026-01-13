def format_response(task, tool, results):
    return {
        "task": task,
        "tool_used": tool,
        "results": results
    }
