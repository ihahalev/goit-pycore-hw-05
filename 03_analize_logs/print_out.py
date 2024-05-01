def display_log_counts(counts: dict):
    log_level = "log level"
    print(f"{log_level:<10} | amount")
    print(f"{'-'*10}-|-{'-'*6}")
    for level, count in counts.items():
        print(f"{level:<10} | {count}")

def display_level_logs(records: list[dict], level: str):
    if (records):
        print(f"\ndetail logs for level '{level}'")
        for data in records:
            print(f"{data['date']} {data['time']} - {data['message']}")
    else:
        print(f"\nno records for level '{level}'")