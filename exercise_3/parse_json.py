import json


def parse_json(f):
    a_values = []
    b_values = []

    for line in f:
        d = json.loads(line)

        if not isinstance(d, dict):
            continue

        try:
            a_value = d['A']
            b_value = d['B']
        except KeyError:
            continue

        if isinstance(a_value, int) or isinstance(a_value, float):
            a_values.append(a_value)

        if isinstance(b_value, str):
            b_values.append(b_value)

    return [
        min(a_values) if len(a_values) > 0 else None,
        max(b_values, key=len) if len(b_values) > 0 else None
    ]
