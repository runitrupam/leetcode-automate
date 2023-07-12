class Solution:
    def search(self, A: List[int], target: int) -> int:


        l = 0
        h =len(A) - 1 # 6
        def find_pivot(arr):
            #compare last element to mid element. 
            #If mid element is greater than last element, pivot must be on right move low to mid+1
            #If mid element is less than last element, move high to mid-1
                element_to_compare = arr[-1]
                low = 0
                high = len(arr)-1    
                while(low <= high):
                    mid = (low+high)//2
                    if element_to_compare < arr[mid]:
                        low = mid+1
                    elif element_to_compare >= arr[mid]:
                        high = mid-1
                return low
        pivot = find_pivot(A)
        print('pivot =',pivot)

        def binary_search(B,l,r):
            # print(B , l ,r,target)
            while(l<=r):
                mid = (l+r )// 2

                if B[mid] == target:
                    return mid
                elif B[mid] > target:
                    r = mid - 1
                elif B[mid] < target:
                    l = mid + 1

            return -1
        # print(A)
        if binary_search(A,0,pivot-1) != -1:
            return binary_search(A,0,pivot-1)
        elif binary_search(A,pivot,len(A) - 1) != -1:
            return binary_search(A,pivot,len(A) - 1)
        return -1