def CalProm(n1:float, n2:float, n3:float)->float:
  if n1>n2:
      if n2>n3:
        Promedi = (n1+n2)/2
      else:
        Promedi = (n1+n3)/2
  else:
      if n1>n3:
        Promedi = (n2+n1)/2
      else:
        Promedi = (n2+n3)/2
  return Promedi
