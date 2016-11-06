#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 1st task"""

import produce

TOMATO = produce.Produce()
TOMATO_ARRIVAL = TOMATO.arrival

EGGPLANT = produce.Produce(1311210802)
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
