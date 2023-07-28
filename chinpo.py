import random
import time


long_chinpo = ""
while True:
    long_chinpo += random.choice("おちんぽ")
    print(long_chinpo[-1], end="", flush=True)
    if long_chinpo[-4:] == "おちんぽ":
        print()
        break
    time.sleep(0.1)

print("おぉぉお”お”～っ！！イグゥウ！！イッグゥウウ！！")
print(f"私は{len(long_chinpo)}回で果てました。。。")