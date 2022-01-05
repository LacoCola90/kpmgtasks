'''
In this problem, your input is a list of integers, which represents the layout of a 3D structure, cubes arranged into towers in a row.
The first number is the height of the first tower, the second is the height of the second and so on.
The function has to calculate the surface area of the structure (we suppose the surface area of a single cube is 6 unit).
If the input starts as [2, 1], then the first tower connects with the second one in 1 level, which means the surface area is 14 units.
'''


def solution(nums):
    nums=nums+[0]

    surfacearea=0
    prevtower=0

    for tower in nums:
        if tower>0:
            surfacearea += tower*2+2+abs(prevtower-tower)
        else:
            surfacearea += abs(prevtower-tower)

        prevtower=tower

    return surfacearea

print(solution([7,4,5,2])) #res=60
print(solution([2,1])) #res=14
