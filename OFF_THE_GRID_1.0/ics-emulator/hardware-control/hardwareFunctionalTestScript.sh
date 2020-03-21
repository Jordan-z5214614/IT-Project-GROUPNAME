#!/bin/bash

#TODO Add in assertion and exception testing

# Nominal value testing, this is to be used to confirm motor 1 -4 and LED strip 1 -4
print "test sequence for motors"
for i in 1 2 3 4
do
        print "Motor $i operating"
        python3 motorControlNodeRed.py 0 $i 0.5
        sleep 1
done

print "test sequence for LED"
for i in 0 1 2 3
do
        print "LED array $i operating"
        sudo python3 neopixelControlNodeRed.py $i 5 0.2 test
done
print "script complete"
