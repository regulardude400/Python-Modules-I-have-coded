'''
Change Jar
Alvin Williams
'''

class ChangeJar():
    
    def __init__(self, change={}):
        '''
        Creates an empty dictionary object.
        Holds the change types: Pennies, Dimes, Nickels, Quarters
        and checks to see if the change is valid..
        '''
        self.change = change
        for k in change:
           if k not in ["25","10","5","1"]:
               raise KeyError("Invalid type of change")
            
    def get_change(self, dollar_amt):
        '''
        Returns a dollar amount
        from the specified change.
        '''
        count_q = 0
        count_d = 0
        count_n = 0
        count_p = 0
        for k, v in sorted(self.change):
            if k == "25" and dollar_amt % int(k)==0:
                print("hi")
                count_q += 1
            else:
                print(dollar_amt%int(k))
                continue
            if k == "10" and dollar_amt % int(k)==0:
                count_d +=1
            else:
                continue
            if k == "5" and dollar_amt % int(k)==0:
                count_n +=1
            else:
                continue
            if k == "1" and dollar_amt % int(k)==0:
                count_p +=1
            else:
                continue
        print(count_q,count_d,count_n,count_p)
        
            
            
    def __getitem__(self, idx):
        '''
        Return item at specified index.
        '''
        for k in self.change:
            if idx > "25":
                raise StopIteration
            elif idx == "25" or idx == "10" or idx == "5" or idx == "1":
                return self.change[idx]
            else:
                return 0
    
    def insert(self, coin_value, num_coins):
        '''
        Inserts a coin into the dictionary object.
        Adds onto the current total number of coins if already in dict
        else start new key and value.
        '''
        if coin_value not in ["25","10","5","1"] or num_coins <= 0:
            return "Not a valid coin value or numerical value for num_coins"
        
        if coin_value in self.change:
            self.change[coin_value] += num_coins
        else:
            self.change[coin_value] = num_coins
    
    def total_value(self):
        '''
        Returns the total value in dollar amount
        '''
        f = 0
        for i in self.change:
            f += int(i)*self.change[i]
        return float(f) / 100
    
    def __str__(self):
        '''
        Returns a string representation of the dictionary.
        '''
        astr = ""
        if self.change == {}:
            return "Empty"
        else:
            for k in sorted(self.change):
                if k == "25":
                    astr += "\nQuarters: " + str(self.change[k])
                elif k == "10":
                    astr +=  "\nDimes: " + str(self.change[k])
                elif k == "5":
                    astr += "\nNickels: " + str(self.change[k])
                else:
                    astr += "\nPennies: " + str(self.change[k])
        return astr
    def __repr__(self):
        '''
        Returns __str__
        '''
        return self.__str__()

    
    def __add__(self, other):
        '''
        Adds up all of the keys and values in the ChangeJar
        '''
        U = ChangeJar()
        for i,v in other.change.items():
           U.insert(i,v)
           for k,p in self.change.items():
               U.insert(k,p)
        return U.change

    def __eq__(self, other):
        '''
       Compares the change types and the amounts,
       and if it works then it returns True
       else False.
        '''
        if self.change == {} and other.change == {}:
                return True
        else:
            for i,p in other.change.items():
                for k,v in self.change.items():
                    if k==i and v ==p:
                        return True
                    else:
                        return False
    
    def __ne__(self, other):
        '''
        Returns the opposite of __eq__ if the conditions
        match.
        '''
        return not self.__eq__(other)
    
    
    
        
