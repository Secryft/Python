#A string is a sequence of characters.
username = "admin"
ip = "192.168.1.1"
print(username[0])  #output a
print(username[-1]) #output n
#String Length & Looping
print(len(username)) #output 5

#Loop through string
for i in "Aditya":
    print (i)

password = "admin123"

print("Length:", len(password))

for ch in password:
    print(ch)

#String Slicing

msg= "failed_login"
print(msg[0:6])
print(msg[-2:])

#String Methods
name = "Aditya "
print(name.lower(),'XXXX')
print(name.strip(),'XXXX')

log = "error: invalid password"

print("error" in log)     # True
print(log.startswith("error"))  # True
print(log.endswith("password")) 

msg = "login failed"
print(msg.replace("failed", "success"))

text = "alert"
count = 0
for i in text:
    
    count += 1
    print(i)
print(count)

log = "user123fail3ed"

digit_count = 0

for ch in log:
    if ch.isdigit():
        digit_count += 1

print(digit_count)

boy= "Anku12a"
count = 0
for i in boy:
    if i.isdigit():
        count +=1
print("Total_nuber",count)
print("Total_char",len(boy)-count)

text = "security-alert-403"
print(text[9:14])
print(text[-9:-4])
print(text.split("-"))

text = "security-alert-403"
start = text.find("alert")
print(text[start:start + 5])

        
    