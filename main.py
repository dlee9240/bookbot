#print ("hello world")
"""
First iteration of the program where I wrote it all in main!
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    #this function returns the words read as a STRING
    return file_contents

def count_words(text):
    
    count = 0
    words = text.split()
    
    #loop through the words after splitting the string. 
    for w in words:
        count += 1

    print (count)

main = main()
count_words(main)

"""

#second attempt to break it out into a function
def main():

    path = "books/frankenstein.txt"
    file_text = read_file(path)
    count = count_words(file_text)
    #print (count)
    #characters_in_file is a dictionary with key being the character and the value = number of times it appears
    characters_in_file = count_characters(file_text) 
    #print (characters_in_file)
    print_report(characters_in_file, count, path)





def read_file(path):
    with open(path) as f:
        file_path = f.read()
    return file_path


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    #text = STRING from the file reader!
    
    #changes the string into a list of every character
    lower_text = text.lower()
    characters = list(lower_text)
    #print (characters)

    #create an empty dictionary
    character_dict = {}
    for character in characters:
        #check if the character is in the dictionary:
        if character in character_dict:
            #plus 1 for the value in the dictionary
            character_dict[character] += 1
        #else add the character in the dictionary and add 1
        else:
            character_dict[character] = 1

    return character_dict

def print_report(char_dict, count, path):
    #I THINK I HAVE TO MODIFY MY ABOVE DICTIONARY CALL TO GIVE KEY VALUE PAIRS OF CHARACTER: X, COUNT: C" TYPE THING....
    #STOP HERE FOR 1/31/25. MY HEAD HURTS


    #convert the dictionary into a List of DICTIONARIES
    #need an empty list to start with.
    list_of_dict = []
    #iterate through the dictionary and append to the list with the new key value pairs...
    for c in char_dict:
        my_dict = {"char": c, "num": char_dict[c]}
        
        #append the dictionary item to the list IF it's in the alphabet...
        if c.isalpha():
            list_of_dict.append(my_dict)
        #have a list of dictionary items with keys and values
        

    list_of_dict.sort(reverse = True, key = sort_on)
    
    print (f"--- Begin report of {path} ---")
    print (f"{count} words found in the document")
    for l in list_of_dict:
        print (f"The '{l['char']}' in character was found {l['num']} times")
    print ("--- End of report ---")



        #print (c)
  




    """
    print (f"--- Begin report of {path} ---")
    print (f"{count} words found in the document")
    for char in char_dict:
        print (f"The '{char}' character was found {char_dict[char]} times")

    #convert the dictionary into a list and run sort on it
    #list_dict = list(char_dict.values())
    #list_dict = list(char_dict)
    
    #list_dict.sort(reverse = True)
    
    #sort_dict = char_dict.sort(reverse = True, key = char_dict.keys())

    #print (sort_dict)
    list_dict = list(char_dict.items())
        
    list_dict.sort(reverse = True)

    print (type(list_dict))

    print (list_dict)    

    #sd = {i: char_dict[i] for i in list_dict}
    
    
    
    
    
    c = count
    p = path

"""

def sort_on(dict):
    return dict["num"]



main()