my_list = ['python', 'java', 'ruby', 'dart', 'abcdef', 'javascript']
def mapper(x): return len(x)


max_list = [i for i in my_list if len(i) == max(list(map(mapper, my_list)))]
print(max_list)
