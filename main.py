import sys
from src.validator import validate_expression
from src.parser import parse_expression
from src.formatter import format_table

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py \"<cron_expression>\"", file=sys.stderr)
        sys.exit(1)

    expr = sys.argv[1]
    if not validate_expression(expr):
        print("Error: Invalid cron expression", file=sys.stderr)
        sys.exit(1)

    fields, command = parse_expression(expr)
    print(format_table(fields, command))

if __name__ == "__main__":
    main()
