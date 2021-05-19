# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome

class PalindromePermutation:

    def __init__(self):
        self.input_str = None

    def using_hash_table(self):
        str_dict = dict()
        for s in self.input_str:
            if s != " ":
                if s in str_dict:
                    str_dict.pop(s)
                else:
                    str_dict[s] = 1

        return len(str_dict) == 0 or len(str_dict) == 1

    def using_sort(self):
        sorted_str = "".join(sorted(self.input_str))
        odd = None
        ind = 0
        for i in range(int(len(sorted_str)/2)):
            if sorted_str[ind] == sorted_str[ind+1]:
                ind += 2
            elif odd is None:
                odd = True
                ind += 1
            else:
                return False
        return True

    def using_bit_vector(self):
        checker = 0
        for s in self.input_str:
            index = ord(s) - ord('a')
            if (checker & 1 << index) > 0:
                checker = checker ^ 1 << index
            else:
                checker = checker | (1 << index)

        return (0 == checker) | (0 == (checker & (checker - 1)))


if __name__ == '__main__':
    palindromePermutationObj = PalindromePermutation()
    palindromePermutationObj.input_str = input()

    print(palindromePermutationObj.using_hash_table())
    print(palindromePermutationObj.using_sort())
    print(palindromePermutationObj.using_bit_vector())

