print("Helloooooooo World. Observe the new line at the end!")

print('Single Ticks!')

print("We can mix double ticks." + ' and Single ticks for string concatenation')

print("We can create a string that has 'single ticks' if it is wrapped in double ticks")

print('We can also create a string that has "double ticks" if it is wrapped in single ticks')

print("This is a print statement with a redundant end argument", end="\n")

print("We are the champions", end=" my friend, No Newline.")

print("We can pass", "multiple arguments")

print("LETS BE CRAZY", "AND PASS", "THREE ARGUMENTS")

print("We have", 3, "arguments that aren't even the same type!")

print("There is a default sep value", "which is a space.")

print("we can pass an empty string", "-into the sep value", sep='')

print("I am too lazy and", "forgetful to add a", "space so we can use the sep argument", sep=" ")

print("Lets","put a bunch of","ampersands in", sep="&")

from time import sleep

print("Hello, world!", end='', flush=True)
sleep(5)
print("Bye!!!")