## We need to find Dot an empty seat on the plane. We have ## logged the layout of the section of the plane as a Python ## list. This is formatted as a nested list, which means that ## elements of the list are lists as well. Listception.

## Note: Our plane section contains three sections of seats in ## each row, and three seats in each section. Here is what the ## values in the layout mean:

## e = empty seat
## o = occupied seat
## None = aisle (you can't sit here!)
## Capital letters = window seats
layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]
## Dot has two conditions for their sitting:

## It has to be window seat
## The next seat needs to be empty
## Identify the right place for Dot to sit. If there is more ## than one option that matches the conditions above, choose the ## seat that is closer to the front, i.e. has a lower row ## number. What is the list index of Dot's seat?

x = 0
for row  in layout:
  
  if (row[0] == "E" and row[1] == "e"):   
    print(x, 0)
    row.pop(0)
    row.insert(0, "O")
    break

  if row[-1] == "E" and row[-2] == "e":
    print(x, -1)
    row.pop(-1)
    row.insert(10, "O")
    break
  
  x = x + 1


print(layout)
