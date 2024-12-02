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
    for i in range(n):
        sub_report = report[:i] + report[i + 1 :]
        m = len(sub_report)

        condition = sub_report[0] - sub_report[1]
        isOk = True
        for j in range(1, m):
            diff = sub_report[j - 1] - sub_report[j]
            if not 1 <= abs(diff) <= 3:
                isOk = False
                break

            if diff * condition <= 0:
                isOk = False
                break

        if isOk:
            return True

    return False


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
