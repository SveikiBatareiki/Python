def add_mult(numbers_list):
    print(numbers_list)
    numbers_list.sort()
    print(f"Counting smallest numbers {numbers_list[0]} and {numbers_list[1]} and multiplying by largest {numbers_list[2]} result is {(numbers_list[0]+numbers_list[1])*numbers_list[2]}")

add_mult([4,2,5])
add_mult([5,9,0])