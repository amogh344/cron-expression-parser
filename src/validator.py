

def validate_expression(expression):
    fields = expression.split()

    if len(fields) != 5:
        return False

    for field in fields:
        if not field.replace("*","").replace("-", "").replace("/", "").isdigit():
            return False
    return True


def validate_range(field, minimum, maximum):
    if field.isdigit():
        number = int(field)

        if minimum <= number <= maximum:
            return True
        else:
            return False

    return True
