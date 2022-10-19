original_str = "Sunapi"
vowels = ['a','e','i','o','u']

reverse_string = ""
vowels_from_original_str = []

for i in original_str:
    if i in vowels:
        vowels_from_original_str.append(i)
print(vowels_from_original_str)
for i in original_str:
    if i not in  vowels:
        reverse_string+=i
    else:
        reverse_string+=vowels_from_original_str.pop()
print(reverse_string)





