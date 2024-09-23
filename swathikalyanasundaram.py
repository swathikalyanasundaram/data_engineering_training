#1
fruits=['apple','banana','cherry','date','elderberry']
print(fruits)

#2
print('First fruit:',fruits[0])
print('Last element:',fruits[-1])
print('Second fruit:',fruits[1])
print('Fourth element:',fruits[3])

#3
fruits[1]='blueberry'
print(fruits)

#4
fruits.append('fig')
fruits.append('grape')
fruits.remove('apple')
print(fruits)

#5
first_three_elements=fruits[:3]
print(first_three_elements)

#6
length_of_fruits=len(fruits)
print('Length of fruits:',length_of_fruits)

#7
vegetables=['carrot','broccoli','spinach']
food=vegetables+fruits
print(food)

#8
for fruit in fruits:
    print(fruit)

#9
if fruits=='cherry':
    print('Cherry is present')
else:
    print('Not present')

if fruits=='mango':
    print('mango is present')
else:
    print('Not present')

#10
fruit_lengths=[len(fruit) for fruit in fruits]
print(fruit_lengths)

#11
fruits_sorted=sorted(fruits)
print('Sorted fruits:',fruits_sorted)
print('Reversed fruits:',fruits_sorted[::-1])

#12
nested_lists=[['apple','banana','cherry'],['fig','grapes','elderberry']]
print(nested_lists[1][0])

#13
numbers=[1,2,2,3,4,4,4,5]
remove_duplicates=list(set(numbers))
print(remove_duplicates)

#14
word = "hello, world, python, programming"
splitted_words = word.split(", ")
print('Splitted words:',splitted_words)
joined_words = " ".join(splitted_words)
print("Joined words:",joined_words)