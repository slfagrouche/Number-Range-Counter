# This function counts from start to end with an increment of inc.
# If is_exclusive is True, the end value is excluded from the count.
# If start is equal to end, the function returns None if is_exclusive is True, else it prints start.

def count_inc_end(start, end, inc, is_exclusive):
    # If start is equal to end, return None if is_exclusive is True, else print start and return
    if start == end:
        return None if is_exclusive else print(start)

    # If start is greater than end, negate inc to count down instead of up
    inc = -inc if start > end else inc

    # Check if the increment value is a multiple of the distance between start and end
    if (end - start) % abs(inc) == 0:
        # If it is, use range with end incremented by inc to include end in the list
        list = range(start, end + inc, inc)
    else:
        # If it's not, use range without end incremented to exclude end from the list
        list = range(start, end, inc)

    # Loop through the list and print the values
    for i in list:
        if is_exclusive and i == end:
            # If is_exclusive is True and we reach the end value, break the loop
            break
        print(i)

print("Testing count_inc_end(start, end, inc, is_exclusive)")
print("count_inc_end(5, 2, 2, True):")
count_inc_end(5, 2, 2, True)
print()

print("count_inc_end(2, 5, 2, False):")
count_inc_end(2, 5, 2, False)
print()

print("count_inc_end(-3, -7, 1, True):")
count_inc_end(-3, -7, 1, True)
print()

print("count_inc_end(2, 5, 1, False)")
count_inc_end(2, 5, 1, False)
print()

print("count_inc_end(5, 2, 2, False)")
count_inc_end(5, 2, 2, False)
print()

print("count_inc_end(6, 2, 2, False)")
count_inc_end(6, 2, 2, False)
print()


