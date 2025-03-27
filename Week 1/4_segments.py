r'''
Your task is to divide a string into segments so that each segment is a repeat of the same character. The segments should be represented as a list of pairs containing the segments lengths and characters.

For example, the string aaabbccdddd has four segments and can be represented as the list [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')].

In a file segments.py, implement the function find_segments with a string as a parameter. The function returns a list of pairs representing the segments of the string.

Your function will be tested using many different strings. Each test string consists of the characters a–z and contains 1–100 characters.'
'''

def find_segments(data):
    # TODO
    result = [] #empty list where the result will be stored
    count = 1 #starting a counter variable to keep track of the number of characters 
    first_char = data[0] #starting character of the string provided
    for letter in data[1:]:
        if letter == first_char:
            count += 1 #if the character is the same as first_char we keep adding.
        else:
            result.append((count, first_char)) 
            first_char = letter
            count = 1
            # if is not equal to fisrt_char, we append the to result, we restart the first char assigning it to the current letter and we restart the count.
    
    result.append((count, first_char)) #once the loop is done, we append the final segment
    return result
   

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]