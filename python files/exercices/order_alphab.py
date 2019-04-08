alphabetic = "abcdefghijklmnopqrstuvwxyz" ## store alphabetic to compare
myString = "abcdefghijhgkwvlmnopqrstyes" ## my test string
result = myString[0:1] ## take the first char from myString
final_result = '' ## string to store the correct reuslt
for i in range(len(myString) - 1):
    current_char = i ## take the first char
    next_char = i + 1 ## take the next char
    
    ## if my current char <= next char continue in for loop and fill my reuslt
    if(alphabetic.find(myString[current_char]) <= alphabetic.find(myString[next_char])):
        result += myString[next_char]
    else:
        ## else compare my final result with my temp reuslt
        if len(final_result) < len(result):
            final_result = result
        result = myString[next_char] ## init result with the next char