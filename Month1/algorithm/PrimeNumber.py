from util.Utility import get_palindrome, get_prime_number, get_anagram


def main():
    rng = int(input("Enter range : "))
    arr = get_prime_number(rng)
    print(arr)
    print(get_palindrome(arr))
    print(get_anagram(arr))


if __name__ == '__main__':
    main()
