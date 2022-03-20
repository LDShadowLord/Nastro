class PositiveError:
    def __init__(self, text="[INFO]",code,display)
        __prefix__ = ">"
        __text__ = text
        __code__ = code
        display = display
        return __text__+" "+__prefix__+__code__+" "+display

class NegativeError:
    def __init__(self, text="[ERROR]",code,display)
        __prefix__ = "<"
        __text__ = text
        __code__ = code
        display = display
        return __text__+" "+__prefix__+__code__+" "+display

def Error000001():
    return NegativeError(
        code="000001",
        display="You must wipe down the database first by using the '-delete_db' command.")