#!/usr/bin/python
# nlantau, 2021-11-01

from datetime import date
period_is_late=lambda x,y,z:abs((x-y).days)>z
