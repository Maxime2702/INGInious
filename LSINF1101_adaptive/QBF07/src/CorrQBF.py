#!/usr/bin/python3
# -*- coding: utf-8 -*-


def counts(words):
  freqs = {}
  for word in words:
    freqs[word] = freqs.get(word, 0) + 1
  return freqs
  
def topk(tuples,k):
  sorted_tuples = sorted(tuples,reverse=True)
  
  result = sorted_tuples[0:k]
  
  k2 = k
  while k2 < len(sorted_tuples) and sorted_tuples[k2][0] == sorted_tuples[k-1][0]:
    result.append ( sorted_tuples[k2] )
    k2 += 1
  
  return result

def topk_words ( words, k ):
  freqs = counts(words)

  tuples = []
  for word, count in freqs.items ():
    tuples.append ( (count,word) )
    
  return topk(tuples,k)
