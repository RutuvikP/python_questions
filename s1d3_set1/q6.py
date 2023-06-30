def vowelCount(str):
    vowels = "aeiouAEIOU"
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count

output=vowelCount("Hello")
print(output)