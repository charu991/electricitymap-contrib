def Palindrome(string):

# Run loop from 0 to half of the input

for i in range(0, int(len(string) / 2)):

if string[i] != str[len(string) – i – 1]:

return False

return True

s = input(“Give me your word:\n”)

if Palindrome(s):

print(“It is A Palindrome”)

else:

print(“It is not a Palindrome”)
