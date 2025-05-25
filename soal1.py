def test_tuple(ta):
  if ta[0] == ta[1] == ta[2] == ta[3]: #ini untuk ngecek apakah semua elemen tuple sama
    return True # jika iya, return True
  else:
    return False # jika tidak, return False



#ini testcase nya bg
tx= (90, 90, 90, 90)
td= (90, 90, 91, 90)

print (test_tuple(tx))
print (test_tuple(td))
