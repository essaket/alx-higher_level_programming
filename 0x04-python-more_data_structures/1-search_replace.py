#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda rep: replace if rep == search else rep, my_list))
