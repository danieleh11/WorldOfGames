import random


def generate_sequence(chosen_difficult):
    random_list = []
    for num in range(1, chosen_difficult + 1):
        rand_num = random.randint(1, 102)
        random_list.append(rand_num)
    return random_list


def get_list_from_user(chosen_difficult):
    user_list = []
    for num in range(1, chosen_difficult + 1):
        user_num_list = input(f"enter numbers between 1 to 102, Input {chosen_difficult} numbers:")
        user_list.append(user_num_list)
    return user_list


def is_list_equal(random_list, user_list):
    is_equal = bool(set(random_list).intersection(user_list))
    if is_equal:
        print(f"User Won! users input={user_list} , comp input={random_list}")
        return True
    else:
        print(f"User Lost! users input={user_list} , comp input={random_list}")
        return False


def play_memory(chosen_difficult):
    random_list = generate_sequence(chosen_difficult)
    user_list = get_list_from_user(chosen_difficult)
    return is_list_equal(random_list, user_list)

