'''
Link: https://www.codewars.com/kata/583203e6eb35d7980400002a
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

'''
def count_smileys(arr):
    if not arr:
        return 0
    smiling_mouth = [')', 'D']
    smiling_nose = ['-', '~']
    smiling_eyes = [':', ';']
    counter_smileys = 0
    for item in arr:
        if item[-1] in smiling_mouth and (item[-2] in smiling_eyes or item[-2] in smiling_nose):
            counter_smileys += 1

    return counter_smileys #the number of valid smiley faces in array/list

if __name__ == "__main__":
    test_1 = [':D',':~)',';~D',':)']
    output = count_smileys(test_1)
    print(output)

# otras soluciones
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

def count_smileys(arr):
    total = 0
    eyes = ':;'
    nose = '-~'
    mouth = ')D'
    for char in arr:

        if len(char) == 3:
            if char[0] in eyes and char[1] in nose and char[2] in mouth:
                total += 1

        elif len(char) == 2:
            if char[0] in eyes and char[1] in mouth:
                total += 1
    return total
