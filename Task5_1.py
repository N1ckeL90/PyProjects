def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
for i in range(1, 10):
    try:
        print(next(odd_to_15))
    except StopIteration:
        print("StopIteration")
