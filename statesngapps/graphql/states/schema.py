from .queries.city import CityQuery
from .queries.lga import LGAQuery
from .queries.state import StateQuery, GovernorQuery


class StatesRootQueries(CityQuery, GovernorQuery, LGAQuery, StateQuery):
    pass
