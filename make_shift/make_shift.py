from setting import *
from set_list import Set_list
from normal import Normal
from special import Special
from rest import Rest
from classify import Classify


IndivShift = Set_list(Worker)

_ , SpShift = Special(Worker,SpecialJob)
# print(SpShift)

Worker2, RestShift = Rest(Worker,SpShift)
# print(Worker2)
# print(RestShift)

Shift = RestShift + SpShift
IndivShift = Classify(Shift,IndivShift)


Worker3, _ = Special(Worker2,SpecialJob)
# print(Worker3)

NormalShift = Normal(Worker3,Job,IndivShift)
# print(NormalShift)

Shift = NormalShift
# Shift = NormalShift + RestShift + SpShift

# print(Shift)

# IndivShift = Classify(Shift,Worker)
IndivShift = Classify(Shift,IndivShift)
print(IndivShift)