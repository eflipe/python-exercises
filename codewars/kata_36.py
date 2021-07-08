"""
You must create a method that can convert a string from
any format into PascalCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.

"""
import string


def camelize(str_):
    new_str = ""
    index_flag = False
    for index, let in enumerate(str_.lower()):
        if let in string.punctuation or let.isspace():
            print(index)
            index_flag = True
            continue
        if index_flag is not False or index == 0:
            new_str += let.title()
            index_flag = False
        else:
            new_str += let

    return new_str


# otra
# def camelize(str_):
#     new_str = ""
#     new_word = True
#     for elem in str_:
#         if elem.isalnum():
#             new_str += elem.upper() if new_word else elem.lower()
#             new_word = False
#         else:
#             new_word = True
#     return new_str


if __name__ == "__main__":
    text = "your-NaMe-here"  # "YourNameHere"
    text_2 = "testing ABC"  # "TestingAbc"
    text_3 = "example name"
    text_4 = "cODE warS"
    text_5 = "java script"
    output = camelize(text_5)
    print(output)
