#!/usr/bin/env python3
import re 
class MyString:
  def __init__(self,value=""):
    self._value=value
  @property
  def value(self):
      return self._value
  @value.setter
  def value (self,new_value):
      if not isinstance(new_value,str):
          print("The value must be a string.")
      self._value= new_value

    # (pass)
  def is_sentence(self):
      return self.value.endswith(".")
  
  def is_question(self):
      return self.value.endswith("?")
  
  def is_exclamation(self):
      return self.value.endswith("!")
  
  def count_sentences(self):
      if not self.value:
          return 0
      sentences= re.split(r'[.!?]',self.value)
      sentences = [s.strip() for s in sentences if s.strip()]
      
      return len(sentences)
      
string=MyString('THIS IS A SENTENCE.It has three!')
print(string.count_sentences())
    
# string=MyString()
# string.value="Hello"
# print(string.value)