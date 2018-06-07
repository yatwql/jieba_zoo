import nltk
from nltk import CFG
toy_grammer = nltk.CFG.fromstring(
"""
  S -> NP VP
  VP -> V NP
  V -> "eats" | "drinks"
  NP -> Det N
  Det -> "a" | "an" | "the"
  N -> "presentent" | "Obama" | "apple" | "coke"
  """)    
toy_grammer.productions()