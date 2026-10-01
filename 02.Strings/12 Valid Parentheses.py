#LN: 20
def valid(s):
    st=[]
    map={ ")":"(", "]":"[", "}":"{" }
    for ch in s:
        if ch in map.values():
            st.append(ch)
        elif ch in map.keys():
            if not st or map[ch] != st.pop():
                return False
    return not st
#Time:O(n)
#Space:O(n)

    
    