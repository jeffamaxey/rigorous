str = "builtin ids can be overwritten without affecting internal operation"
list = list(str)
___assertEqual(list, list(str))
