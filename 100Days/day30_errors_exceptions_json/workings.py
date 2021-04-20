# try:
#     """Attempt this...."""
#     file = open("100Days\day30_errors_exceptions_json/a_file.txt")
#     dict = {"key": "value"}
#     print(dict["oogada"])

# except FileNotFoundError:
#     """Catch specific error types"""
#     # print("There was an error")
#     file = open("100Days\day30_errors_exceptions_json/a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:   # capture the Key word to pass into the error text...
#     print(f"Key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     raise KeyError("Gotcha")
#     # file.close()
#     # print("File was closed")

#____________________________________________________________________________#

height = float(input("Enter height: "))
weight  = float(input("Enter weight: "))

bmi = weight / height **2
print(bmi)

if height > 3:
    raise ValueError("Nah mate, that's way too tall!")