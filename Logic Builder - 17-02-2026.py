# Logic Builder - FizzBuzz Program

def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    number_count = 0

    print("----- FizzBuzz Output from 1 to 50 -----")

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)
            number_count += 1

    print("\n----- Count Summary -----")
    print("Fizz occurred:", fizz_count, "times")
    print("Buzz occurred:", buzz_count, "times")
    print("FizzBuzz occurred:", fizzbuzz_count, "times")
    print("Numbers occurred:", number_count, "times")

# Calling the function
fizz_buzz()