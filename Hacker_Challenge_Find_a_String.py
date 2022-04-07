def count_substring(string, sub_string):
    j = 0
    if len(sub_string)>len(string):
        return 10
    else:
        for i in range(0, 1+len(string)-len(sub_string)):
            if string[i:i+len(sub_string)] == sub_string:
                j = j + 1
            else:
                continue
        return j


print(count_substring("ABCDCDC", "CDC"))