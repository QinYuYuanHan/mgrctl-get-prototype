from mgrctl.api import fetch_resource
from mgrctl.output import render_output

def apply_filter(data, filter_expr):
    if not filter_expr:
        return data

    key, value = filter_expr.split("=")
    return [item for item in data if str(item.get(key)) == value]

def handle_get(args):
    data = fetch_resource(args.resource)
    data = apply_filter(data, args.filter)
    render_output(data, args.output)
