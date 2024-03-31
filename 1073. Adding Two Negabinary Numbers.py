class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def to_decimal(arr):
            n = 0
            number = 0
            # flip the array to get the least significant digit first
            for i in arr[::-1]:
                number += i * (-2) ** n
                n += 1
            return number
        
        def to_negabinary(num):
            if num == 0:
                return [0]
            digits = []
            while num != 0:
                remainder = num % -2
                num //= -2
                if remainder < 0:
                    remainder += 2
                    num += 1
                digits.append(remainder)
            return digits[::-1]
        
        number_arr1 = to_decimal(arr1)
        number_arr2 = to_decimal(arr2)
        
        sum_arr = number_arr1 + number_arr2

        return to_negabinary(sum_arr)
