import concurrent.futures
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting - %s", name, threading.get_ident())
    time.sleep(3)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(thread_function, [f"runid_{id}" for id in range(10)] )