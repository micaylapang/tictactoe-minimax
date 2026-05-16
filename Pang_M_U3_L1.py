# Name: Micayla Pang 
# Date: 12/4/24

def successors(state, turn):
   sli = [i for i in range(len(state)) if state[i] == '.'] #indexes of all blank spots
   ret = [(state, state[0:i] + turn + state[i+1:]) for i in sli] #
   return ret  # [(previous state, new state), ...]

def terminal_test(state, tc):
   if state.find('.') < 0: return True #find returns index & -1 if not there, end if no empty spot
   for li in tc:
      check_li = [state[x] for x in li]
      if len(set(check_li)) == 1 and check_li[0] != '.':
         return True
   return False
      
def utility(turn, tc, state):
   # return 1 (turn wins), -1 (turn loses), or 0 (tie)  
   for l in tc: 
      v = [state[x] for x in l]
      if len(set(v))==1 and v[0]!='.': 
         return 1 if v[0]==turn else -1
   return 0   

def minimax(state, turn, tc):
   return max_value(state, turn, tc)[1]  #returns state w maximized chance for turn

def max_value(state, turn, tc): # recursive
   if terminal_test(state,tc): 
      return (utility(turn, tc, state), state)
   maxv = -2
   maxs = state 
   for s in successors(state, turn): 
      if turn=='X': nt='O'
      else: nt='X'
      minv = min_value(s[1], nt, tc)[0]
      if minv>maxv: 
         maxv=minv
         maxs = s[1]
   return (maxv, maxs)
   
def min_value(state, turn, tc):
   if terminal_test(state,tc): 
      return (-1*utility(turn, tc, state), state)
   minv = 2 
   mins = state
   for s in successors(state, turn): 
      if turn=='X': nt='O'
      else: nt='X'
      maxv = max_value(s[1], nt, tc)[0]
      if maxv<minv: 
         minv=maxv
         mins = s[1]
   return (minv, mins)

def get_turn(state):
   if state.count('X')==state.count('O'): 
      return 'X' 
   return "O"

def conditions_table(n=3, n2=9): #n=r/c length
   ret = [[] for i in range(n*2+2)] #7 arrays: 3 rows, 3 cols, 2 diagonals
   for i in range(n2): #n2 is length of state 
      ret[i//n].append(i)     # rows: [0, 1, 2], [3, 4, 5], [6, 7, 8]
      ret[n+i%n].append(i)    # cols: [0, 3, 6], [1, 4, 7], [2, 5, 8]
      if i//n == i % n: ret[n+n].append(i)   # diagonal \: [0, 4, 8]
      if i // n == n - i%n - 1: ret[n+n+1].append(i)  # diagonal /: [2, 4, 6]
   return ret

def display(state, n=3, n2=9):
   str = ""
   for i in range(n2):
      str += state[i] + ' '
      if i % n == n-1: str += '\n'
   return str

def human_play(s, n, turn):
   index_li = [x for x in range(len(s)) if s[x] == '.']
   for i in index_li:
      print ('[%s] (%s, %s)' % (i, i//n, i%n))
   index = int(input("What's your input? (Type a number): "))
   while s[index] != '.':
      index = int(input("Invalid. What's your input? "))
   state = s[0:index] + turn + s[index+1:]
   return state
   
def main():
   X = input("X is human or AI? (h: human, a: AI) ")
   O = input("O is human or AI? (h: human, a: AI) ")
   state = input("input state (ENTER if it's an empty state): ")
   if len(state) == 0: state = '.........'
   turn = get_turn(state)
   tc = conditions_table(3, 9)
   print ("Game start!")
   print (display(state, 3, 9))
   while terminal_test(state, tc) == False:
      if turn == 'X':
         print ("{}'s turn:".format(turn))
         if X == 'a': state = minimax(state, turn, tc)
         else: state = human_play(state, 3, turn)
         print (display(state, 3, 9))
         turn = 'O'
      else:
         print ("{}'s turn:".format(turn))
         if O == 'a': state = minimax(state, turn, tc)
         else: state = human_play(state, 3, turn)
         print (display(state, 3, 9))
         turn = 'X'
         
   if utility(turn, tc, state) == 0: #utility tells you who won 
      print ("Game over! Tie!")
   else: 
      turn = 'O' if turn == 'X' else 'X'
      print ('Game over! ' + turn + ' win!')

if __name__ =='__main__':
   main()