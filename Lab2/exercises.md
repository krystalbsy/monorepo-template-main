# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

In dictionary, if it's a set, pop() remove and return an arbitrary element from the set. If it is a dict, pop(key[, default]) will remove it and return its value if key is in the dictionary. popitem() will remove and return a (key, value) pair from the dictionary. 
This is not a good name, because these functions actually do two things, so should be renamed as 'popAndGet', etc.

Similarly, in list, pop() or pop(i) retrieves the item at i and also removes it, which is also not a good name because it does not fully describe what this function is doing.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

(1) Data Structure:
- Dictionary:
A dictionary is implemented as a hash table or hash map. It uses a hash function to map keys to their corresponding values.
Dictionaries are unordered, keys in a dictionary must be unique and immutable, and you use keys to access the item in dictionary.
- List:
A list is implemented as a dynamic array.
It stores elements in a contiguous block of memory, allowing for efficient indexing.
Lists are ordered collections, and you can access them by their index.

(2) Use Cases:
- Dictionaries:
Dictionaries are typically used when you have a collection of key-value pairs and need fast lookups based on keys. 
- List:
Lists are used when you need to maintain an ordered collection of elements and perform operations like appending, inserting, or removing elements based on their positions in the list.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, inside the[] will be the index of that item starting from 0. As long as it is within the range you are able to access it.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

(1)Pros:

- Flexibility: Python is known for its dynamic typing and ability to handle a wide range of data types, and libraries that follow suit can be more versatile in various applications.
- Code Reusability: You can use the same library or data structure in different projects with different data types without major modifications.
- Interoperability: Libraries that accept any data type can be more interoperable with other code and libraries, as they don't impose strict requirements on data types. 

(2)Cons:

- Type Safety: Working with any data type can lead to type-related errors at runtime, making it harder to catch issues during development. Code may not be as type-safe as it would be in a statically typed language.
- Performance Overhead: Handling any data type can introduce performance overhead, as the library may need to check and adapt to the data type at runtime. This can be a concern in performance-critical applications.
- Readability and Maintainability: Code that works with any data type might be less readable and maintainable because the data type is not always clear from the code itself. It may require additional documentation or careful naming conventions.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

I think the naming conventions in the Requests library are considered clear and well-structured, making it easy for users to understand how to use the library effectively. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, requests.Request(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None) has a lot of aruguments.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  


`**kwargs` is a syntax used in function definitions to allow a function to accept an arbitrary number of keyword arguments (keyword-value pairs) as input.

Why it might be good:

- Flexibility: `**kwargs` allows a method to accept a variable number of keyword arguments, which makes it more flexible.
- Reduced Overloading: Instead of overloading a method with multiple variations that accept different combinations of arguments, you can use `**kwargs` to consolidate these variations into a single method.

Why it might be bad:

- Lack of Explicitness: Using **kwargs can make your code less explicit because the method's signature does not clearly indicate what parameters are accepted. This can make it harder for developers to understand how to use the method correctly.
- Debugging Difficulty: it might be challenging to catch typos or mistakes in the keyword arguments since they are not statically checked. This can lead to runtime errors that are harder to debug.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Why is that?

Setting an argument's default value to None is a common practice when you want to make the argument optional. It provides flexibility to the caller, as they can choose to omit that argument when calling the function or method.
No Default Values: If an argument has no default value, it means that the caller is required to provide a value for that argument when invoking the method or function. This is typically done when the argument is considered mandatory for the function's operation.

Can arguments be set to anything besides None?
Yes, arguments can be set to any valid Python value as their default values. This includes numbers, strings, lists, dictionaries, objects, or any other data type. 

Why might it be good to set an argument to some predetermined value?
By specifying a predetermined default value, you ensure that the method behaves predictably when the argument is not explicitly provided. This can make the code easier to understand and debug.