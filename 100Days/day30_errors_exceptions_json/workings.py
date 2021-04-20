try:
    """Attempt this...."""
    file = open("100Days\day30_errors_exceptions_json/a_file.txt")
    dict = {"key": "value"}
    print(dict["oogada"])
except FileNotFoundError:
    """Catch specific error types"""
    # print("There was an error")
    file = open("100Days\day30_errors_exceptions_json/a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"Key {error_message} does not exist")