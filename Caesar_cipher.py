message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))

#==============ENCODING==============
encoded_message = ""
for ch in message:
    if ch == ' ' or ch == '!':
        encoded_message = encoded_message + ch
        continue
    elif ord(ch) in range(ord('A'),ord('Z')+1): #ord() ASCII code for letter
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message = encoded_message + new_char
    else:
        pos = ord(ch) - ord('a')  # 21
        pos = (pos + offset) % 26  # 2
        new_char = chr(pos + ord("a"))
        encoded_message = encoded_message + new_char
print(encoded_message) 

#==============DECODING==============
decoded_message = ''
for ch in encoded_message:
    if ch == ' ' or ch == '!':
        decoded_message = decoded_message + ch
        continue
    elif ord(ch) in range(ord('A'),ord('Z')+1):
        pos = ord(ch) - ord('A')  # 21
        pos = (pos - offset) % 26  # 2
        new_char = chr(pos + ord("A"))
        decoded_message = decoded_message + new_char
    else:
        pos = ord(ch) - ord('a')  
        pos = (pos - offset) % 26 
        new_char = chr(pos + ord("a"))
        decoded_message = decoded_message + new_char   
print(decoded_message)
        
        
    
    
        
        
        
        
    
        