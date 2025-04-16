# this is a comment

users = ['Ashley', 'Jaylen', 'Kita']

data = ['Ashley', 42, True]

emptylist = []

print('Ashley' in users)

print(users[0])
print(users[-2])

print(users.index('Kita'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Jaylen')
print(users)

users += ['Mickey Mouse']
print(users)

# users.extend(['Donald', 'Duck'])
# print(users)

users.insert(0, 'Daffy')
print(users)

users[2:2] = ['Tom','Peter']
print(users)

users[1:3] = ['TP', 'TJ']
print(users)

users.remove('TJ')
print(users)

print(users.pop())

del users [0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['ashley']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)

# Tuples

mytuple = tuple(('Ashley', 42,True))

anothertuple = (1, 4, 2, 8, 2, 4, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append( 'Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(data.)

print(anothertuple.count(2))

