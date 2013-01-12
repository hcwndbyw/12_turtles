command_templates = { "forward": ("forward", [int]), "backward": ("backward", [int]) }
command_instances = {} 
types_waiting = {}

class Command():
    __slots__ = ['needed_params', 'params', 'name']

    def __init__(self, name, needed_params):
        self.needed_params = needed_params
        self.name = name

    def next_needed_type(self):
        return self.needed_params[0]

    def supply_arg(self, p):
        ''' type of the param has been checked return True if this has been sent to run false if not'''
        self.params.append(p)
        self.needed_params = need_params[1:]
        if len(self.needed_params) == 0:
            send_to_run(str(self))
            return True
        return False
            
    def __str__(self):
        return name + '(' + str(params)[1:-1] + ')'

def safe_append(dictionary, key, val):
    if not key in dictionary:
        dictionary[key] = []
    dictionary[key].append(val)

def append_cmds_processing(cmd):
    temp = Command(*command_templates[cmd])
    safe_append(command_instances, cmd, temp)
#    if not cmd in command_instances:
#        command_instance[cmd] = []
#
#    command_instances[cmd].append(temp)

    safe_append(types_waiting, temp.next_needed_type(), temp)
#    if not temp.next_needed_type() in types_wating:
#        types_waiting[temp.next_needed_type()] = []
#    types_waiting[temp.next_needed_type()].append(temp)

def try_parse_type(word):
    for possibleType in types_waiting:
        print possibleType
        try:
            temp = possibleType(word)
            t = types_waiting[temp]
            types_waiting[temp] = types_waiting[1:]
            if not types_waiting[temp].supply_arg(word): #didn't complete call
                safe_append(types_waiting, t.next_needed_type(), t)
#                types_waiting[t.next_needed_type()].append( t )
        except:
            continue

def supply_words(tweet):
    for word in tweet:
        if word in command_templates: # recognized command
            append_cmds_processing(word)
        else:
            try_parse_type(word)


