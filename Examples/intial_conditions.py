import numpy as np

class Planets:

    def __init__(self):
        self.X = []
        self.Y = []
        self.Z = []
        self.Mass = []
        self.Vx = []
        self.Vy = []
        self.Vz = []
        self.G = 6.67430E-11
        self.Mass = []

    def add_star(self,Mass):
        self.Mass.append(Mass)
        self.X.append(0)
        self.Y.append(0)
        self.Z.append(0)
        self.Vx.append(0)
        self.Vy.append(0)
        self.Vz.append(0)


    def add_planet(self,Mass,Oribital_radius,eccentricity=0,inclination=0):

        # turn the orbital semi-major axis into a x,y,z position, assume we are on the x-y plane
        self.X.append(Oribital_radius)
        self.Y.append(0)
        self.Z.append(0)

        # using star mass self.mass[0] and the orbital radius we can calculate the orbital velocity
        # v = sqrt(GM/r)
        self.Vx.append(0)
        self.Vy.append(np.sqrt(self.G*self.Mass[0]/Oribital_radius))
        self.Vz.append(0)
        self.Mass.append(Mass)
        # account for the center of mass
        comX, comY, comZ = self.center_of_mass()
        self.X = [x - comX for x in self.X]
        self.Y = [y - comY for y in self.Y]
        self.Z = [z - comZ for z in self.Z]
        

    def center_of_mass(self):
        total_mass = sum(self.Mass)
        center_of_mass_x = sum([self.X[i]*self.Mass[i] for i in range(len(self.Mass))]) / total_mass
        center_of_mass_y = sum([self.Y[i]*self.Mass[i] for i in range(len(self.Mass))]) / total_mass
        center_of_mass_z = sum([self.Z[i]*self.Mass[i] for i in range(len(self.Mass))]) / total_mass

        return center_of_mass_x, center_of_mass_y, center_of_mass_z
    


class Galaxy:
    """

    Class to create the initial conditions of a galaxy.

    """

    def __init__(self, N, R, z, sigma_R, sigma_z, bluge_height, bludge_frac,Msol = 2E30,G = 6.67430e-11):
        """
        Parameters
        ----------
        N : int
            Number of particles in the disc.
        R : float
            Radius of the disc.
        z : float
            Height of the disc.
        sigma_R : float
            Standard deviation of the radial distribution.
        sigma_z : float
            Standard deviation of the vertical distribution.
        M : float
            Mass of the galaxy.
        G : float
            Gravitational constant.
        """
        self.N = N
        self.R = R
        self.z = z
        self.sigma_R = sigma_R
        self.sigma_z = sigma_z
        self.Msol = Msol
        self.G = G
        self.bluge_height = bluge_height
        self.Nbluge = int(N*bludge_frac)
        self.Ndisc = N - self.Nbluge

        self.X = []
        self.Y = []
        self.Z = []
        self.Mass = []
        self.Vx = []
        self.Vy = []
        self.Vz = []

        self.add_black_hole()
        self.create_bluge()
        self.create_disc()
        self.assign_star_mass()
        self.assign_velocity(1000)



    def create_bluge(self):
        """
        Create the bluge of the galaxy.
        """

        # sphere of radius R with random distribution of particles
        for i in range(self.Nbluge):
            r = np.random.normal(0, self.bluge_height)
            phi = np.random.uniform(0, 2*np.pi)
            x = r * np.cos(phi)
            y = r * np.sin(phi)
            z = np.random.normal(0, self.sigma_z)
            self.X.append(x)
            self.Y.append(y)
            self.Z.append(z)

    def create_disc(self):
        """
        Create the disc of the galaxy.
        """
        # a thin disc of radius R and thickness sigma_R
        # Generate random positions within the disc
        r = self.R * np.sqrt(np.random.uniform(0, 1, ))
        theta = np.random.uniform(0, 2 * np.pi, self.Ndisc)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        # Generate random heights within the thickness
        z = np.random.uniform(-self.sigma_R/2, self.sigma_R/2, self.Ndisc)

        # Combine the coordinates into a single array
        particle_positions = np.column_stack((x, y, z))

        return particle_positions

    def add_black_hole(self):
        """
        Add a black hole to the galaxy.
        """
        # place a black hole at the center of the galaxy
        self.X.append(0)
        self.Y.append(0)
        self.Z.append(0)
        self.Mass.append(1E6*self.Msol)
        self.Vx.append(0)
        self.Vy.append(0)
        self.Vz.append(0)

    def assign_star_mass(self, IMF='kroupa'):
        """
        Assign a mass to each star in the galaxy.
        """
        if IMF == 'kroupa':

            # assign masses to the stars randomly from a Kroupa initial mass function
            for i in range(self.N):
                r = np.random.uniform(0, 1)
                if r < 0.08:
                    mass = np.random.uniform(0.08, 0.5)
                elif r < 0.5:
                    mass = np.random.uniform(0.5, 1)
                else:
                    mass = np.random.uniform(1, 150)
                self.Mass.append(mass*self.Msol)

    def assign_velocity(self, v):
        """
        Assign a velocity to each star in the galaxy.
        """
        for i in range(self.N):
            if i  == 0:
                self.Vx.append(0)
                self.Vy.append(0)
                self.Vz.append(0)
            vx = np.random.normal(0, v)
            vy = np.random.normal(0, v)
            vz = np.random.normal(0, v)
            self.Vx.append(vx)
            self.Vy.append(vy)
            self.Vz.append(vz)
