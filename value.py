#!/usr/bin/python
import sys
import time
import copy
actions = ["up", "right", "down", "left"]
class MDP:

    def __init__(self, team_name, gamma):
        self.grid = [['-' for i in range(4)]for j in range(4)]
        self.utility = [[0 for i in range(4)]for j in range(4)]
        self.grid[0][0] = self.grid[0][1] = self.grid[0][3] = self.grid[2][2] = 'w'
        self.utility[0][2] = team_name
        self.utility[2][1] = -1 * team_name
        self.grid[0][2] = 'p'
        self.grid[2][1] = 'n'
        self.gamma = gamma
        self.reward = (-0.05 * team_name)
        self.convergence = (0.05 * team_name)

    def print_grid(self):
        print "GRID"
        for i in range(4):
            for j in range(4):
                print self.grid[i][j],
            print 
        print
        print "Utility Status"
        for i in range(4):
            for j in range(4):
                print "%.2f" % self.utility[i][j],
            print 
        print
        print

    def value_iteration(self):
        c = -1
        while(1):
            c += 1
            print
            print "=================Iteration",c+1,"====================="
            print
            delta = 0
            u = [[self.utility[i][j] for j in range(4)]for i in range(4)]
            for i in [3,2,1,0]:
                for j in range(4):
                    #print "hi"
                    if (self.grid[i][j] == 'n' or self.grid[i][j] == 'p' or self.grid[i][j] == 'w'):
                        continue
                    #self.utility[i][j] = self.reward
                    max_val = -100
                    print 
                    print "Cell:(",i,",",j,")" 
                    print
                    for l in actions:
                        prnt = ""
                        fl = 0
                        if  l == "up":
                            fl = 1
                            #prnt = ""
                            temp = 0
                            #print "hi"
                            if i-1 < 0:
                                temp += 0.8 * u[i][j]
                                prnt += "0.8*"+str(u[i][j])+" + "
                            else:
                                if self.grid[i-1][j] == 'w':
                                    temp += 0.8 * u[i][j]
                                    prnt += "0.8*"+str(u[i][j])+" + "
                                else:
                                    temp += 0.8 * u[i-1][j]
                                    prnt += "0.8*"+str(u[i-1][j])+" + "
                            if j-1 < 0:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])+" + " 
                            else:
                                if self.grid[i][j-1] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])+" + "
                                else:
                                    temp += 0.1 * u[i][j-1]
                                    prnt += "0.1*"+str(u[i][j-1])+" + "
                            if j+1 > 3:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])
                            else:
                                if self.grid[i][j+1] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])
                                else:
                                    temp += 0.1 * u[i][j+1]
                                    prnt += "0.1*"+str(u[i][j+1])
                            if temp > max_val:
                                max_val = temp
                            #print "North ->",prnt
                        
                        if  l == "down":
                            #prnt = ""
                            fl = 2
                            temp = 0
                            if i+1 > 3:
                                temp += 0.8 * u[i][j]
                                prnt += "0.8*"+str(u[i][j])+" + "
                            else:
                                if self.grid[i+1][j] == 'w':
                                    temp += 0.8 * u[i][j]
                                    prnt += "0.8*"+str(u[i][j])+" + "
                                else:
                                    temp += 0.8 * u[i+1][j]
                                    prnt += "0.8*"+str(u[i+1][j])+" + "
                            if j-1 < 0:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])+" + "
                            else:
                                if self.grid[i][j-1] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])+" + "
                                else:
                                    temp += 0.1 * u[i][j-1]
                                    prnt += "0.1*"+str(u[i][j-1])+" + "
                            if j+1 > 3:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])
                            else:
                                if self.grid[i][j+1] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])
                                else:
                                    temp += 0.1 * u[i][j+1]
                                    prnt += "0.1*"+str(u[i][j+1])
                            if temp > max_val:
                                max_val = temp 
                            #rint "South -> ",prnt 
                        
                        if  l == "left":
                            #prnt = ""
                            fl = 3
                            temp = 0
                            if j-1 < 0:
                                temp = 0.8 * u[i][j]
                                prnt += "0.8*"+str(u[i][j])+" + " 
                            else:
                                if self.grid[i][j-1] == 'w':
                                    temp += 0.8 * u[i][j]
                                    prnt += "0.8*"+str(u[i][j])+" + "  
                                else:
                                    temp += 0.8 * u[i][j-1]
                                    prnt += "0.8*"+str(u[i][j-1])+" + " 
                            if i-1 < 0:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])+" + "
                            else:
                                if self.grid[i-1][j] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])+" + " 
                                else:
                                    temp += 0.1 * u[i-1][j]
                                    prnt += "0.1*"+str(u[i-1][j])+" + "
                            if i+1 > 3:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j]) 
                            else:
                                if self.grid[i+1][j] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j]) 
                                else:
                                    temp += 0.1 * u[i+1][j]
                                    prnt += "0.1*"+str(u[i+1][j])
                            if temp > max_val:
                                max_val = temp   
                            #print "West ->",prnt
                            
                        
                        if  l == "right":
                            #prnt  = ""
                            fl = 4
                            temp = 0
                            if j+1 > 3:
                                temp = 0.8 * u[i][j]
                                prnt += "0.8*"+str(u[i][j])+"+" 
                            else:
                                if self.grid[i][j+1] == 'w':
                                    temp += 0.8 * u[i][j]
                                    prnt += "0.8*"+str(u[i][j])+"+" 
                                else:
                                    temp += 0.8 * u[i][j+1]
                                    prnt += "0.8*"+str(u[i][j+1])+"+" 
                            if i-1 < 0:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j])+"+"
                            else:
                                if self.grid[i-1][j] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j])+"+" 
                                else:
                                    temp += 0.1 * u[i-1][j]
                                    prnt += "0.1*"+str(u[i-1][j])+"+" 
                            if i+1 > 3:
                                temp += 0.1 * u[i][j]
                                prnt += "0.1*"+str(u[i][j]) 
                            else:
                                if self.grid[i+1][j] == 'w':
                                    temp += 0.1 * u[i][j]
                                    prnt += "0.1*"+str(u[i][j]) 
                                else:
                                    temp += 0.1 * u[i+1][j]
                                    prnt += "0.1*"+str(u[i+1][j])
                            if temp > max_val:
                                max_val = temp  
                           # print "East ->", prnt
                        if fl == 1:
                            print "North -> ", self.reward," + [", prnt,"]"
                        elif fl == 2:
                            print "South -> ", self.reward," + [", prnt,"]"
                        elif fl == 3:
                            print "West -> ", self.reward," + [", prnt,"]"
                        else:
                            print "East -> ", self.reward," + [", prnt,"]"
                        print "Util: ", temp + self.reward
                        print
                        fl = 0

                    self.utility[i][j] = self.reward + (self.gamma * max_val)

                    if abs(self.utility[i][j] - u[i][j]) > delta:
                        delta = self.utility[i][j] - u[i][j]
                    
                    
            self.print_grid()
            if delta < self.convergence:
                break
        return self.utility

if __name__ == '__main__':
    goal = ''
    print "Enter Team_name:"
    team_name = input()
    print "Enter gamma:"
    gamma = input()
    #print "Enter "
    
    goal = MDP(team_name,gamma)
    goal.print_grid()
    ans  = goal.value_iteration()
    print "result"
    print goal.print_grid()








