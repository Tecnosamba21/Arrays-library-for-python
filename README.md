# Arrays_Utilities-base
A library created by TecnoSamba21

I know that working with arrays in python is so hard, so I made a library to make easier this work.

I present you my new library called "Array_utilities-base"! A library made in pure python to work with arrays and lists. Now, you're not going to spend a lot of time to (for example) search a element in a list!

*Commands:*
-	`__getInfoLocalArray__(Array)`: Get information about an array
- `delete(number, Array)`: Delete an element of an array
- `show(Array)`: Print an array in a terminal
- `search(Array,searching)`: Search if an element is in an array (if yes return true else return false, use it with a print or a bool type variable)
- `getIdentification(Array, Object)`: Get the position of an element in a array

## Example

~~~python
#/bin/python3

import functions

array = ['hello','world']

def isanelement(element):
  return search(array, element)

print(isanelement('hello'))

show(array)
~~~
