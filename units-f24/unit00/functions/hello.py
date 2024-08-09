def say_hello (name : str) -> str :
    """ This function prints a greeting """
    return("Hello, " + name + "!", "Is your name ", str(len(name)) + str("-characters "), "long?")

say_hello(name="Jane_Doe")