def sms_break(S, maxlen):
  S = S.split()
  mdSize = 5

  ans = []
  curStr = ""
  curLen = 0
  for word in S:
    wordLen = len(word)
    if curLen + wordLen + 1 < maxlen - mdSize:
      curStr += (word + " ")
      curLen += (wordLen + 1)
    elif wordLen + 1 > maxlen - mdSize:
      ptr = 0
      while wordLen > 0:
        curStr += word[ptr:(ptr+maxlen-mdSize)]
        ptr += maxlen - mdSize
        wordLen -= ptr

    ans.append("{} ({}/{})".format())
