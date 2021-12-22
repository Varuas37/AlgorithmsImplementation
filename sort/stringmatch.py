def BruteForceStringMatch(Text,Pattern):
  print('_______________')
  print('STRING MATCH')
  print('_______________')
  lengthOfText = len(Text)
  lengthOfPattern = len(Pattern)
  count = 0
  for i in range(lengthOfText-lengthOfPattern+1):
    j=0
    count=count+1
    while j<lengthOfPattern and Pattern[j] == Text[i+j]:
      count=count+1
      j = j+1
      if j == lengthOfPattern: 
        return {'startingIndex: ':i,'totalComparisions: ':count-1}
  return -1

