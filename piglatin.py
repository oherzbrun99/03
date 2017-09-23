
def piglatinify():
    words = str(input("")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

piglatinify()

#could not figure out how to affect words that start with a vowel. Used
#https://stackoverflow.com/questions/23177250/converting-a-sentence-to-piglatin-in-python
#as reference