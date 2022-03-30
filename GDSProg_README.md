README

Welcome to Genetic Design Scoring Program! (GDSProg)

Program Overview: This program is designed to input a design of gates based on specific parts, score the final output response function, and allow for modification(or replacement) of individual parts to increase/decrease  this score. The program then plots the scores as a function of iteration cycle. 

REQUIREMENTS: Input Library of csv file of parts with format: [Name, Ymax, Ymin, n, k, Type] where Name and Type are strings, and Ymax, Ymin, n, and k are float variables. Type can be either “NOR” or “NOT.” 

Main Functions Overview:
Firstpart: Input gate name from data structure; input name of starting input tuples (input1 to input5). Calculates y response truth table for input gate (from library).  If NOT gate, 1 input; if NOR, 2 inputs. Distinguishes type of gate and calculates response function of gate

Partstogate: input gate name from data structure, input truth tables from previous gates (the ones to connect to current gate). Calculates response output from input truth table/s based on output from previous gate(s) (part 1 and part 2). Part 2 has a default value in case there is only 1 previous gate in circuit. 

Scorecalc: Calculates score based on scoring function for the final terminal gate truth table in circuit and prints result. 

Gate Modification Functions:
The following operations can be applied to each gate in the library: Stretch, slope increase, slope decrease, increase promoter strength,  decrease promoter strength, increase RBS strength, decrease RBS strength. 

Example Output:

Welcome to GDSProg!

Please input your library: Cello_lib.csv

To start assembly press s, to modify existing gates press m: m

Available modifications are: stretch, slopeincrease, slopedecrease, strongerpromoter, weakerpromoter, strongerRBS, weakerRBS 

Input function and gate name: slopedecrease O

Part Osld had its slope decreased by a factor of 100.0 . new slope =  0.063

To start assembly press s, to modify existing gates press m: s

How many gates do you start with? 3

Please type your gate (NOR gates should go before NOT gates): Osld

Please type your gate (NOR gates should go before NOT gates): P

Please type your gate (NOR gates should go before NOT gates): Q

Please type your inputs for NOT 3 

Please type your inputs for NOT 4

Please type your inputs for NOT 5

Your working parts are NOR:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['Osld', 'P', 'Q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
Input gate connection Osld to D

Gate needs second input, please type: P

Your working parts are NOR:  ['D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['Q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part' 

Input gate connection D to A

Gate needs second input, please type: Q

Your working parts are NOR:  ['A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part' 

Input gate connection A to T

Your working parts are NOR:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['T', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part' 

Input gate connection T score T

The score is  0.0005252347316966715

Do you want to modify your parts or stop? (press m or s) m

How many gates would you like to modify? 1

Please input gate name P

Part Pspr had its promoter strength increased by 400%.

Modification completed!

How many gates do you start with? 3

Please type your gate (NOR gates should go before NOT gates): O

Please type your gate (NOR gates should go before NOT gates): Pspr

Please type your gate (NOR gates should go before NOT gates): Q

Please type your inputs for NOT 2

Please type your inputs for NOT 3

Please type your inputs for NOT 4

Your working parts are NOR:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['O', 'Pspr', 'Q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
Input gate connection O to D

Gate needs second input, please type: Pspr
Your working parts are NOR:  ['D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['Q', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part' 

Input gate connection D to A

Gate needs second input, please type: Q

Your working parts are NOR:  ['A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part' 

Input gate connection A to T

Your working parts are NOR:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       NOT:  ['T', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                       
To finish type 'part score part'

Input gate connection T score T

The score is  0.0184042700984644

Do you want to modify your parts or stop? (press m or s) s

#Figure pops up#

#Program Ends
