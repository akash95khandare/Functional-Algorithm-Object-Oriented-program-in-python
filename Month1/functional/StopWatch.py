from util.Utility import start_watch, stop_watch


def main():
    start = start_watch()
    print(stop_watch(start))


if __name__ == '__main__':
    main()
