#!/usr/bin/python3
import argparse
import math
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', help='Target IP Address', default='BLANK', type=str)
    parser.add_argument('-p', '--port', help='Target Port', default=110, type=int)              # Required Example
    parser.add_argument('-u', '--username', help='Username to test', nargs='?', type=str)       # Optional Example
    arguments = parser.parse_args()
    return arguments


def print_elapsed_time(_start_time):
    seconds = round(int(time.time() - _start_time), 2)
    minutes = math.trunc(seconds / 60)
    remaining_seconds = math.trunc(seconds - (minutes * 60))
    if len(f'{remaining_seconds}') != 2:
        remaining_seconds = f'0{remaining_seconds}'
    elapsed_time = f'{minutes}:{remaining_seconds}'
    msg = '**** Total_Time Elapsed: ' + elapsed_time + ' =======================\n\n'
    print(msg)


def main():
    args = parse_args()
    ip = args.ip
    port = args.port
    username = args.username
    # Do Stuff Here and Modify Above argparse with options as necessary.


if __name__ == '__main__':
    main()