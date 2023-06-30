def palindromeChecker(str1):
    bag=""
    for i in range(len(str1)-1,-1,-1):
        bag+=str1[i]
    if bag==str1:
        return True
    else:
        return False

given="madam"
output=palindromeChecker(given)
if output:
    print('Word '+given+' is palindrome')
else:
    print('Word '+given+' is not palindrome')