#! /usr/bin/env python3

import argparse

import MinecraftServer
import MinecraftServerConfiguration
import MinecraftServerManager
import Global

manager = MinecraftServerManager.MinecraftServerManager(Global.MinecraftServerManagerConfigPath)

def new(args):
    server = manager.createServer(args.name)
    server.loadConfig()
    server.config.setConfig("server-port", "22000")
    server.config.save()

def run(args):
    server = MinecraftServer.MinecraftServer(args.name)
    if not server.isConfigured():
        print ("Server is not configurated or does not exists")
        return False
    else:
        server.run()

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

