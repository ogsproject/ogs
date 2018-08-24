#! /usr/bin/env python3

import argparse

from MinecraftServerManager import MinecraftServer
from MinecraftServerManager import MinecraftServerConfiguration
from MinecraftServerManager import MinecraftServerManager
from MinecraftServerManager import Global

manager = MinecraftServerManager.MinecraftServerManager(Global.MinecraftServerManagerConfigPath)

def new(args):
    server = manager.createServer(args.name)
    server.loadConfig()
    server.config.setConfig("server-port", "22000")
    server.config.save()

def run(args):
    manager.start(args.name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands help', dest="command")

    new_parser = subparsers.add_parser('new', help='new command help')
    new_parser.add_argument('name', help='name help')

    run_parser = subparsers.add_parser('run', help='run command help')
    run_parser.add_argument('name', help='name help')

    del_parser = subparsers.add_parser('del', help='del command help')
    del_parser.add_argument('name', help='name help')

    args = parser.parse_args()

    if args.command == "new":
        new(args)

    elif args.command == "run":
        run(args)

    elif args.command == "del":
        delete(args)

    else:
        parser.print_help()

