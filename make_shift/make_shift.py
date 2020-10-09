# from setting import *
# from function import Set_list, Classify
# from normal import Normal
# from special import Special
# from rest import Rest



# IndivShift = Set_list(Worker)

# _ , SpShift = Special(Worker,SpecialJob)
# # print(SpShift)

# Worker2, RestShift = Rest(Worker,SpShift)
# # print(Worker2)
# # print(RestShift)

# Shift = RestShift + SpShift
# IndivShift = Classify(Shift,IndivShift)


# Worker3, _ = Special(Worker2,SpecialJob)
# # print(Worker3)

# NormalShift = Normal(Worker3,Job,IndivShift)
# # print(NormalShift)

# Shift = NormalShift
# # Shift = NormalShift + RestShift + SpShift

# # print(Shift)

# # IndivShift = Classify(Shift,Worker)
# # IndivShift = Classify(Shift,IndivShift)
# ViewIndiv = []
# for indiv in IndivShift:
#   tmp = []
#   for ind in indiv:
#     tmp.append(ind[0])
#   ViewIndiv.append(tmp)
  

# print(ViewIndiv)