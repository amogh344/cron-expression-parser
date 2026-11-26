

def validate_expression(expression):
    fields = expression.split()

    if len(fields) != 5:
        return False

    for field in fields:
        if not field.replace("*","").replace("-", "").replace("/", "").isdigit():
            return False
    return True