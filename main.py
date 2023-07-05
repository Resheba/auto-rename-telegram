from config import CHANNELS, BOTS
from time import sleep


def bots_circle(delay: int = 60*4, start_delay: int = 0):
    sleep(start_delay)

    for index, bot in enumerate(BOTS):
        cur_bot = bot
        next_bot = BOTS[(index+1)%len(BOTS)]
        if not cur_bot.change_links(channels=CHANNELS, debug=True):
            print('Link Error')
            return False
        if not cur_bot.change_channels_owner(user_id=next_bot.id, channels=CHANNELS, debug=True):
            print('Owner Error')
            return False
        sleep(delay)
    return False


def error_checker():
    choose = input('\nWhat will we do?\n1. Go next\n2. Exit\n')
    if choose == '1': return True
    elif choose == '2': return False
    else: return error_checker()


def main():
    while 1:
        circle = bots_circle()
        if not circle:
            if not error_checker(): return


if __name__ == "__main__":
    main()