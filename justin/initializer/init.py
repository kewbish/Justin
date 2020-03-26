def display_welcome():
    msg = """
    Welcome to Justin
    We would like to get started
    
    Please fill in the details to make me do your work faster. 
    """
    print(msg)


def initialize(dictionary: dict):
    display_welcome()
    for entity in dictionary:
        if dictionary[entity] is None:
            try:
                user_input = input("{} >>> ".format(' '.join([x.capitalize() for x in entity.split('_')])))
                if user_input.isspace():
                    user_input = None
            except (KeyboardInterrupt, EOFError):
                user_input = None
            dictionary[entity] = user_input
    else:
        return dictionary
