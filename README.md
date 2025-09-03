# GitHub User Activity CLI

A beginner-friendly **command-line interface (CLI)** tool that fetches and displays a GitHub user's recent activity directly in your terminal.  
This project is based on the [Roadmap.sh *GitHub User Activity* project prompt](https://roadmap.sh/projects/github-user-activity).

It is built entirely with Python’s **standard library**, without any external dependencies.

---

## Features

- Fetch recent activity for any GitHub user
- Human-readable event summaries:
  - **Pushed** commits
  - **Opened/closed issues**
  - **Opened/closed pull requests**
  - **Starred** repositories
  - **Forked** repositories
- Limit number of displayed events (default: 5)
- Graceful error handling for:
  - Invalid usernames
  - API rate limits
  - Network issues
  - Invalid JSON responses

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/haritt04/github-activity.git
cd github-activity
````

### 2. Run the script

```bash
python github_activity.py <github-username>
```

### 3. Limit the number of events

```bash
python github_activity.py <github-username> -n 3
```

### Example output

```
- Pushed 2 commit(s) to haritt04/task-tracker
- Opened issue #12 in haritt04/github-activity
- Starred roadmapsh/projects
```

---

## How It Works

1. **Argument Parsing**
   Uses Python’s built-in `argparse` module to capture the GitHub username and event limit.

2. **Fetching Data**
   Makes a request to the GitHub API:
   `https://api.github.com/users/<username>/events`
   via `urllib.request`.
   (Optional: Add a GitHub token for higher rate limits.)

3. **Error Handling**
   Handles `HTTPError`, `URLError`, and JSON parsing errors with clear messages.

4. **Display**
   Converts API event data into a clean, readable format for the terminal.

---

## Credits

* Project idea from [Roadmap.sh](https://roadmap.sh/projects/github-user-activity)
* Built with **Python 3** and the **GitHub REST API**

---