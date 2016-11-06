#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
"""Week 11 2nd task"""

import time

class Snapshot(object):
    """Takes the snapshot of the time.

    Attributes:
        object: Returns the mixture of unix time.
    """

    def __init__(self):
        """This function builds the snapshot class.

        Args:
            
        Returns:
            object: Returns the mixture of unix time.
        Example:
            >>> mysnap = Snapshot()
            >>> hasattr(mysnap, 'created')
            True
        """
        self.created = time.time()
