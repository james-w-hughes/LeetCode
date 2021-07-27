class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend >= 0 and divisor >= 0:
            solution = dividend//divisor
            return solution
        elif dividend < 0 and divisor < 0:
            solution = (-dividend)//(-divisor)
            return solution
        else:
            solution = -(-dividend//divisor)
            return solution

