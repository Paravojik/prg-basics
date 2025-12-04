import tv
tv1=tv.TV()
tv1.show_status()

tv1.turn_on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery'])
tv1.show_channels()
tv1.set_channel(5)

tv1.set_channels(['channel1'])
tv1.show_channels()
tv1.show_status()
tv1.set_channel(3)
tv1.show_status()
tv1.decrease_volume()
tv1.show_status()
tv1.increase_volume()
tv1.increase_volume()
tv1.increase_volume()
tv1.increase_volume()
tv1.show_status()


tv1.turn_off()
tv1.show_status()