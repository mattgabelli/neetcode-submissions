class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # read exactly `length` characters after the '#'
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result