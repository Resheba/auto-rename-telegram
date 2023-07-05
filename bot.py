from telethon import TelegramClient, functions, sync
from telethon.errors.rpcerrorlist import UsernamePurchaseAvailableError, UsernameNotModifiedError, FloodWaitError
from randomizer import get_random_string
from dataclasses import dataclass
from asyncio import sleep as asleep
from time import sleep


@dataclass
class Bot:
    API_ID: int|str
    API_HASH: str
    PHONE: str|int
    PASSWORD: str

    def __post_init__(self):
        self.API_ID = int(self.API_ID)
        self.PHONE = str(self.PHONE)

        self.client = TelegramClient(self.PHONE, api_id=self.API_ID, api_hash=self.API_HASH, device_model="iPhone 55 Pro", system_version="IOS 100.1")
        self.client.start(phone=self.PHONE)
        self.me = self.client.get_me()
        self.username = self.me.username
        self.id = self.me.id
        print(self.username)

    def _change_channel_name(self, name: str, channel_id: int|str, debug: bool = False) -> bool:
        try:
            self.client(functions.channels.UpdateUsernameRequest(channel=channel_id, username=name))
        except (UsernamePurchaseAvailableError, UsernameNotModifiedError):
            return False
        except FloodWaitError as ex:
            if debug: print(f"Banned {self.username} for: {ex.seconds}")
            return False
        except Exception as ex:
            if debug: print(ex)
            return False
        return True
    
    def _change_channel_owner(self, user_id: int|str, channel_id: int, debug: bool = False) -> bool:
        try:
            self.client(functions.channels.EditCreatorRequest(channel=channel_id, user_id = user_id, password=self.PASSWORD))
        except Exception as ex:
            if debug: print(ex)
            return False
        return True
    
    def change_links(self, channels: list[int], delay: int = 2, debug: bool = False) -> bool:
        for channel_id in channels:
            for i in range(10):
                new_name = get_random_string(25)
                if self._change_channel_name(name=new_name, channel_id=channel_id, debug=debug):
                    break
                elif i == 9:
                    return False
            sleep(delay)
        return True
    
    def change_channels_owner(self, user_id: int|str, channels: list[int], delay: int = 2, debug: bool = False) -> bool:
        for channel_id in channels:
            if self._change_channel_owner(user_id=user_id, channel_id=channel_id, debug=debug):
                sleep(delay)
                continue
            return False
        return True


# Async methods for async projects.


async def chnage_channel_name(name: str, channel_id: int|str, client: TelegramClient, debug: bool = False) -> bool:
    try:
        await client(functions.channels.UpdateUsernameRequest(channel=channel_id, username=name))
    except (UsernamePurchaseAvailableError, UsernameNotModifiedError):
        return False
    except Exception as ex:
        if debug: print(ex)
        return False
    return True


async def change_channel_owner(user_id: int|str, channel_id: int, password: str, client: TelegramClient, debug: bool = False) -> bool:
    try:
        await client(functions.channels.EditCreatorRequest(channel=channel_id, user_id = user_id, password=password))
    except Exception as ex:
        if debug: print(ex)
        return False
    return True


async def bot_change_links(client: TelegramClient, channels: list[int], delay: int = 2, debug: bool = False) -> bool:
    for channel_id in channels:
        for i in range(5):
            new_name = get_random_string(20)
            if await chnage_channel_name(name=new_name, channel_id=channel_id, debug=debug, client=client):
                break
            elif i == 4:
                return False
        await asleep(delay)
    return True


async def hand_over_owner(client: TelegramClient, new_owner: str|int):
    pass
