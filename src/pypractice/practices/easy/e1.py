

def about():

    print("""
    Exercise 1: Sum Two Numbers

    Write a function that receives two numbers
    and returns their sum.
    """)


def check(solution):

    tests = [
        ((1, 2), 3),
        ((5, 5), 10),
        ((-1, 1), 0),
        ((10, 20), 30),
    ]

    passed = 0

    for index, (inputs, expected) in enumerate(tests, 1):

        try:
            result = solution(*inputs)

            if result == expected:
                passed += 1
                print(f"Test {index}: PASS")
            else:
                print(f"Test {index}: FAILED")

        except Exception as error:
            print(f"Test {index}: ERROR - {error}")

    print(f"\n{passed}/{len(tests)} tests passed.")
