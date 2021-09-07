def smallest(my_list):
    smallest = ""
    for x in my_list:
        if smallest == "":
            smallest = x
        else:
            if len(x) < len(smallest):
                smallest = x

    return smallest


my_list = ["hello", "my", "world", "welcome", "python"]

print(smallest(my_list))
