import os
from typing import List

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def get_reports(inputFile: str) -> List[List[int]]:
    path = f"{BASE_PATH}/{inputFile}"
    reports = []
    with open(path, "r") as file:
        data = file.readlines()
        for line in data:
            report = [int(ele) for ele in line.split(" ")]
            reports.append(report)

    return reports


def isSafeReport(report: List[int]) -> bool:
    n = len(report)

    condition = report[0] - report[1]

    for i in range(1, n):
        diff = report[i - 1] - report[i]
        if not 1 <= abs(diff) <= 3:
            return False

        if diff * condition <= 0:
            return False

    return True


def get_safe_reports(reports: List[List[str]]) -> int:
    count = 0
    for report in reports:
        if isSafeReport(report):
            count += 1

    return count


def main(inputFile):
    reports = get_reports(inputFile)
    safe_count = get_safe_reports(reports)
    print(safe_count)


if __name__ == "__main__":
    # main("example.txt")
    main("input.txt")
