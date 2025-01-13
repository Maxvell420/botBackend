def prov(func):
    res = func()

    def change():
        return {"1": "2"}

    return change
