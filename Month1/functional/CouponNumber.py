from util.Utility import coupon_generator


def main():
    n = int(input("Enter a number : "))
    ls = coupon_generator(n)
    print(ls)


if __name__ == '__main__':
    main()
