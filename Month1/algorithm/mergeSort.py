from array import array
from util.Utility import merge_sort, start_watch, stop_watch


def main():
    arr = array('i', [56, 35, 4, 99, 98, 77, 3, 2, 1, 0])
    stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

    start = start_watch()
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
    print("Elapse time : ", stop_watch(start))

    start = start_watch()
    merge_sort(stringArr, 0, len(stringArr) - 1)
    print(stringArr)
    print("Elapse time : ", stop_watch(start))


if __name__ == '__main__':
    main()
