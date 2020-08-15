#!/usr/bin/python3
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', help='Target IP Address', default='BLANK', type=str)
    parser.add_argument('-p', '--port', help='Target Port', default=110, type=int)              # Required Example
    parser.add_argument('-u', '--username', help='Username to test', nargs='?', type=str)       # Optional Example
    arguments = parser.parse_args()
    return arguments


def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    username = args.username
    # Do Stuff Here and Modify Above argparse with options as ncessary.