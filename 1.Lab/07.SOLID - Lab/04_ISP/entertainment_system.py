class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device):
        pass

    def connect_to_device_via_rca_cable(self, device):
        pass

    def connect_to_device_via_ethernet_cable(self, device):
        pass

    def connect_device_to_power_outlet(self, device):
        pass


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self, power_outlet):
        self.connect_device_to_power_outlet(power_outlet)


class DVDPlayer(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self, power_outlet):
        self.connect_device_to_power_outlet(power_outlet)


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self, power_outlet):
        self.connect_device_to_power_outlet(power_outlet)


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_ethernet_cable(dvd_player)

    def plug_in_power(self, power_outlet):
        self.connect_device_to_power_outlet(power_outlet)
