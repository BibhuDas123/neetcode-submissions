class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,L,M,R):
            left,right=arr[L:M+1],arr[M+1:R+1]
            i,j,k=L,0,0
            while j<len(left) and k<len(right):
                if left[j]<right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                i+=1
                j+=1
            while k<len(right):
                arr[i]=right[k]
                i+=1
                k+=1

        def mergeshot(arr,L,R):
            if L==R:
                return
            m=(L+R)//2
            mergeshot(arr,L,m)
            mergeshot(arr,m+1,R)
            merge(arr,L,m,R)
        mergeshot(nums,0,len(nums)-1)
        return nums