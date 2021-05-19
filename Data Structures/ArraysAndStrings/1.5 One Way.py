# One way
# There are three types of edits that can be perfomed on strings: insert a character, remove a character, or replace a
# character. Given two strings , write a function to check if they are one edit (or zero edits) away.

class OneWay:
    def __init__(self):
        self.str_1 = None
        self.str_2 = None
        self.len_s1 = None
        self.len_s2 = None

    def using_strings_comparision(self):
        mis_match = False
        if oneWayObj.len_s1 == oneWayObj.len_s2:
            for i in range(len(self.str_1)):
                if self.str_1[i] != self.str_2[i]:
                    if not mis_match:
                        mis_match = True
                    elif mis_match:
                        return False
        else:
            for i in range(len(self.str_1)):
                if self.str_1[i] != self.str_2[i]:
                    if not mis_match:
                        mis_match = True
                        self.str_2 = self.str_2.replace(self.str_2[i], "", 1)
                    elif mis_match:
                        return False
        return True


if __name__ == "__main__":
    oneWayObj = OneWay()
    str1 = input()
    str2 = input()

    if len(str1) < len(str2):
        oneWayObj.str_1 = str1
        oneWayObj.str_2 = str2
    else:
        oneWayObj.str_1 = str2
        oneWayObj.str_2 = str1

    oneWayObj.len_s1 = len(oneWayObj.str_1)
    oneWayObj.len_s2 = len(oneWayObj.str_2)
    if abs(oneWayObj.len_s1 - oneWayObj.len_s2) > 1:
        print(False)

    print(oneWayObj.using_strings_comparision())
