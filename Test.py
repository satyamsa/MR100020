from Supply import Supply

bk_supply = Supply('address')
print(bk_supply.address)
bk_supply.reset()
bk_supply.disable_out()
bk_supply.set_voltage(20)
bk_supply.set_current(5)
bk_supply.enable_out()
bk_supply.MEASURE_OUT()

