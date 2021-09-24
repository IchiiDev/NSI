from balistique import projectile

trajectoire = projectile(45, 20, 0)

print(trajectoire.getDistance())
print(trajectoire.getFlightTime())
print(trajectoire.getMaxHeight())