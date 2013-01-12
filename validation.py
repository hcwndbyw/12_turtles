import runner
command_templates = { "forward": ("forward", [int]), "backward": ("backward", [int]) }
command_instances = {} 
types_waiting = {}

class Command():
    __slots__ = ['needed_params', 'params', 'name']

    def __init__(self, name, needed_params):
        self.needed_params = needed_params[:]
        self.name = name
        self.params = []

    def next_needed_type(self):
        print len(self.needed_params)
        return self.needed_params[0]

    def supply_arg(self, p):
        ''' type of the param has been checked return True if this has been sent to run false if not'''
        self.params.append(p)
        self.needed_params.pop(0)
        if len(self.needed_params) == 0:
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

def append_cmds_processing(cmd):
    temp = Command(*command_templates[cmd])
    safe_append(command_instances, cmd, temp)
    safe_append(types_waiting, temp.next_needed_type(), temp)

def try_parse_type(word):
    for possibleType in types_waiting:
        try:
            typeWanted = possibleType(word)
            fnCall = types_waiting[possibleType][0]
            types_waiting[possibleType] = types_waiting[possibleType][1:]
            if not fnCall.supply_arg(typeWanted): #didn'fnCall complete call
                safe_append(types_waiting, fnCall.next_needed_type(), fnCall)
            else:
                print command_instances[fnCall.name]
                command_instances[fnCall.name].remove(fnCall)
                print command_instances[fnCall.name]
                '''
                for i in range(len(command_instances[temp.name])):
                    if command_instance[temp.name][i] == t:
                        command_instance[temp.name].pop(i)
                        break'''
        except:
            continue

def supply_words(tweet):
    for word in tweet:
        if word in command_templates: # recognized command
            append_cmds_processing(word)
        else:
            try_parse_type(word)


