""" 
This is a Seeing The World program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 02/2022 - 03/2022
"""

from audioop import reverse


like_to_visit = ['texas', 'california', 'paris', 'rome', 'madrid']
print(like_to_visit)
print(sorted(like_to_visit))
print(like_to_visit)

print(sorted(like_to_visit, reverse=True))
print(like_to_visit)

like_to_visit.reverse()
print(like_to_visit)

like_to_visit.reverse()
print(like_to_visit)

like_to_visit.sort()
print(like_to_visit)

like_to_visit.sort(reverse=True)
print(like_to_visit)