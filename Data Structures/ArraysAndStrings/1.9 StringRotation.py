# String Rotation
# Given two strings s1 and s2, write code to check if s2 is a rotation of s1. eg: "waterbottle" is a rotation of
# "erbottlewat"

class StringRotation:
    def __init__(self):
        self.str_1 = None
        self.str_2 = None

    def isSubstring(self, string):
        return string.find(self.str_1) >= 0

    def using_rotate_string(self):
        for i in range(len(self.str_1)):
            for j in range(len(self.str_2)):
                if self.str_1[i] == self.str_2[j]:
                    rotated_str = self.str_2[j:] + self.str_2[0:j]
                    if self.isSubstring(rotated_str):
                        return True
        return False

    def using_concatenate_string(self):
        return self.isSubstring(self.str_2 + self.str_2)


if __name__ == '__main__':
    stringRotationObj = StringRotation()
    stringRotationObj.str_1 = input()
    stringRotationObj.str_2 = input()
    print(stringRotationObj.using_concatenate_string())
