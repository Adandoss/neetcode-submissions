class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        val_max: int = arr[-1]
        maxes_indexes: List[int] = [len(arr)-1]

        for i in range(len(arr)-1, -1, -1):
            if arr[i] > val_max:
                maxes_indexes.insert(0, i)
                val_max = arr[i]

        j: int = 0
        for i in range(len(arr) - 1):
            if i >= maxes_indexes[j]:
                j += 1
            arr[i] = arr[maxes_indexes[j]]

        arr[-1] = -1
        
        return arr

        

