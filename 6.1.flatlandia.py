

def find_special_state(states):
    # define the sets of letters in the same line in keyboard (qwerty) in a list
    list_of_sets = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
    # find the special state
    for state in states:
        state_set = set(state.lower().rstrip('\n'))
        for set_of_letters in list_of_sets:
            if state_set & set_of_letters == state_set:
                print(state)
                return state
    return None


# read the "states.txt" file
states_file = open("../resources/states.txt", "r", encoding="utf-8")
states = states_file.readlines()
states_file.close()

find_special_state(states)
