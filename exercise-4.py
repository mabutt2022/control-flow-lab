# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
sides = []
for _ in range(3):
    sides.append(input('Enter the lengths of three side of a triangle: '))

if len(set(sides)) == 1:
    print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a equalateral triangle')
elif len(set(sides)) == 2:
    print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a isosceles triangle')
else:
    print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a scalene triangle')