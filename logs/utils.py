def check_log_line(parser, line):
    try:
        parser.parse(line)
    except Exception:
        return False
    else:
        return True
