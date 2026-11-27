

def validate_expression(expression):
    parts = expression.strip().split(maxsplit=5)

    if len(parts) < 6:
        return False

    fields = parts[:5]

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
    subfields = field.split(",")
    for sub in subfields:
        if "/" in sub:
            parts = sub.split("/")
            if len(parts) != 2 or not parts[1].isdigit() or int(parts[1]) <= 0:
                return False
            sub = parts[0]

        if sub == "*":
            continue

        if "-" in sub:
            parts = sub.split("-")
            if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                return False
            start, end = int(parts[0]), int(parts[1])
            if start > end or not (minimum <= start <= maximum) or not (minimum <= end <= maximum):
                return False
            continue

        if sub.isdigit():
            val = int(sub)
            if not (minimum <= val <= maximum):
                return False
        else:
            return False

    return True
