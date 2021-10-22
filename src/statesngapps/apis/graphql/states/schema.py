from django.utils.translation import gettext_lazy as _

from .queries.city import CityQuery
from .queries.district import DistrictQuery
from .queries.lga import LGAQuery
from .queries.state import StateQuery, GovernorQuery


class StatesRootQueries(CityQuery, DistrictQuery, GovernorQuery, LGAQuery, StateQuery):
    class Meta:
        description = _('StatesNG Root State Queries')
