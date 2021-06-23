def number(lines):
    if lines:
        lines = [f'{line+1}: {lines[line]}' for line in range(len(lines))]

    return lines


def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
