

def validate_expression(expression):
    fields = expression.split()

    if len(fields) == 5:
        return True
    else:
        return False