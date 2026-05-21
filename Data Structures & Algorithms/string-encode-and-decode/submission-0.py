class Solution:

    def encode(self, strs: List[str]) -> str:
        final_output=''
        for string in strs:
            count=len(string)
            output=str(count)+"#"+string
            final_output+=output

        return final_output

    def decode(self, s: str) -> List[str]:
        i=0
        output=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            output.append(s[j+1:j+1+length])
            i=j+1+length
        return output
