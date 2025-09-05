class Solution:
    def defangIPaddr(self, address: str) -> str:
        ipv4 = ""
        for s in address:
            if s == ".":
                ipv4 += "[.]"
            else:
                ipv4 += s
        return ipv4
