#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch and display GitHub user activity.")
    parser.add_argument("username", help="GitHub username to fetch activity for")
    parser.add_argument("-n", "--num-events", type=int, default=5, help="Number of recent events to display (default: 5)")
    return parser.parse_args()
if __name__ == "__main__":
    args = parse_arguments()
    print(args)
