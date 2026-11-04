def equilateral(sides):
    return sides[0] == sides[1] == sides[2] > 0


def isosceles(sides):
    return (
        (sorted(sides)[0] == sorted(sides)[1] 
      or sorted(sides)[1] == sorted(sides)[2])
     and sorted(sides)[0] + sorted(sides)[1] > sorted(sides)[2]
    )


def scalene(sides):
    return (
        sorted(sides)[0] < sorted(sides)[1] < sorted(sides)[2]
    and sorted(sides)[0] + sorted(sides)[1] > sorted(sides)[2]
    )
