def load_logs(file_path: str) -> list[dict]:
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            parsed_list = [parse_log_line(record.strip()) for record in file.readlines()  if record.strip()]
        parsed_list = [log for log in parsed_list if log]
        return parsed_list
    except FileNotFoundError:
        print("load_logs FileNotFoundError")
        return []
    except Exception as error:
        print("load_logs error", type(error), error)
        return []

def parse_log_line(line: str) -> dict:
    try:
        date, time, level, *msg = line.split()
        return {
            'date': date,
            'time': time,
            'level': level.upper(),
            'message': ' '.join(msg) }
    except ValueError:
        print("parse_log_line warning, wrong log format")
        return {}
    except Exception as error:
        print("parse_log_line error", type(error), error)
        return {}