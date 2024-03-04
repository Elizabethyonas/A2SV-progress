class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        self.backtrack(digits, digit_to_letters, '', combinations)
        
        return combinations
    
    def backtrack(self, digits, digit_to_letters, combination, combinations):
        if not digits:
            combinations.append(combination)
            return
        
        for letter in digit_to_letters[digits[0]]:
            self.backtrack(digits[1:], digit_to_letters, combination + letter, combinations)