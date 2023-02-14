class GPDriver:
    def __new__(cls):
        if not hasattr(cls, "_instacne"):
            cls._instance = super().__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        pass