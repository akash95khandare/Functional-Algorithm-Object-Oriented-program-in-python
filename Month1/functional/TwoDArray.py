from util.Utility import get_two_d_arr, display_two_d_arr


def main():
    r = int(input("Enter row value : "))
    c = int(input("Enter column value : "))
    arr = get_two_d_arr(r, c)
    display_two_d_arr(arr)


if __name__ == '__main__':
    main()
