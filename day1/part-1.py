import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def get_lists(inputFile):
    path = f"{BASE_PATH}/{inputFile}"
    left_list = []
    right_list = []
    with open(path, "r") as file:
        data = file.readlines()
        for line in data:
            left, right = line.split("   ")
            left_list.append(int(left))
            right_list.append(int(right))

    return left_list, right_list


def get_total_distance(sorted_left, sorted_right):
    d = 0
    for i in range(len(sorted_right)):
        d += abs(sorted_left[i] - sorted_right[i])

    return d


def main(inputFile):
    left_list, right_list = get_lists(inputFile)
    left_list.sort()
    right_list.sort()
    total_distance = get_total_distance(left_list, right_list)
    print(total_distance)


main("input-1.txt")
