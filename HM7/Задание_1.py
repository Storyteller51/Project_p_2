def analyze_grades(*grades):
    if not grades:
        return None

    count = len(grades)
    average = sum(grades) / count
    highest = max(grades)
    lowest = min(grades)

    success = 0
    for i in grades:
        if i >= 60:
            success += 1

    return {
        "count": count,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": success
    }