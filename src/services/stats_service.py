from scipy.stats import norm


class StatsService:
    """
    Luokka, joka vastaa StatsView:n tarjoamasta sovellukslogiikasta.
    """

    def __init__(self):
        """
        Luokan konstruktori, joka luo uuden StatsView:n
        tarjoamasta sovelluslogiikasta vastaavan olion.
        """

    def normal_cdf(self, point, mean, std):
        """
        Laskee normaalijakauman kertymäfunktion arvon.

        Args:
            x: Float-arvo, joka kuvaa normaalijakauman kohtaa.
            mean: Float-arvo, joka kuvaa normaalijakauman odotusarvoparametria.
            sd: Float-arvo, joka kuvaa normaalijakauman keskihajontaparametria.

        Returns:
            Palauttaa normaalijakauman N(mean, sd) kertymäfunktion arvon kohdassa x.
        """

        try:
            point = float(point)
            mean = float(mean)
            std = float(std)
        except ValueError:
            return False

        return round(norm.cdf(x=point, loc=mean, scale=std), 5)


stats_service = StatsService()
