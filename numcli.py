from numerology.numerology.destiny_number import get_destiny_number


def main():
    N = str(input("Enter your full name : "))

    dest_num = get_destiny_number(N)

    print('Your Destiny Number is: {}'.format(dest_num))


if __name__ == '__main__':
    main()
