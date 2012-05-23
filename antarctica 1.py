import os

os.listdir(".")

def lines(f): 
    #lines(f) takes the name of a file, and it returns a list of strings, each holding one line from the file. lines(f) returns [] if f doesn't exist.
    x = open(f, "r")
    y = []
    for line in x:
        line = line.strip()
        y.append(line)
    return y

def candidates(f): 
    """candidates(f) takes the name of a file describing the candidates in an election, and it returns a list of tuples, each containing the name of a candidate and their pre-registered voting ticket (or an empty string if there is no ticket). 
    e.g. given file.txt, candidates("file.txt") returns [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]. 
    You may assume that the format of the file is always correct, and you should disregard any blank lines in the file."""
    candidateList = lines(f)
    newCandidateList = []
    for candidate in candidateList:
        eachWord = candidate.split(':')
        if len(eachWord) == 2:
            eachTuple = (eachWord[0], eachWord[1])
        else:
            eachTuple = (eachWord[0], "")
        newCandidateList.append(eachTuple)
    return newCandidateList

def rankedVote(p, cs): 
    #rankedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, and it returns a list of strings holding the interpretation of p as a ranked vote.
    # e.g. given cs = [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]: 
    #rankedVote("21 3", cs) returns ["C D", "AB", "HJ K"], 
    #rankedVote("2 12", cs) returns ["EFG"], and 
    #rankedVote(p, cs) returns [] for all p which aren't valid ranked votes. See formal.html for more examples.
    candidateList = []
    for rank in range(1,10):
        candidateNumber = p.find(str(rank))
        if p.find(str(rank), candidateNumber+1) != -1:
            return candidateList
        if candidateNumber == -1:
            return candidateList
        candidateName = cs[candidateNumber][0]
        candidateList.append(candidateName)
    return candidateList

def markedVote(p, cs): 
    #markedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, and it returns a list of strings holding the interpretation of p as a marked vote.
    # e.g. given cs = [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]: 
    #markedVote(" x", cs) returns ["C D"], 
    #markedVote("2 ", cs) returns ["AB"], and 
    #markedVote(p, cs) returns [] for all p which aren't valid marked votes. See formal.html for more examples.
    candidateList = []
    candidateMark = p.strip()
    if len(candidateMark) == 1:
        position = p.rstrip()
        candidateNumber = len(position) - 1
        candidateName = cs[candidateNumber][0]
        candidateList.append(candidateName)
    return candidateList

6.def writtenVote(p, piles): 
    #writtenVote(p, piles) takes a string p and an election status piles, and it returns a list of strings holding the interpretation of p as a written vote wrt piles. writtenVote(p, piles) returns [] for all p which aren't valid written votes. See formal.html for more examples.
    
