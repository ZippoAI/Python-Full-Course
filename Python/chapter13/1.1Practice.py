# grocery = ['Milk', 'Eggs', "Bread"]

# for i , j in enumerate(grocery, start=1):
#     print(f"{i}. {j}")


# numbers = [10, 3, 4, 7, 8]

# for ind, value in enumerate(numbers):
#     if value%2==0:
#         print(f"Index: {ind}, Value: {value}")

# words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# empty = []
# for i , j in enumerate(words):
#     if i%2==0:
#         empty.append('Even')
#     else:
#         empty.append(j)
# print(empty)



# correct = ['A', 'C', 'B', 'D', 'A']
# student = ['A', 'B', 'B', 'D', 'C']

# for i, j in enumerate(correct):
#     student_answer = student[i]
#     if student_answer != j:
#         print(f'Question No. {i+1}: Wrong (Your answer {student_answer} and Correct answer {j})')

# nums = [1,2,3]

# l1= iter(nums)

# # for num in nums:
# #     print(num)


# print(next(l1))
# print(next(l1))


# user_id = ['user1', 'user2', 'user3']

# user_name = ['Zippo', 'Bulbul', 'Alkama']

# result = dict(zip(user_id, user_name))

# print(result)

l1 = [2,5,7]
l2 = [1,6,2]

empty = []

def check_greater(l1, l2):
    for i in range(len(l1)):
        if l1[i]> l2[i]:
            empty.append(l1[i])
        else:
            empty.append(l2[i])
    print(empty)

check_greater(l1,l2)


