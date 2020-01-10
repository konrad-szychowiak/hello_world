def is_palindrome(text: str) -> bool:
    """
    Function checks if the text and reverse are identical
    """
    return text == text[::-1]

data=input().lower()
out=True

if is_palindrome(data):
    out = True

else:
    for i in range(len(data)):
        if is_palindrome(data[:i] + data[i+1:]):
            out = True
            break
            
    for i in range(len(data)):
        for j in range(len(data)-i):
            if is_palindrome(data[:i] + data[i+1:i+j] + data[i+j+1:]):
                out = True 
                break
                break
        

print("YES" if out else "NO")
