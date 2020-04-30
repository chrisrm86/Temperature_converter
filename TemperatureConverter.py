#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       Temperature Converter
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
from tkinter import *
from tkinter.messagebox import *

class TemperatureConverter():
	def __init__(self, parent=None):

		self.frame = parent
		self.frame.geometry("320x155")
		self.frame.resizable(False, False)
		self.frame.title("Temperature Converter")
		self.frame.iconbitmap('icon.ico')

		self.principalContainer = Frame(self.frame, bg="LightGray")
		self.principalContainer.pack(expand=YES, fill=BOTH)

		self.inputContainer = Frame(self.principalContainer, height=40, width=40, bg="orange")
		self.inputContainer.pack(side=TOP, expand=NO, fill=X)

		text1 = Label(self.inputContainer, text="Enter a value:", bg="orange", fg="white", padx=20).pack(side=LEFT)
		
		self.buttonsContainer = Frame(self.principalContainer, bg="LightGray", height=50)
		self.buttonsContainer.pack(expand=NO, fill=BOTH)

		self.resultsContainer = Frame(self.principalContainer, height=100)
		self.resultsContainer.pack(side=BOTTOM, expand=NO, fill=BOTH)

		text2 = Label(self.resultsContainer, text="RESULT:", width=10).pack(side=LEFT, padx=20)

		inputDataSTR=str()
		inputTempData=IntVar()

		inputDataSection = Entry(self.inputContainer, width=50, textvariable=inputDataSTR)
		inputDataSection.pack(side=RIGHT, padx=20)

		displayResults = Label(self.resultsContainer, text=" ", width=100)
		displayResults.pack(side=RIGHT, padx=10)
		
		def convert():
			try:
				temperature=float(inputDataSection.get())
				selectOption=inputTempData.get()
				if selectOption==1:
					inputDataSTR = (temperature-32)*5/9
				else:
					inputDataSTR= temperature*1.8+32
				displayResults.config(text=str(inputDataSTR))
			except ValueError:
				self.popup_window()

		btn1 = Radiobutton(self.buttonsContainer, text="Fahrenheit to Celsius", variable=inputTempData, value=1, indicatoron=0)
		btn1.pack(side=RIGHT, padx=5, pady=40)

		btn2 = Radiobutton(self.buttonsContainer, text="Celsius to Fahrenheit", variable=inputTempData, value=2, indicatoron=0)
		btn2.pack(side=LEFT, padx=5, pady=40)
		btn3 = Button(self.buttonsContainer, text="Convert", width=50, command=convert).pack(side=BOTTOM)

		btn2.select()

	def popup_window(self):
		showinfo(title="Error", message="Enter value")

if __name__=='__main__':
	root = Tk()
	TemperatureConverter(root)
	root.mainloop()