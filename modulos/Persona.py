import csv
from tkinter import *
from tkinter import messagebox
from Modulos.Mascota import Mascota
class Persona:
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__telefono = telefono
        self.__tipoPersona = tipoPersona
        self.__estado = estado

    # Getters y Setters
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getTipoDocumento(self):
        return self.__tipoDocumento
    def setTipoDocumento(self, tipoDocumento):
        self.__tipoDocumento = tipoDocumento

    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento = documento

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getTipoPersona(self):
        return self.__tipoPersona
    def setTipoPersona(self, tipoPersona):
        self.__tipoPersona = tipoPersona

    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        self.__estado = estado


    def __str__(self):
        return f"{self.__nombre} {self.__apellido}, {self.__tipoDocumento}: {self.__documento}, Tel: {self.__telefono}, Tipo: {self.__tipoPersona}, Estado: {self.__estado}"

class Cliente(Persona):
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado, mascota):
        super().__init__(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)
        self.__mascota = mascota

        #getters y setters
        def getMascota(self):
            return self.__mascota
        def setMascota(self,mascota):
            self.__mascota = mascota
            return f"{super().__str__(), Mascota: {self.__mascota}}"
class Empleado:
    def __init__(self, nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado):
        super().__init__(nombre, apellido, tipoDocumento, documento, telefono, tipoPersona, estado)