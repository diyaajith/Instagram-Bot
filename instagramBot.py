from instabot import Bot
bot = Bot()
bot.login(username="", password="")

#upload a picture
bot.upload_photo("profile.jpg", caption="Photo of a Human")

#follow someone
bot.follow("thisisbillgates")

#send a message
bot.send_message("Hello from Diya", ['user1','user2'])

#get follower info
my_followers = bot.get_user_followers("thisisbillgates")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()