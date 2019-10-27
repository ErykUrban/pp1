wzrost = 170
cal = 2.54
stopa = 30.48
wzrost_stopa = wzrost//stopa
wzrost_cal = round((wzrost-(wzrost_stopa*stopa))/cal)
print("Mam " + str(wzrost) + "cm wzrostu, tj. " + str(wzrost_stopa) +" stóp i " +str(wzrost_cal) + " cali.")




