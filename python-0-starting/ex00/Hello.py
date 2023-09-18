ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

"""
List
- ordered collection of items
- mutable, meaning you can change its elements
- commonly used for sequences of data that may change over time

Tuple
- ordered collection of items, like a list
- immutable, meaning you cannot change its element once defined
- commonly used for collections of values that shouldn't change

Set
- unordered collection of unique elements
- the order in which the elements are inserted into the set will not preserved
- mutable

Dictionary (dict)
- unordered collection of key-value pairs
- mutable
- keys are unique
"""

ft_list[1] = "World!"
ft_tuple = ("Hello", "Malaysia!")
ft_set.remove("tutu!")
ft_set.add("Subang Jaya!")
ft_dict["Hello"] = "42 Kuala Lumpur!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)