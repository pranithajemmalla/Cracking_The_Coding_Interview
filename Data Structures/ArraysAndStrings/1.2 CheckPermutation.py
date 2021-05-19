# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other
from helper import timeit


class CheckPermutation:
    def __init__(self):
        self.first_string = None
        self.second_string = None

    @timeit
    def using_brute_force(self):
        for s in self.first_string:
            if s in self.second_string:
                self.second_string.replace(s, "", 1)
            else:
                return False
        return True

    @timeit
    def using_hash_table(self):
        dict_s1 = dict()

        for s in self.first_string:
            if s in dict_s1:
                dict_s1[s] += 1
            else:
                dict_s1[s] = 1

        for s in self.second_string:
            if s in dict_s1:
                dict_s1[s] -= 1
                if dict_s1[s] == 0:
                    dict_s1.pop(s)
            else:
                return False

        return True

    @timeit
    def using_sort(self):
        sort_s1 = "".join(sorted(self.first_string))
        sort_s2 = "".join(sorted(self.second_string))

        return sort_s1 == sort_s2


if __name__ == '__main__':
    checkPermutationObj = CheckPermutation()
    input_str1 = input()
    input_str2 = input()

    if len(input_str1) != len(input_str2):
        print(False)

    checkPermutationObj.first_string = input_str1
    checkPermutationObj.second_string = input_str2
    print(checkPermutationObj.using_brute_force())
    print(checkPermutationObj.using_hash_table())
    print(checkPermutationObj.using_sort())
