response = input("What is you name? \n ")
name_prefix = 'name is'
name_prefix_start = response.find(name_prefix)
name_prefix_size =len(name_prefix)

if name_prefix_start > -1:
    name_start = name_prefix_start + name_prefix_size + 1
    name = response[name_start:]
    print("Hello {}!".format(name))
else:
    print("Couldn't find your name! Please use the following format:\n"
    "My name is <your name here>")