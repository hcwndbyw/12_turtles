import runner

runner._init()

command_templates = { 
    "forward": ("forward", [int]),
    "fd": ("fd", [int]),            
    "back": ("back", [int]),
    "backward": ("backward", [int]),
    "bk": ("bk", [int]),
    "right": ("right",[int]),
    "rt": ("rt", [int]),
    "left": ("left",[int]),
    "lt": ("lt", [int]),
    "goto": ("goto", [int,int]),
    "setpos": ("setpos", [int,int]),
    "setposition": ("setposition", [int,int]),
    "setx": ("setx", [int]),
    "sety": ("sety", [int]),
    #setheading
    #seth
    "home": ("home", []),
    "circle": ("circle", [int]), #only radius
    "dot": ("dot", [int]), #only size
    "stamp": ("stamp", []),
    #clearstamp
    "undo": ("undo", []),
    #speed
    "degrees": ("degrees", []), #noargs
    "radians": ("radians", []),
    #pendown
    #pd
    #down
    #penup
    #pu
    #up
    "pensize": ("pensize", [int]), #force a param
    "width": ("width", [int]),
    #pen
    #color
    #pencolor
    #fillcolor
    #fill
    "begin_fill": ("begin_fill", []),
    "end_fill": ("end_fill", [])
    #reset
    #clear
    #write
    #begin_poly
    #end_poly

}

command_instances = {} 
types_waiting = {}

class Command():
    __slots__ = ['needed_params', 'params', 'name', 'tweets']

    def __init__(self, name, needed_params):
        self.needed_params = needed_params[:]
        self.name = name
        self.params = []
        self.tweets = []

    def add_tweet(self,tweet):
        self.tweets.append(tweet)

    def next_needed_type(self):
        return self.needed_params[0]

    def print_tweets(self):
        print (str(self) + "\n Brought to you by:")
        for tweet in self.tweets:
            print "    " +tweet.user.name+ ":\n        "+ tweet.text
        print

    def supply_arg(self, p, tweet):
        ''' type of the param has been checked return True if this has been sent to run false if not'''
        if type(p) == int:
            p = p%1000
        self.add_tweet(tweet)
        self.params.append(p)
        self.needed_params.pop(0)
        if len(self.needed_params) == 0:
            self.print_tweets()
            runner.giveCommand(str(self))
            return True
        return False
            
    def __str__(self):
        return self.name + '(' + str(self.params)[1:-1] + ')'

    def __repr__(self):
        return str(self)

def safe_append(dictionary, key, val):
    if not key in dictionary:
        dictionary[key] = []
    dictionary[key].append(val)

def append_cmds_processing(cmd, tweet):
    temp = Command(*command_templates[cmd])
    temp.add_tweet(tweet)
    if len(temp.needed_params) == 0:
        temp.print_tweets()
        runner.giveCommand(str(temp))
    else:
        safe_append(command_instances, cmd, temp)
        safe_append(types_waiting, temp.next_needed_type(), temp)

def try_parse_type(word, tweet):
    for possibleType in types_waiting:
        try:
            typeWanted = possibleType(word)
            fnCall = types_waiting[possibleType][0]
            types_waiting[possibleType] = types_waiting[possibleType][1:]
            if not fnCall.supply_arg(typeWanted, tweet): #didn't complete call
                safe_append(types_waiting, fnCall.next_needed_type(), fnCall)
            else:
                command_instances[fnCall.name].remove(fnCall)
            break
        except:
            continue

def supply_words(tweet):
    for word in tweet.text.split():
        if word in command_templates: # recognized command
            append_cmds_processing(word, tweet)
        else:
            try_parse_type(word, tweet)


