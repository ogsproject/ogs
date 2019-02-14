#! /usr/bin/env python3

import argparse, os

from OpenGameServer import ServerManager, Global, Log

Global.config.init()
manager = ServerManager.ServerManager()
manager.loadPlugins(os.path.join(os.path.dirname(__file__), "games"))

def new(args):
    manager.createServer(args.game)

def setProp(args):
    manager.setServer(args.name, args.prop, args.val)

def run(args):
    manager.start(args.name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands help', dest="command")

    new_parser = subparsers.add_parser('new', help='new command help')
    new_parser.add_argument('game', help='game help')

    new_parser = subparsers.add_parser('set', help='set command help')
    new_parser.add_argument('name', help='name help')
    new_parser.add_argument('prop', help='prop help')
    new_parser.add_argument('val', help='val help')

    run_parser = subparsers.add_parser('start', help='start command help')
    run_parser.add_argument('name', help='name help')

    del_parser = subparsers.add_parser('del', help='del command help')
    del_parser.add_argument('name', help='name help')

    args = parser.parse_args()

    if args.command == "new":
        new(args)

    elif args.command == "set":
        setProp(args)

    elif args.command == "start":
        run(args)

    elif args.command == "del":
        delete(args)

    else:
        parser.print_help()



# from flask import Flask

# app = Flask(__name__)

# app.run()

# @app.route("/")
# def hello():
#     return "Hello World!"
