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
wheels={}
special={}
program=input('>')
currentwheel=0
stack=[]
for i in program:
    if i=='>':
        currentwheel=(currentwheel+1)%len(wheels)
    elif i=='<':
        currentwheel=(currentwheel-1) if currentwheel!=0 else len(wheels)
    elif i in list(special.keys):
        special[i](stack)
    elif i in wheels[currentwheel]:
        wheels[currentwheel][i](stack)
        
