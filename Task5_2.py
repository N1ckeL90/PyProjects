N = 15
num_gen = (num for num in range(1, N+1, 2))
for i in range(1, 10):
    try:
        print(next(num_gen))
    except StopIteration:
        print("StopIteration")

