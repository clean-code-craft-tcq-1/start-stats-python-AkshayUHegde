from math import nan


def calculateStats(numbers):
    computedStats = {
        "avg": nan,
        "max": nan,
        "min": nan
    }
    if numbers:
        computedStats["avg"] = sum(numbers) / len(numbers)
        computedStats["max"] = max(numbers)
        computedStats["min"] = min(numbers)
    return computedStats


if __name__ == '__main__':
    print(calculateStats([1.5, 8.9, 3.2, 4.5]))
