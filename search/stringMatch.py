
def string_match(string, sub_str): 
 #  Brute force string matching  
 
 for i in range(len(string)-len(sub_str)+1): 
  index = i  # index Point to the 1 Three characters to be compared  
  for j in range(len(sub_str)): 
   if string[index] == sub_str[j]:
    
    index += 1 
   else: 
    break 
   if index-i == len(sub_str): 
    return i 
  
 return -1 


__author__ = 'Wang' 
from collections import defaultdict 
def shift_table(pattern): 
 #  generate  Horspool  Algorithm's moving table  
 #  The current detection character is c , the mode length is m 
 #  If the current c Not included before the pattern m-1 In characters, the length of the move mode m 
 #  In other cases move the one on the far right c To the end of the pattern 1 The distance between two characters  
 table = defaultdict(lambda: len(pattern)) 
 for index in range(0, len(pattern)-1): 
  table[pattern[index]] = len(pattern) - 1 - index 
 return table 
def horspool_match(pattern, text): 
 #  implementation  horspool  String matching algorithm  
 #  Match successful, return pattern in text At the beginning of; Otherwise returns  -1 
 table = shift_table(pattern) 
 index = len(pattern) - 1 
 while index <= len(text) - 1: 
  print("start matching at", index) 
  match_count = 0 
  while match_count < len(pattern) and pattern[len(pattern)-1-match_count] == text[index-match_count]: 
   match_count += 1 
  if match_count == len(pattern): 
   return index-match_count+1 
  else: 
   index += table[text[index]] 
 return -1 

if __name__ == "__main__": 
#  print(string_match("123456", "56")) 
 print(horspool_match("001", "0000000000")) 


