def format_table(fields, command):
    output = []
    for name, values in fields.items():
        vals_str = " ".join(str(v) for v in values)
        output.append(f"{name:<14}{vals_str}")
    output.append(f"{'command':<14}{command}")
    return "\n".join(output)
