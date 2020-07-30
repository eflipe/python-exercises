# Given a sentence, sort it alphabetically in ascending order.
# Function to sort the words
# in ascending order
def sortedSentence(Sentence):

    # Splitting the Sentence into words
    words = Sentence.split(" ")

    # Sorting the words
    words.sort()

    # Making new Sentence by
    # joining the sorted words
    newSentence = " ".join(words)

    # Return newSentence
    return newSentence 
