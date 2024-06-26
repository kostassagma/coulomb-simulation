from vector import Vector
from constants import K, dt
from state import particles, E, B


class Particle:
    def __init__(self, mass: float, charge: float, pos: Vector, velocity=Vector(0, 0)) -> None:
        self.mass = mass
        self.charge = charge
        self.pos = pos
        self.velocity = velocity
        # particles.append(self)

    def force(self, q):
        r = Vector(self.pos.x-q.pos.x, self.pos.y-q.pos.y)
        # print(r)
        return r*((K*self.charge*q.charge)/(abs(r))**3)

    global particles

    def forces_of_particles(self, iteration=0):
        if iteration >= len(particles):
            return Vector(0, 0)
        if particles[iteration] is self:
            return self.forces_of_particles(iteration=iteration+1)
        return self.force(particles[iteration]) + self.forces_of_particles(iteration=iteration+1)

    def forces_of_e_field(self):
        return E*self.charge

    def forces_of_m_field(self):
        return (self.velocity.cross_product(B))*self.charge

    def sigma_forces(self):
        return self.forces_of_particles() + self.forces_of_e_field() + self.forces_of_m_field()

    def acceleration(self):
        return self.sigma_forces()*(1/self.mass)

    def move(self):
        self.velocity = self.velocity + self.acceleration()*dt
        self.pos = self.pos + self.velocity*dt
        # print(particles[0].velocity.x)
