def count_all(text):
    count = 0
    d ={}
    
  for c in text:
      if c == " ":
        c = "space"

      if c in d:
        d[c] = d[c]+1

      else:
        d[c] = 1
  for k in sorted(d):
      print (k +":" +str(d[k]))
  return d

def main():
  text = input("enter your text:  ")
  count_all(text)

main()
