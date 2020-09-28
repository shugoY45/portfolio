from setting import *
from normal import Normal
from special import Special
from rest import Rest
from classify import Classify


_ , SpShift = Special(Worker,SpecialJob)
# print(SpShift)

Worker2, RestShift = Rest(Worker,SpShift)
# print(Worker2)
# print(RestShift)

Worker3, _ = Special(Worker2,SpecialJob)
# print(Worker3)

NormalShift = Normal(Worker3,Job)
# print(NormalShift)

Shift = NormalShift + RestShift + SpShift
# print(Shift)

IndivShift = Classify(Shift,Worker)
print(IndivShift)

print(Hello)