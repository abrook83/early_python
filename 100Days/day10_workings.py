# functions with outputs

def format_name(fname, lname):
    """ creates a full name in title case from the fname & lname inputs """
    full_name = f"{fname.title()} {lname.title()}"
    return full_name

print(format_name("aaron","brook"))