from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from datetime import datetime

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
    #  PLOTTING GRAPHS 
    
    self.build_cars_make()
    self.build_cars_fuel()
    self.scatter_cars_fuel()
    self.priceCheck()
    self.most_sold()

     
  def build_cars_make(self):
    media_obj1 = anvil.server.call('plot_carsMake')
    self.image_1.source = media_obj1
    pass
    
  def build_cars_fuel(self):
    media_obj2 = anvil.server.call('plot_carsFuel')
    self.image_2.source = media_obj2
 
  def scatter_cars_fuel(self):
    media_obj3 = anvil.server.call('scatter_carsFuel')
    self.image_3.source = media_obj3

  def priceCheck(self):
    media_obj4 = anvil.server.call('price_check')
    self.image_4.source = media_obj4
    
  def most_sold(self):
    media_obj5 = anvil.server.call('mostSold')
    self.image_5.source = media_obj5
    
    # DEFINING 'CLICK' EVENT TO FIND VEHICLE BASED ON UI COMPONENTS (RADIOBUTTON, TEXTBOX)
  
  def button_1_click(self, **event_args):
    budget = self.budget.text
    length = self.carLength.text 
    hp = self.carHP.text
    
    rb1 = RadioButton(text="CNG", group_name="radioGroup1", value ="CNG")
    rb2 = RadioButton(text="CNG + Petrol", group_name="radioGroup1", value ="CNG + Petrol")
    rb3 = RadioButton(text="Diesel", group_name="radioGroup1", value ="Diesel")
    rb4 = RadioButton(text="Electric", group_name="radioGroup1", value ="Electric")
    rb5 = RadioButton(text="Hybrid", group_name="radioGroup1", value ="Hybrid")
    rb6 = RadioButton(text="Petrol", group_name="radioGroup1", value ="Petrol")
  
    
    rb1.selected =True
    rb2.selected =True
    rb3.selected =True
    rb4.selected =True
    rb5.selected =True
    rb6.selected =True
    
    if rb1.selected ==True:
      fuel = rb1.get_group_value()
    
    if rb2.selected ==True:
      fuel = rb2.get_group_value()
      
    if rb3.selected ==True:
      fuel = rb3.get_group_value()
      
    if rb4.selected ==True:
      fuel = rb4.get_group_value()
      
    if rb5.selected ==True:
      fuel = rb5.get_group_value()
      
    if rb6.selected ==True:
      fuel = rb6.get_group_value()
      
    findCar = anvil.server.call("exploreCar", budget, length, hp, fuel)
  
    if findCar:
      self.findCar_label.visible =True
      self.findCar_label.text ="Car is: "+str(findCar)
    
    
    
    
    

  



 







  

  


