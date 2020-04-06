#!/usr/bin/env python3

from multiprocessing import Process
import modbusServer
import sys
import time

def main():
    while True:
        time.sleep(1)

if __name__ == "__main__":

    server = Process(target=modbusServer.run_server)
    driver = Process(target=main)

    try:
        driver.start()
        server.start()
    except KeyboardInterrupt:
        print("Shutting down")
        server.terminate()
        driver.terminate()

