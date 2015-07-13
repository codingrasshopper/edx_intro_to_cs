given_str = "abcdefggggaqabcdef"

def isalphabetical(s1):
    for x in range(len(s1)-1):
        
        if s1[x]> s1[x+1]:
            return False
        
    return True
        


def main():
    maxs =""
    start = 0 
    maxl=0
    end = 1
    while end < len(given_str)+1:
        substr = given_str[start:end]
        if isalphabetical(substr):
            end +=1
            #print substr
            if len(substr) > maxl:
                maxl = len(substr)
                maxs = substr
                
        else:
            start = end -1
    print maxs
                
    
if __name__=="__main__":
    main()
    
