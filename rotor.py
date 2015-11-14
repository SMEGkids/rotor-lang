#Copyright (C) 2015 Hipe99

#This file is part of Rotor.

#Rotor is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Rotor is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with Rotor. 
#If not, see <http://www.gnu.org/licenses/>.
wheels=[{'N':(lambda stack: stack.append(math.log(stack.pop)))},{'N':(lambda stack: print('\n')}]
special={}
program=tokenise(input('>'))#british spelling all the way!
currentwheel=0
stack=[]
for i in program:
    if '"' == i[0]:
        stack.append(i[1:])
    elif ' in i:
        stack.append(i[1])
    elif i=='>':
        currentwheel=(currentwheel+1)%len(wheels)
    elif i=='<':
        currentwheel=(currentwheel-1) if currentwheel!=0 else len(wheels)
    elif i in list(special.keys):
        special[i](stack)
    elif i in wheels[currentwheel]:
        wheels[currentwheel][i](stack)
def tokenise(thing):
    tokens=[]
    mode="normal"
    for i in thing:
        if i=="'":
            mode='pushchar'
            tokens.append("'")
        elif i=='"':
            mode = 'pushstr' if mode=='normal' else mode='normal'
            tokens.append('"') if mode=='pushstr'
        if mode=='normal':
            tokens.append(i)
        elif mode=='pushchar':
            tokens[-1]=tokens[-1]+i
            mode='normal'
        else:
            tokens[-1]=tokens[-1]+i
      
    
 
