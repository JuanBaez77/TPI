import csv
from tkinter import *
from tkinter import messagebox

class Raza:
    def __init__(self, raza, estado):
        self.__raza = raza.lower()
        self.__estado = estado
        
    # Getters
    def get_raza(self):
        return self.__raza
    
    def get_estado(self):
        return self.__estado
    
    # Setters
    def set_raza(self, raza):
        self.__raza = raza 
        
    def set_estado(self, estado):
        self.__estado = estado   
        
    def __str__(self):
        return self.__raza
    
    def __repr__(self):
        return self.__raza