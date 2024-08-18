import telebot
import instaloader

# Replace with your bot token
bot_token = '7044639389:AAE7tGw3_nkZSJG2pZ8DXpB3ZCZ5X4KHW4s'
bot = telebot.TeleBot(bot_token)

# Initialize Instaloader
L = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "WELCOME TO OFFICIAL INSTAGRAM DOWNLOAD 💙\n"
        "SEND THE LINK OF THE REEL / IMAGE YOU WANT TO DOWNLOAD ❄️"
    )
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: True)
def download_instagram_media(message):
    link = message.text.strip()

    try:
        # Extract shortcode from the link
        shortcode = link.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        # Download the post to a specific folder
        L.download_post(post, target="downloads")

        bot.reply_to(message, "Downloaded successfully!")
    except instaloader.exceptions.InstaloaderException as e:
        bot.reply_to(message, f"Failed to download: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

bot.polling()