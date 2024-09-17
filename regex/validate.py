import re


email = input("What's your email?").strip()



# if '@' in email and '.' in email:
#     print("valid")
# else:
#     print("Invalid")




# username, domain = email.split("@")

# if username and ("." in domain): 
#     print("valid")
# else:
#     print("invalid")


# if(re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email)):
if(re.search(r"^(\w+\.)?\w+@(\w+\.)?\w+\.(com|org|edu)$", email), re.IGNORECASE):
    print("valid")
else:
    print("invalid")