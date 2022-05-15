class Result:
    """Luokka, joka kuvaa yksittäistä laskettua tulosta.

    Attributes:
        value: Float-arvo, joka kuvaa tuloksen arvoa.
    """

    def __init__(self, value, index=None):
        """Luokan konstruktori, joka luo uuden tulosta kuvaavan olion.

        Args:
            value: Float-arvo, joka kuvaa tuloksen arvoa.
        """

        self.value = value
        self.index = index
        
