def is_palindrome(text: str):
    return text == text[::-1]

data = input().lower()
out = False

if is_palindrome(data):
    out = True

else:
    for i in range(len(data)):
        if is_palindrome(data[:i] + data[i+1:]): out = True
        
    if not out:
        for i in range(len(data)):
            for j in range(len(data)-i):
                if is_palindrome(data[:i] + data[i+1:i+j] + data[i+j+1:]): out = True 

print("YES" if out else "NO")
