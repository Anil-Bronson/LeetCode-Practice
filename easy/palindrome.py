def isPalindrome(s: str) -> bool:
    new_string = s.lower().strip()
    print(new_string)
    if not new_string:
        return True
    
    for c in new_string:
        if not c.isalpha():
            new_string = new_string.replace(c,"")
            print(new_string)
        
    return new_string == new_string[::-1]

s = "A man, a plan, a canal: Panama"
isPalindrome(s)