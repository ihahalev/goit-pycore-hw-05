import sys
from input_helper import load_logs
from analize_helper import count_logs_by_level, filter_logs_by_level
from print_out import display_log_counts, display_level_logs

def main():
    if len(sys.argv) < 2:
        return print("Logs path not provided")
    _, path, *args = sys.argv
    parsed_logs = load_logs(path)
    if not parsed_logs:
        return
    counted = count_logs_by_level(parsed_logs)
    display_log_counts(counted)
    if (args):
        level = args[0]
        records = filter_logs_by_level(parsed_logs, level.upper())
        display_level_logs(records, level.upper())

if __name__ == "__main__":
    main()
