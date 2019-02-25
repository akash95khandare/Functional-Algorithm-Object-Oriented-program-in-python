import com.bridgelab.util.Utility as u

rng = int(input("Enter range : "))
arr = u.get_prime_number(rng)
print(arr)
print(u.get_palindrome(arr))
print(u.get_anagram(arr))
