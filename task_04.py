#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 task 04."""

import car


class CustomCar(car.Car):
    """Using subclassing to demonstrate both the has-a and is-a concepts.

        Attributes:
            car.Car: Child class costructor.
    """
    def __init__(self, color='red', tires=None):
        """CustomCar() class constructor.

        Args:
            color (string): Cars color. Defaults = 'red'.
            tires (list): A list of CustomTire() objects. Defaults = None.

        Returns:
            Returns the color of the car which is red.

        Examples:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
        """
        car.Car.__init__(self, color)
        if tires is None:
            self.tires = []
            list_of_tires = ['a', 'b', 'c', 'd']
            for each in list_of_tires:
                each = CustomTire()
                self.tires.append(each)
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """Using subclassing to demonstrate both the has-a and is-a conceptscar.

        Attributes:
            car.Tire: Child class costructor.
    """
    def __init__(self, miles=0):
        """Constructor for the CustomTire() class.

        Args:
            miles (int): The number of miles on the CustomTire. Defaults to 0.

        Returns:
            Total miles.

        Examples:
            >>> isinstance(mycar.tires[0], CustomTire)
            True
        """
        car.Tire.__init__(self, miles)
        self.__maximum_miles = 500
