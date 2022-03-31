#!/usr/bin/env python3

import math
import os
#Change directory
os.chdir('/Users/masha.lzs/Desktop')

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from numpy import array


#Open the csv
#library = pd.read_csv("Cello_lib.csv")

#Create tuples of inputs
input1 = (2, 7)
input2 = (1, 6.5)
input3 = (4.5, 10)
input4 = (3.3, 7.93)
input5 = (5.1, 15)

tuples = [input1, input2, input3, input4, input5]

#--------------------------------------------------------------------------------------------------------------------------------------
#create modification functions for gates
#stretch function
def stretch(part, minfactor = 0.5, maxfactor = 7):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]	
	ymin = library["Ymin"][index1] * minfactor
	ymax = library["Ymax"][index1] * maxfactor
	partname = library["Name"][index1] + "str"
	newpart = pd.DataFrame({"Name": [partname], "Ymax": [ymax],"Ymin": [ymin], "n" : [library["n"][index1]],"K": [ library["K"][index1]], "Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "was streched: new ymin = ", str(ymin), "new ymax = ", str(ymax))
	return data

#slope increase
def slopeincrease(part, slopefactor = 10):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]
	n = library["n"][index1] * slopefactor
	partname = library["Name"][index1] + "sli"
	newpart = pd.DataFrame({ "Name" : [partname], "Ymax": [library["Ymax"][index1]], "Ymin": [library["Ymin"][index1]], "n": [n] , "K": [library["K"][index1]], "Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its slope increased: new slope = ", str(n))
	return data


#slope decrease
def slopedecrease(part, slopefactor = 0.01):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]
	n = library["n"][index1] * slopefactor
	partname = library["Name"][index1] + "sld"
	newpart = pd.DataFrame({"Name": [partname], "Ymax": [library["Ymax"][index1]], "Ymin": [library["Ymin"][index1]], "n": [n], "K": [library["K"][index1]], "Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its slope decreased by a factor of", str(1/slopefactor), ". new slope = ", str(n))
	return data

#stronger promoter
def strongerpromoter(part):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]	
	ymin = library["Ymin"][index1] * 4
	ymax = library["Ymax"][index1] * 4
	partname = library["Name"][index1] + "spr"
	newpart = pd.DataFrame({"Name":[partname],"Ymax": [ymax],"Ymin": [ymin],"n": [library["n"][index1]],"K": [library["K"][index1]],"Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its promoter strength increased by 400%.")
	return data


#weaker promoter
def weakerpromoter(part):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]	
	ymin = library["Ymin"][index1] * 0.25
	ymax = library["Ymax"][index1] * 0.25
	partname = library["Name"][index1] + "wpr"
	newpart = pd.DataFrame({ "Name": [partname],"Ymax": [ymax], "Ymin": [ymin],"n": [library["n"][index1]],"K": [library["K"][index1]], "Type":[library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its promoter strength decreased by 400%.")
	return data

#strong RBS
def strongerRBS(part):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]	
	K = library["K"][index1] * 0.25
	partname = library["Name"][index1] + "srbs"
	newpart = pd.DataFrame({"Name": [partname], "Ymax": [library["Ymax"][index1]], "Ymin": [library["Ymin"][index1]], "n": [library["n"][index1]], "K": [K], "Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its RBS strength increased by 400%. The new value of K is ", str(K))
	return data

#weak RBS
def weakerRBS(part):
	data = library
	index1 = library.loc[library['Name'] == part].index[0]	
	K = library["K"][index1] * 4
	partname = library["Name"][index1] + "wrbs"
	newpart = pd.DataFrame({"Name": [partname], "Ymax": [library["Ymax"][index1]], "Ymin": [library["Ymin"][index1]], "n": [library["n"][index1]], "K": [K], "Type": [library["Type"][index1]]})
	data = pd.concat([data,newpart], ignore_index = True)
	print("Part", partname, "had its RBS strength decreased by 400%. The new value of K is ", str(K))
	return data

#--------------------------------------------------------------------------------------------------------------------------------------
#Create functions for gate connection that will calculate the output after each gate
	
#Create first connection - if NOR or NOT alone
def firstpart(g1, i1, i2=1):
	index1 = library.loc[library['Name'] == g1].index[0]
	if library["Type"][index1] == "NOT":
		y1 = [0]*2
		for x in range(0,2):
			y1[x] = library["Ymin"][index1] + (library["Ymax"][index1] - library["Ymin"][index1])/(1 + (i1[x]/library["K"][index1])**library["n"][index1])
		return y1
	else:
		inputs1 = [0]*4
		inputs2 = [0]*4
		y1 = [0]*4
		inputs1[0] = i1[0]+i2[0]
		inputs1[1] = i1[0]+i2[1]
		inputs1[2] = i1[1]+i2[0]
		inputs1[3] = i1[1]+i2[1]
		for x in range(0,4):
			y1[x] = library["Ymin"][index1] + (library["Ymax"][index1] - library["Ymin"][index1])/(1 + (inputs1[x]/library["K"][index1])**library["n"][index1])
		return y1

#create following connection to NOR or NOT
def partstogate(g, part1, part2=[1]):
	index1 = library.loc[library['Name'] == g].index[0]	
	if len(part2) == 1: #if accepting gate is NOT
		y1 = [0]*2
		if len(part1) == 2: #if input is NOT
			inputs = [0]*2
			inputs[1] = part1[0] #high output
			inputs[0] = part1[1] 
			for x in range(0,2):
				y1[x] = library["Ymin"][index1] + (library["Ymax"][index1] - library["Ymin"][index1])/(1 + (inputs[x]/library["K"][index1])**library["n"][index1])
			return y1
		else:
			inputs = [0]*2
			inputs[1] = part1[0] #high output
			inputs[0] = sum(part1[1:4])/3
			for x in range(0,2):
				y1[x] = library["Ymin"][index1] + (library["Ymax"][index1] - library["Ymin"][index1])/(1 + (inputs[x]/library["K"][index1])**library["n"][index1])
			return y1
	else: #if the accepting gate is NOR
		y1 =[0]*4
		if len(part1) == 4:
			inputs1 = [0]*2
			inputs1[0] = part1[0] #high output
			inputs1[1] = sum(part1[1:4])/3#low output
		else: 
			inputs1 = [0]*2
			inputs1 = part1
		if len(part2) == 4:
			inputs2 = [0]*2
			inputs2[0] = part2[0] #high output
			inputs2[1] = sum(part2[1:4])/3#low output
		else: 
			inputs2 = [0]*2
			inputs2 = part2
		i1 = [0]*4
		i1[3] = inputs1[0]+inputs2[0]
		i1[2] = inputs1[0]+inputs2[1]
		i1[1] = inputs1[1]+inputs2[0]
		i1[0] = inputs1[1]+inputs2[1]
		for x in range(0,4):
			y1[x] = library["Ymin"][index1] + (library["Ymax"][index1] - library["Ymin"][index1])/(1 + (i1[x]/library["K"][index1])**library["n"][index1])
		return y1

#function to calculate the score
def scorecalc(output):
	if len(output) == 2:
		score = math.log10(output[0]/output[1])
		print("The score is ", score)
		return score
	else:
		score = math.log10(output[0]/max(output[1:3]))
		print("The score is ", score)
		return score


#starting main
partsnor = np.zeros((20,4))
partsnot = np.zeros((20,2))
gates = [0]*20
gatesnor = [0]*20
gatesnot = [0]*20
scoresvec = [0]*5
runcount = 0
scoresvec = [0]*5
print("Welcome to GDSProg!")
lib = input("Please input your library: ")
library = pd.read_csv(lib)
while True:
	key = input("To start assembly press s, to modify existing gates press m: ")
	if key == 'm':
		print("Available modifications are: stretch, slopeincrease, slopedecrease, strongerpromoter, weakerpromoter, strongerRBS, weakerRBS ")
		action, p = input("Input function and gate name: ").split()
		choices = [stretch, slopeincrease, slopedecrease, strongerpromoter, weakerpromoter, strongerRBS, weakerRBS]
		choicesstr = ['stretch', 'slopeincrease', 'slopedecrease', 'strongerpromoter', 'weakerpromoter', 'strongerRBS', 'weakerRBS']
		loc = choicesstr.index(action)
		library = choices[loc](p)
	if key == 's':
		while True:
			countnor = 0
			countnot = 0
			runcount = runcount + 1
			num = input("How many gates do you start with? ")
			for x in range(0,int(num)):
				gate =  input("Please type your gate (NOR gates should go before NOT gates): ")
				gates[x] = gate
				ind = library.loc[library['Name'] == gates[x]].index[0]
				if (library['Type'][ind] == "NOR"):
					countnor = countnor + 1
				else:
					countnot = countnot + 1
			inor = np.zeros((countnor,2))
			for a in range(0, countnor):
				x,y =  input("Please type your inputs for NOR ").split()
				inor[a,0] = x
				inor[a,1] = y
			inot = np.zeros((countnot,1))
			for a in range(0, countnot):
				x =  input("Please type your inputs for NOT ")
				inot[a] = x
			for i in range(0, countnor):
				gatesnor[i] = gates[i]
			for i in range(countnor, (countnor + countnot)):
				gatesnot[i-countnor] = gates[i]
			print("Your working parts are NOR: ", gatesnor)
			print("                       NOT: ", gatesnot)
			for x in range(0,countnor):
				partsnor[x,:] = firstpart(gates[x], tuples[int(inor[x, 0])-1], tuples[int(inor[x, 1])-1])
			for x in range(countnor,(countnor+countnot)):
				partsnot[x-countnor,:] = firstpart(gates[x], tuples[int(inot[x-countnor])-1])
			while True:
				countfornor = 0
				a, act, b = input("Input gate connection ").split()
				if act == "to":
					ind = library.loc[library['Name'] == b].index[0]
					if (library['Type'][ind] == "NOR"):
						e = input("Gate needs second input, please type: ")
					if a in gatesnor:
						indxa = gatesnor.index(a)
						ainp = partsnor[indxa, :]
						gatesnor.pop(indxa)
						partsnor = np.delete(partsnor,indxa, axis=0)
					else:
						indxa = gatesnot.index(a)
						ainp = partsnot[indxa, :]
						gatesnot.pop(indxa)
						partsnot = np.delete(partsnot, indxa, axis=0)
					if (library['Type'][ind] == "NOR"):
						if e in gatesnor:
							indxe = gatesnor.index(e)
							einp = partsnor[indxe, :]
							gatesnor.pop(indxe)
							partsnor = np.delete(partsnor,indxe, axis=0)
						else:
							indxe = gatesnot.index(e)
							einp = partsnot[indxe, :]
							gatesnot.pop(indxe)
							partsnot = np.delete(partsnot,indxe, axis=0)
					if (library['Type'][ind] == "NOR"):
						out = partstogate(b, ainp, einp)
						norind = gatesnor.index(0)
						gatesnor[norind] = b
						partsnor[norind, :] = out
					else:
						out = partstogate(b, ainp)
						notind = gatesnot.index(0)
						gatesnot[notind] = b
						partsnot[notind, :] = out
					print("Your working parts are NOR: ", gatesnor)
					print("                       NOT: ", gatesnot)
					print("To finish type 'part score part' ")
				if act == "score":
					if a in gatesnor:
						indxa = gatesnor.index(a)
						ainp = partsnor[indxa, :]
						gatesnor.pop(indxa)
						partsnor = np.delete(partsnor,indxa, axis=0)
						score = scorecalc(ainp)
						scoresvec[runcount-1] = score
					else:
						indxa = gatesnot.index(a)
						ainp = partsnot[indxa, :]
						gatesnot.pop(indxa)
						partsnot = np.delete(partsnot, indxa, axis=0)
						score = scorecalc(ainp)
						scoresvec[runcount-1] = score
					break
			decision = input("Do you want to modify your parts or stop? (press m or s) ")
			if decision == "m":
				if runcount == 5:
					runs = array(range(runcount+1))
					X = runs[1:len(runs)]
					Y = scoresvec[0:runcount]
					plt.scatter(X,Y, s=100,c='magenta')
					plt.title('Too many cycles! Thank you for using GDSProg, here are your results')
					plt.xlabel('Cycle number')
					plt.ylabel('Gate Score')
					plt.xlim(0,5)
					plt.show()
					break
				num = input("How many gates would you like to modify? ")
				gts = [0]*int(num)
				for i in range(0, int(num)):
					gts[i] = input("Please input gate name ")
				choices = [stretch, slopeincrease, slopedecrease, strongerpromoter, weakerpromoter, strongerRBS, weakerRBS]
				for x in range(0,int(num)):
					choose = random.choice(choices)
					library = choose(gts[x])
				print("Modification completed!")
			if decision == "s":
				runs = array(range(runcount+1))
				X = runs[1:len(runs)]
				Y = scoresvec[0:runcount]
				plt.scatter(X,Y, s=100,c='magenta')
				plt.title('Thank you for using GDSProg, here are your results')
				plt.xlabel('Cycle number')
				plt.ylabel('Gate Score')
				plt.xlim(0,5)
				plt.show()
				quit()
				
				
				
			
			
	
			
				
			
				
			
			
			
		
			
			
			
			
			
	
		
			
			
				
			
			
	
	
	
	
	
	
			