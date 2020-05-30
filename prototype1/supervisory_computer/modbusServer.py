#!/usr/bin/env python3
"""
Pymodbus Synchronous Server
--------------------------------------------------------------------------

This synced server is implemented using TCP, with multiple slave contexts
"""
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_server(num_of_plcs):

    slaves = {}

    # ----------------------------------------------------------------------- #
    # Dynamically generates an address space starting from 0x01 for the
    # of PLCs that are passed. You can create your own address space, refer to
    # the pymodbus documentation, particularly the synchronous server example
    # ----------------------------------------------------------------------- #
    for num in range(1,num_of_plcs+1):
        address = "0x" + str(num)
        slaves.update({address: ModbusSlaveContext(hr=ModbusSequentialDataBlock(0,[5]*10))})



    context = ModbusServerContext(slaves=slaves, single=False)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- #
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '2.3.0'

    # ----------------------------------------------------------------------- #
    # run the server
    # ----------------------------------------------------------------------- #
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()
