#!/usr/bin/env python3

import ipdb

class CashRegister:

  def __init__( self, discount_value = 0 ):
    self.discount = discount_value
    self.total = 0
    self.items = []
    
    
  def add_item( self, item_string, price_float, quantity = 1 ):
    
    new_total = price_float * quantity
    self.last_transaction = new_total
    
    for i in range( quantity ):
      self.items.append( item_string )
    self.total += new_total
    
  def apply_discount( self ):
    if self.discount > 0:
      percent = self.discount / 100
      money_off = self.total * percent
      self.total = int( self.total - money_off )
      print( f"After the discount, the total comes to ${self.total}." )
    else:
      print( "There is no discount to apply." )
   

  def void_last_transaction( self ):
    self.total = self.total - self.last_transaction
  






c1 = CashRegister()

c1.add_item( "macbook air", 1000 )

c1.apply_discount()



