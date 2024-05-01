from collections import Counter

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list[dict]) -> dict:
    levels = [log['level'].upper() for log in logs]
    return Counter(levels)