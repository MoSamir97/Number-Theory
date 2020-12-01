# Written by:
#               Name: Mohamed Samir Abdelkhalek
#               ID:   1527294

# The aim of this program is use the extended euclidian algorithm to do two things:
#   1. find the gcd(a,b) where a, b are given by the user.
#   2. find the integers x and y that would allow us to write the gcd(a,b) as a linear combination of a and b.

# Basically we care about 4 columns (x, y, r, q) and intially 2 rows: row_1 = (1, 0, a, 0) and row_2 = (0, 1, b, 0)

# If we want to add a new row we should examine if r_i/r_i+1 != 0.
# Suppose r_i/r_i+1 != 0, then we add a new row_i+2 to our matrix consists of (x_i+2, y_i+2, r_i+2, q_i+2)
# Where:
#       1. q_i+2 = floor(r_i/r_i+1)
#       2. r_i+2 = r_i - (r_i * q_i+2)
#       3. x_i+2 = x_i-2 - (q_i+2 * x_i-1)
#       4. y_i+2 = y_i-2 - (q_i+2 * y_i-1)

# Instead of making some gigantic matrix, only care about two consective rows: row_i,  row_i+1.
# Then update row_i with the values of row_i+1 and update row_i+1 with the values the values of row_i+2
# We can detect the recursive pattern in the our computation, thus we shall design our program to run based on recursive algorithm not iterative one.


def enterTwoIntegers():
    a = int(input('Enter a value for a: '))
    b = int(input('Enter a value for b: '))

    # If we have negative values, flip the signs and make the flags = True
    flag_Negative_value_a = False
    flag_Negative_value_b = False

    # If we swap, we need to unswap when printing the output
    flag_sawpped = False

    # if b < 0, b = |b|
    if b < 0:
        b = abs(b)
        flag_Negative_value_b = True

    # if a < 0, a = |a|
    if a < 0:
        a = abs(a)
        flag_Negative_value_a = True

    # If b > a, then swap b with a
    if b > a:
        b, a = a, b
        flag_sawpped = True

    # Create the intial tuples as descriped above.
    first_row = [1, 0, a, 0]
    second_row = [0, 1, b, 0]

    new_row = solve(first_row, second_row)
    x = new_row[0]
    y = new_row[1]
    gcd = new_row[2]

    # Flip the signs back
    if flag_Negative_value_a:
        a = -1 * a
        x = -1 * x

    if flag_Negative_value_b:
        b = -1 * b
        y = -1 * y

    gcd_ab = f'gcd({b}, {a}) = {new_row[2]}' if flag_sawpped else f'gcd({a}, {b}) = {new_row[2]}'
    linear_combination = f'We found the integers x = {x} and y = {y} such that'

    # If b < 0 make the combination look like this ax - by
    sign = '+'
    if b < 0:
        b = abs(b)
        sign = '-'

    linear_combination2 = f'{a}({x}) {sign} {b}({y}) = {gcd}'

    print(gcd_ab)
    print(linear_combination)
    print(linear_combination2)


def solve(first_row, second_row):
    new_q = first_row[2] // second_row[2]  # Compute q_i+2
    new_r = first_row[2] - (second_row[2] * new_q)  # Compute r_i+2
    new_x = 0
    new_y = 1

    if new_r != 0:
        new_x = first_row[0] - (new_q * second_row[0])
        new_y = first_row[1] - (new_q * second_row[1])

        # update first_row to have second_row values
        first_row = second_row[:]

        # Update seocond_row to have the new values
        second_row[0] = new_x
        second_row[1] = new_y
        second_row[2] = new_r
        second_row[3] = new_q

        # Now repeat the process recursively
        solve(first_row, second_row)

    # If new_r == 0, return second_row
    return second_row


# start the program by calling enterTwoIntegers() function
enterTwoIntegers()
