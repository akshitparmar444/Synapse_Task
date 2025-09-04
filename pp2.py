
def lumos(runes:str) -> int:
    required = ("lumos")
    added = set()
    count=0
    for ch in runes:
        ch_lower=ch.lower()
        count=count+1
        if ch_lower in required:
            added.add(ch_lower)
            if len(added)==5:
                return count
            
    return -1

print(lumos("lxUbcOS"))