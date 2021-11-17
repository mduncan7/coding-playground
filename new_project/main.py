# I have multiple tokens and need to make connections with only one at a time!
# Look into logging (in std lib) and coloredlogs (not in std lib)
import time
from argparse import ArgumentParser
from typing import Union
import json
import threading

class MyCog():
    pass


class MyBot(object):
    def __init__(self):
        self._cog = None

    def run(self, token: str):
        print(f"I am running with token {token} using {self._cog}")

    def add_cog(self, cog: MyCog):
        self._cog = cog


def main(token_name: Union[str, None]):
    tokens = get_tokens()
    if token_name is None:
        run_all(tokens)
    else:
        token = tokens[token_name]["token"]
        run_token(token)


def get_tokens() -> dict:
    with open("config.json") as f:
        return json.load(f)["tokens"]


def run_all(tokens: dict):
    threads = list()
    for key, val in tokens.items():
        print(f"Main    : create and started bot using token {key}.")
        x = threading.Thread(target=run_token, args=(val["token"], 10,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"Main    : before joining thread #{index}...")
        thread.join()
        print(f"Main    : thread #{index} done!")


def run_token(token: str, loop_num: int = 1):
    my_bot = MyBot()
    my_bot.add_cog(MyCog())
    for i in range(loop_num):
        time.sleep(1)
        my_bot.run(token)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-t", "--token", type=str, dest="token", help="Choose the token to use.", required=False)

    args = parser.parse_args()

    main(args.token)
