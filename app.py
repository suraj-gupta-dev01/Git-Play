raw_data = list(map(lambda key: input(f"enter your {key}: "), ["name", "age", "contact", "city"]))
print(raw_data)



def filter_integers(func):
    def wrapper(*args, **kwargs):
        print(args)
    return wrapper


@filter_integers
def show_data(data):
    return data

show_data()