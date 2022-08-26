def sum_of_digits(digits):
    assert digits >= 0 and digits == int(digits), f'Digit must be a positive integer'

    if digits == 0:
        return 0
    return (digits % 10) + sum_of_digits(digits // 10)


if __name__ == "__main__":
    print(sum_of_digits(24))
