if __name__ == '__main__':
    s = list(input())
    alnum_number=0
    alpha_number=0
    digit_number=0
    lower_number=0
    upper_number=0
    for i in s:
        if i.isalnum():
            alnum_number+=1
        if i.isalpha():
            alpha_number+=1
        if i.isdigit():
            digit_number+=1
        if i.islower():
            lower_number+=1
        if i.isupper():
            upper_number+=1
print(alnum_number > 0)
print(alpha_number > 0)
print(digit_number > 0)
print(lower_number > 0)
print(upper_number > 0)