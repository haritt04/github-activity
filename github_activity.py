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

def fetch_events(username, limit=5, token=None):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                print(f"Error: Received status code {response.status}")
                sys.exit(1)
            data = response.read()
            events = json.loads(data)
            return events[:limit]
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response")
        sys.exit(1)

def display_events(event):
    for event in events:
        event_type = event.get("type")
        repo_name = event.get("repo", {}).get("name", "unknown repo")

        if event_type == "PushEvent":
            commits = len(event["payload"]["commits"])
            print(f"- Pushed {commits} commit(s) to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            issue_number = event["payload"]["issue"]["number"]
            print(f"- {action.capitalize()} issue #{issue_number} in {repo_name}")
        elif event_type == "PullRequestEvent":
            action = event["payload"]["action"]
            pr_number = event["payload"]["pull_request"]["number"]
            print(f"- {action.capitalize()} pull request #{pr_number} in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        elif event_type == "ForkEvent":
            print(f"- Forked {repo_name}")
        else:
            # fallback for unhandled event types
            print(f"- {event_type} on {repo_name}")

if __name__ == "__main__":
    args = parse_arguments()
    events = fetch_events(args.username, limit=args.num_events)
    display_events(events)
