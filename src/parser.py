import re

def parse_line(line):
    pattern = r'(\w{3} \d+ \d+:\d+:\d+) \S+ sudo: (\w+) .*COMMAND=([/\w\s\-\.]+)'
    match = re.match(pattern, line)
    if match:
        timestamp, user, command = match.groups()
        return {
            "timestamp": timestamp,
            "user": user,
            "command": command.strip()
        }
    return None

def parse_log_file(path):
    logs = []
    with open(path) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                logs.append(parsed)
    return logs
