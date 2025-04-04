from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time


def main():
    bot = InternetSpeedTwitterBot()
    # bot.get_internet_speed()
    # time.sleep(5)
    bot.tweet_at_provider()
    # print(f"Download Speed: {down} Mbps")
    # print(f"Upload Speed: {up} Mbps")
    # bot.tweet_at_provider()
    
    
main()