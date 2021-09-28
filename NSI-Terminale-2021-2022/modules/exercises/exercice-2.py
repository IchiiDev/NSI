from balistique import projectile

trajectoire = projectile(65, 13, 2)

print(trajectoire.getDistance())
print(trajectoire.getFlightTime())
print(trajectoire.getMaxHeight())
print(trajectoire.getY(10))
trajectoire.tracerTrajectoire(15, 20)
trajectoire.animerTrajectoire(15, 20, 20)