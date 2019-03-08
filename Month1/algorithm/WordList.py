from util.Utility import word_list, read_from_file


def main():
    sts = read_from_file()
    print(sts)
    key = input("Enter word for search : ")
    if word_list(key, sts):
        print("Word found.")
    else:
        print("Word not found.")


if __name__ == '__main__':
    main()
