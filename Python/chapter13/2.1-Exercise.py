# 1. Filter Even Numbers
nums = [10, 15, 22, 33, 40, 55]

num_result = list(filter(lambda a: a%2==0, nums))
print(num_result)


# 2. Remove Empty Strings
words = ["hello", "", "python", "", "world"]

word_result = list(filter(lambda a: a if len(a)>0 else None, words))

print(word_result)

# 3. Filter Words Longer Than 4 Characters
names = ["Zippo", "Thor", "Batman", "AI", "CaptainIndia"]

names_result = list(filter(lambda a: len(a)>4, names))

print(names_result)


# 4. Double the Even Numbers Only

values = [1, 2, 3, 4, 5, 6]

value_result = list( map (lambda a:a*2, filter(lambda a:a%2==0, values)))
print(value_result)

# 5. Capitalize Names Starting with 'a'
names2 = ["alex", "bob", "angel", "maya", "adam"]

def cap_(l):
    return l.capitalize()

names2_result = list(map(cap_, filter(lambda a: a if a[0].lower()=='a' else None , names2)))

names2_result2 = list(map(lambda a:a.capitalize(), filter(lambda a: a if a[0].lower() == 'a' else None,names2)))


print(names2_result2)

