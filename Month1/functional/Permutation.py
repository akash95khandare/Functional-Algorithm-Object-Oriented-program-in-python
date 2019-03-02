from util.Utility import permutation


def main():
    strInp = input("Enter a string : ")
    permutation(strInp, 0, len(strInp))


if __name__ == '__main__':
    main()
