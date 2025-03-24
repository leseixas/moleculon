import numpy as np
import pandas as pd
import scipy as sp

class Particle:
    def __init__(self, element, position: np.ndarray,
                 velocity: np.ndarray, force: np.ndarray, charge: float,
                 electric_dipole: np.ndarray, magnetic_dipole: np.ndarray):
        self.element = element
        self.position = position
        self.velocity = velocity
        self.force = force
        self.charge = charge
        self.electric_dipole = electric_dipole
        self.magnetic_dipole = magnetic_dipole


    def shift(self, shift: np.ndarray):
        """
        Shifts the position by a given value.

        Parameters:
        shift (int or float): The value by which to shift the position.
        """
        self.position += shift
    

    def rotate(self, rotation_matrix):
        """
        Rotate the position, velocity, force, and dipole of the object using the given rotation matrix.

        Parameters:
        rotation_matrix (numpy.ndarray): A 3x3 matrix used to rotate the object's attributes.

        Returns:
        None
        """
        self.position = np.dot(rotation_matrix, self.position)
        self.velocity = np.dot(rotation_matrix, self.velocity)
        self.force = np.dot(rotation_matrix, self.force)
        self.dipole = np.dot(rotation_matrix, self.dipole)


    def __str__(self):
        return f"Element: {self.element}\nPosition: {self.position}\nVelocity: {self.velocity}\nForce: {self.force}\nCharge: {self.charge}\nDipole: {self.dipole}"
    
