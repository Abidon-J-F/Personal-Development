""" 
This is a Sandwiches Functions program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

import sandwiches_Func

sandwiches_Func.make_sandwiches('lettuce')
sandwiches_Func.make_sandwiches('lettuce', 'pepperoni', 'chicken strips')
sandwiches_Func.make_sandwiches('lettuce', 'cheese')

##
from sandwiches_Func import make_sandwiches
make_sandwiches('lettuce')
make_sandwiches('lettuce', 'pepperoni', 'chicken strips')
make_sandwiches('lettuce', 'cheese')

##
from sandwiches_Func import make_sandwiches as ms
ms('lettuce')
ms('lettuce', 'pepperoni', 'chicken strips')
ms('lettuce', 'cheese')

##
import sandwiches_Func as s

s.make_sandwiches('lettuce')
s.make_sandwiches('lettuce', 'pepperoni', 'chicken strips')
s.make_sandwiches('lettuce', 'cheese')

##
from sandwiches_Func import *

make_sandwiches('lettuce')
make_sandwiches('lettuce', 'pepperoni', 'chicken strips')
make_sandwiches('lettuce', 'cheese')