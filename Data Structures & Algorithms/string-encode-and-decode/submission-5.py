class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        length = 1
        for word in strs: 
            length = len(word)
            encoded_string += str(length)
            encoded_string += ","
        encoded_string += "#"
        for word in strs:
            encoded_string += word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        str_length = len(s)
        seen = []
        index = 0
        once = False
        curr = ""
        for i in range(str_length):
            if s[i] == "#" and once == False:
                once = True
                index = i 
                break

            if s[i] == ",":
                seen.append(int(curr))
                curr = ""
            else:
                curr += s[i]
        
        pos = index + 1
        for j in range(len(seen)): 
            y = seen[j]
            decoded_strs.append(s[pos: pos+y])
            pos = pos + y
        return decoded_strs



