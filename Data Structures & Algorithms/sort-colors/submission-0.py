class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def heapify(arr,n,i):
            largest=i
            left=i*2+1
            right=i*2+2
            if left<n and arr[left]>arr[largest]:
                largest=left
            if right<n and arr[right]>arr[largest]:
                largest=right
            
            if largest!=i:
                arr[largest],arr[i]=arr[i],arr[largest]
                heapify(arr,n,largest)
        
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            heapify(nums,n,i) #max heap
        
        for end in range(n-1,0,-1):
            nums[end],nums[0]=nums[0],nums[end]
            heapify(nums,end,0)
        
        