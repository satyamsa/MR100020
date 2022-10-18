import pyvisa
import time

class Supply:
    def __init__(self, address):
        self.address = address
        rm = pyvisa.ResourceManager()
        self.supply = rm.open_resource(self.address)

    def set_voltage(self,voltage):
        self.supply.write("VOLT " + str(voltage))

    def set_current(self,current):
        self.supply.write("CURR " + str(current))

    def set_OVP(self,OVP):
        self.supply.write("VOLT:PROT {}".format(OVP))

    def set_OCP(self,OCP):
        self.supply.write("CURR:PROT {}".format(OCP))

    def reset(self):
        self.supply.write("*RST")

    def enable_out(self):
        self.supply.write("OUTP ON")

    def disable_out(self):
        self.supply.write("OUTP OFF")

    def MEASURE_OUT(self):
        self.supply.query("MEAS:CURR?")
        self.supply.query("MEAS:VOLT?")
        self.supply.query("MEAS:POW?")
        self.supply.query("VOLT:SLEW?")
        self.supply.query("CURR:SLEW?")

    def VOLT_SLEW(self,slew_rate):
        self.supply.write("VOLT:SLEW {}".format(slew_rate))

    def CURR_SLEW(self,slew_rate):
        self.supply.write("CURR:SLEW {}".format(slew_rate))

