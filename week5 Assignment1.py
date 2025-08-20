class Smartphone:
    def __init__(self, Brand, Model, Storage):
        self.Brand = Brand
        self.Model = Model
        self.Storage = Storage #in GB
        self.Battery = 100
        self.apps = []

    def Install_App(self, app_name, size):
     if size > self.storage:
        return f"The {app_name} size has larger size than the phone's storage"
     self.Storage -= size
     self.apps.append(app_name)

    def play_media(self, minutes):
     if self.Battery <=5:
        return "Battery too low, cannot PLay the media"
     else:
        drain = min(self.Battery, minutes)
        return "Playing Media...."
    
    def charge(self, amount):
     self.Battery = min(100, self.Battery + amount)
     return f"Charging....Battery at {self.Battery}"
    
    def info(self):
     return  (f"{self.Brand} {self.Model}\n"
            f"Battery:{self.Battery}%\n"
            f"Storage:{self.Storage}GB free\n"
            f"Apps:{','.join(self.apps) if self.apps else "No apps Installed."}")
    
phone = Smartphone("Samsung", "A04E", 256)
print(phone.info())
print (phone.charge(23))
print(phone.play_media(20))
