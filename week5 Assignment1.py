class Smartphone:
    def __init__(self, brand, model, storage):
        self._brand = brand       # protected (encapsulation)
        self._model = model
        self._storage = storage
        self._battery = 100
        self._apps = []

    # Encapsulation with getters
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def install_app(self, app_name, size):
        if size > self._storage:
            return f"❌ Not enough storage for {app_name}."
        self._storage -= size
        self._apps.append(app_name)
        return f"✅ Installed {app_name}, {self._storage}GB left."

    # Polymorphic method
    def info(self):
        return (f"📱 Smartphone: {self._brand} {self._model}\n"
                f"Battery: {self._battery}% | Storage left: {self._storage}GB\n"
                f"Apps: {', '.join(self._apps) if self._apps else 'None'}")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # inherit Smartphone
        self.gpu = gpu

    # Polymorphism → override info()
    def info(self):
        return (f"🎮 Gaming Phone: {self._brand} {self._model}\n"
                f"GPU: {self.gpu} | Battery: {self._battery}%\n"
                f"Storage left: {self._storage}GB")

class BusinessPhone(Smartphone):
    def __init__(self, brand, model, storage, email_client):
        super().__init__(brand, model, storage)
        self.email_client = email_client

    # Polymorphism → override info()
    def info(self):
        return (f"💼 Business Phone: {self._brand} {self._model}\n"
                f"Email Client: {self.email_client}\n"
                f"Battery: {self._battery}% | Storage left: {self._storage}GB")


