from src.validator import validate_expression
from src.parser import parse_expression

expr = "*/15 0 1,15 * 1-5 /usr/bin/find"
if validate_expression(expr):
    fields, cmd = parse_expression(expr)
    print(fields)
    print(cmd)



