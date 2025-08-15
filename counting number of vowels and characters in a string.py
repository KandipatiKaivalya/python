s = input("Enter string: ")
v = "aeiouAEIOU"
vc = 0
cc = 0

for ch in s:
    if ch in v:
        vc += 1
    elif ch != " ":
        cc += 1

print("Vowels =", vc)
print("Consonants =", cc)
