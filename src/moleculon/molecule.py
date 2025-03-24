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