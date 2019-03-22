from util.Utility import is_anagram


def main():
    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")

    if is_anagram(str1.strip(), str2.strip()):
        print("String is anagram.")
    else:
        print("String is not anagram.")


if __name__ == '__main__':
    main()
