from util.Utility import insertion_sort, start_watch, stop_watch


def main():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

    start = start_watch()
    print(insertion_sort(arr))
    print("Elapse time : ", stop_watch(start))

    start = start_watch()
    print(insertion_sort(list(stringArr)))
    print("Elapse time : ", stop_watch(start))


if __name__ == '__main__':
    main()
