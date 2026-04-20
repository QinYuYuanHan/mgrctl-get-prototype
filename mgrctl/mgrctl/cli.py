import argparse
from mgrctl.get import handle_get

def main():
    parser = argparse.ArgumentParser(prog="mgrctl")
    subparsers = parser.add_subparsers(dest="command")

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("resource", choices=["system", "group"])
    get_parser.add_argument("-f", "--filter")
    get_parser.add_argument("-o", "--output", choices=["json", "yaml"], default="json")

    args = parser.parse_args()

    if args.command == "get":
        handle_get(args)
