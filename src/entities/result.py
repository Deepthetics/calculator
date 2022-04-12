from multiprocessing.sharedctypes import Value


class Result:
    """Luokka, joka kuvaa yksittäistä laskettua tulosta.

    Attributes:
        value: Float-arvo, joka kuvaa tuloksen arvoa.
        id: Merkkijonoarvo, joka määrittää tuloksen tunnisteen.
        description: Merkkijonoarvo, joka kuvaa, mihin laskuun tulos liittyy.
    """

    def __init__(self, value, id="", description=""):
        """Luokan konstruktori, joka luo uuden tulosta kuvaavan olion.

        Args:
            value: Float-arvo, joka kuvaa tuloksen arvoa.
            id:
                Vapaaehtoinen, oletusarvoltaan "".
                Merkkijonoarvo, joka määrittää tuloksen tunnisteen.
            description:
                Vapaaehtoinen, oletusarvoltaan "".
                Merkkijonoarvo, joka kuvaa, mihin laskuun tulos liittyy.    
        """

        self.value = value
        self.id = id
        self.description = description
