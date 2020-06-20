""" Spanish Inquisition Exception """


class SpanishInquisition(BaseException):
    """ Spanish Inquisition Exception """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = ("Nobody expected!",)


if __name__ == "__main__":

    try:
        raise SpanishInquisition()
    except Exception:  # pylint: disable=W0703
        pass
