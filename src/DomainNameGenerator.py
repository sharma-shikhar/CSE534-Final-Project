import os
import Filenames
import random
import pickle
from RandomStringGenerator import RandomStringGenerator

def generateTLDs(nTLD, seed):
    tlds = []
    print(seed)
    r = RandomStringGenerator(seed, 3)
    for i in range(0, nTLD):
        tlds.append(r.getNext().lower())
    #print(tlds)
    return tlds

'''
returns a list of domain names
'''
def generateDomainNames(count, levels, nTLD, seed):
    ans = []
    tlds = generateTLDs(nTLD, seed)
    r = RandomStringGenerator(seed)
    for i in range(0, count):
        name = ''
        for j in range(0, levels-1):
            name = name + r.getNext().lower() + '.'
        t = 0
        for char in r.getNext().lower():
            t += ord(char)
        t = t%nTLD
        name = name + tlds[t]
        ans.append(name)
    return ans

def createDomainNameFile(filename, config):
    ans = generateDomainNames(config['nNames'], config['levels'], config['nTLD'], config['seedNames'])
    f = open(filename, 'wb')
    f.truncate()
    pickle.dump(ans, f)
    f.close()

def createDomainNameFileIfNotExists(config):
        filename = Filenames.getDomainNamesFilename(config)
        if not os.path.exists(filename):
            createDomainNameFile(filename, config)
