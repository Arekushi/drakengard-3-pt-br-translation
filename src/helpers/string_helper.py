import re
import ast

def get_list_from_response(response):
    try:
        response = re.sub(r'\s+', ' ', response).strip()
        pattern = r'\[([\s\S]*)\]'
        match = re.search(pattern, response)
        return ast.literal_eval(match.group(0))
    except (AttributeError, SyntaxError, ValueError, TypeError, StopIteration, RuntimeError, KeyError):
        return []
