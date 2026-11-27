

def validate_expression(expression):
    fields = expression.split()

    if len(fields) != 5:
        return False

    for field in fields:
        cleaned = field.replace("*", "").replace("-", "").replace("/", "").replace(",", "")
        if cleaned != "" and not cleaned.isdigit():
            return False

    ranges = [
        (0, 59),
        (0, 23),
        (1, 31),
        (1, 12),
        (0, 6)
    ]

    for i in range(5):
        if not validate_range(fields[i], ranges[i][0], ranges[i][1]):
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
