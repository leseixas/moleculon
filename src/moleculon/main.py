import numpy as np
import pandas as pd
from scipy.spatial import rotation
from scipy.spatial import distance

class Particle:
    def __init__(self, element, position, velocity, force, charge, dipole):
        """
        Initialize a new instance of the class.

        Parameters:
        element (str): The chemical element.
        position (tuple): The position of the element in 3D space (x, y, z).
        velocity (tuple): The velocity of the element in 3D space (vx, vy, vz).
        force (tuple): The force acting on the element in 3D space (fx, fy, fz).
        charge (float): The electric charge of the element.
        dipole (tuple): The dipole moment of the element in 3D space (dx, dy, dz).
        """
        self.element = element
        self.position = position
        self.velocity = velocity
        self.force = force
        self.charge = charge
        self.dipole = dipole

    def shift(self, shift):
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
    

def Molecule(Particle):
    def __init__(self, particles):
        """
        Initializes the object with a list of particles.

        Args:
            particles (list): A list of particles to be initialized.
        """
        self.particles = particles

    def shift(self, shift):
        for particle in self.particles:
            particle.shift(shift)

    def rotate(self, rotation_matrix):
        for particle in self.particles:
            particle.rotate(rotation_matrix)

    def __str__(self):
        return "\n".join([str(particle) for particle in self.particles])