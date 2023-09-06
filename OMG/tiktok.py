#deewanatool
import time
import webbrowser


print("Welcome to Dᴇᴇᴡᴀɴᴀ ᴛᴏᴏʟ")


# Ask the user for their name
tiktok_name = input("Please enter your Tiktok id: ")

# Add a 1-second delay
time.sleep(2)

# Print a greeting with the user's name
print(f"searching id = {tiktok_name}!")
time.sleep(2)
print(f"found id = {tiktok_name}!")
time.sleep(3)
print(f"Target is locked in  {tiktok_name} id!")
time.sleep(2)
print(f"First of all follow me in tiktok!")

url = "https://www.tiktok.com/@nirvanshah.m?lang=en"
webbrowser.open(url)

