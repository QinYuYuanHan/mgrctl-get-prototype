import argparse
import json
import yaml

# mock data (模拟 Uyuni API 返回)
with open("mock_data.json") as f:
    DATA = json.load(f)


def filter_data(data, filter_expr):
    if not filter_expr:
        return data

    key, value = filter_expr.split("=")
    return [item for item in data if str(item.get(key)) == value]


def output_data(data, fmt):
    if fmt == "json":
        print(json.dumps(data, indent=2))
    elif fmt == "yaml":
        print(yaml.dump(data, sort_keys=False))
    else:
        for item in data:
            print(item)


def main():
    parser = argparse.ArgumentParser(prog="mgrctl")
    subparsers = parser.add_subparsers(dest="command")

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("resource", choices=["system", "group"])
    get_parser.add_argument("--filter", "-f", help="Filter (e.g. cpu=x86_64)")
    get_parser.add_argument("-o", "--output", choices=["json", "yaml"], default="json")

    args = parser.parse_args()

    if args.command == "get":
        data = DATA.get(args.resource, [])
        data = filter_data(data, args.filter)
        output_data(data, args.output)


if __name__ == "__main__":
    main()
