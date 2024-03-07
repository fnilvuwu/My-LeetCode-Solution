class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        array_of_indices = []
        for i in range(len(words)):
            if x in words[i]:
                array_of_indices.append(i)

        return array_of_indices
