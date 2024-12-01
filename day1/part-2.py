import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def get_list_data(inputFile):
    path = f"{BASE_PATH}/{inputFile}"
    left_list = []
    right_dict = {}
    with open(path, "r") as file:
        data = file.readlines()
        for line in data:
            left, right = line.split("   ")
            left_list.append(int(left))
            right = int(right)
            if right in right_dict:
                right_dict[right] += 1
            else:
                right_dict[right] = 1

    return left_list, right_dict


def get_similarity_score(left_list, right_dict):
    similarity_score = 0
    for x in left_list:

        similarity_score += x * right_dict[x] if x in right_dict else 0

    return similarity_score


def main(inputFile):
    left_list, right_dict = get_list_data(inputFile)
    similarity_score = get_similarity_score(left_list, right_dict)
    print(similarity_score)


main("input.txt")
