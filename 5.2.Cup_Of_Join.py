# def function Join that get unlimited number of lists and return a list of all the items in the lists
# the function can recive an other parameter 'sep' that will be the separator between the items in the list
# if the parameter is not given the default value will be '-'
def join(*lists, sep='-'):
    # create an empty list
    result = []
    # loop over the lists
    for inner_list in lists:
        # loop over the items in the list
        for item in inner_list:
            # add the item to the result list
            result.append(item)
    # return the result list
    return result
