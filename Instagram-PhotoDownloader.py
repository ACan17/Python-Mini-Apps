import instaloader

# Get instance
insta = instaloader.Instaloader()
userName = input("Enter the username of the profile: ")

# download profile picture
insta.download_profile(userName, profile_pic_only=True)