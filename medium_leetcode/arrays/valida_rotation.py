def valid_rotate(s1,s2):
  c=s1+s1
  for i in range(len(s1)):
    if c[i:i+len(s1)]==s2:
      return True
  return False
