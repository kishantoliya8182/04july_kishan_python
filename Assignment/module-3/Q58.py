# Q58. Write a Python program to read a random line from a file. 

import random

fr=open('list.txt','r')

read_lines=fr.readlines()

random_line=random.choice(read_lines)

print(random_line)


