import speedSensDriver
import sys
import time

try:
    driver = speedSensDriver.speedSensDriver()
    while True:
        RPM = driver.getRPM()
        pulse = driver.getPulse()
        elapsed_time = driver.getTime()
        sys.stdout.write("\rRPM:     "+str(RPM)+", Pulse:     "+str(pulse)+", Time:     "+str(elapsed_time))
        sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nClosing")
