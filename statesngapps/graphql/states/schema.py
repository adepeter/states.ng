from .queries.city import CityQuery
from .queries.lga import LGAQuery
from .queries.state import StateQuery


class StatesRootQueries(CityQuery, LGAQuery, StateQuery):
    pass
