def parse_field(field_str, minimum, maximum):
    values = set()
    subfields = field_str.split(",")

    for sub in subfields:
        step = 1
        if "/" in sub:
            sub, step_str = sub.split("/", 1)
            step = int(step_str)

        if sub == "*":
            start, end = minimum, maximum
        elif "-" in sub:
            start_str, end_str = sub.split("-", 1)
            start, end = int(start_str), int(end_str)
        else:
            if step > 1:
                start, end = int(sub), maximum
            else:
                start = end = int(sub)

        for val in range(start, end + 1, step):
            values.add(val)

    return sorted(list(values))


def parse_expression(expression):
    parts = expression.strip().split(maxsplit=5)
    fields = parts[:5]
    command = parts[5]

    ranges = [
        ("minute", 0, 59),
        ("hour", 0, 23),
        ("day of month", 1, 31),
        ("month", 1, 12),
        ("day of week", 0, 6)
    ]

    parsed = {}
    for i, (name, min_val, max_val) in enumerate(ranges):
        parsed[name] = parse_field(fields[i], min_val, max_val)

    return parsed, command
