import os

os.listdir(".")

def lines(f): 
    # lines(f) takes the name of a file, and it returns a list of strings, each holding one line from the file. 
    # lines(f) returns [] if f doesn't exist.
    y = []
    if not os.path.exists(f):
        return y
    x = open(f, "r")
    for line in x:
        line = line.strip()
        y.append(line)
    return y

def candidates(f): 
    # candidates(f) takes the name of a file describing the candidates in an election, and it returns a list of 
    # tuples, each containing the name of a candidate and their pre-registered voting ticket (or an empty string
    # if there is no ticket). 
    # e.g. given file.txt, candidates("file.txt") returns [("AB", "132"), ("C D", ""), ("EFG", ""), 
    # ("HJ K", "2 1")]. 
    # You may assume that the format of the file is always correct, and you should disregard any blank lines in 
    # the file.
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
    #rankedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, 
    # and it returns a list of strings holding the interpretation of p as a ranked vote.
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

def zeroElection(cs): 
    # JAMES
    # zeroElection(cs) takes a list of tuples cs that describes the candidates in an election, and it returns a 
    # dictionary containing one entry for each candidate. Each entry is a tuple of the form (0, [], k, x), where
    # k is a distinct index from 0 for each candidate, and x is the vote corresponding to the candidate's 
    # pre-registered voting ticket. 
    # e.g. zeroElection([("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]) returns the dictionary 
    # {"AB": (0, [], 0, ["AB", "EFG", "C D"]), "C D": (0, [], 1, ["C D"]), "EFG": (0, [], 2, ["EFG"]), 
    # "HJ K": (0, [], 3, ["HJ K", "AB"])}. 
        piles = {}
        for counter in range(len(cs)):
                item = cs[counter]
                candidateName = item[0]
                candidateTicket = item[1]
                vote = rankedVote(candidateTicket, cs)
                if vote == []:
                    vote.append(candidateName)
                piles[candidateName] = (0,[],counter,vote)
        return piles

    # In each tuple, the second field holds the current list of votes for that candidate, and the first field 
    # always holds the length of that list. We shall refer to a dictionary of this form as an election status.

def markedVote(p, cs): 
    #markedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, 
    # and it returns a list of strings holding the interpretation of p as a marked vote.
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

def writtenVote(p, piles): 
    #writtenVote(p, piles) takes a string p and an election status piles, and it returns a list of strings
    # holding the interpretation of p as a written vote wrt piles. writtenVote(p, piles) returns [] for all p 
    # which aren't valid written votes. See formal.html for more examples.
    for eachKey in piles:
        if eachKey == p:
            x = piles[eachKey]
            y = x[3]
            return y
    return []

def paperToVote(p, cs, piles):
    #paperToVote(p, cs, piles) takes a string p, a list of tuples cs that describes the candidates in an 
    # election, and a corresponding election status piles, and it returns a list of strings holding the
    # interpretation of p as a vote. paperToVote(p, cs, piles) returns [] for all p which aren't valid votes.
    x = writtenVote(p, piles)
    if x != []:
        return x
    y = rankedVote(p, cs)
    if y != []:
        return y
    z = markedVote(p, cs)
    if z != []:
        return z
    return []


def distributeVotes(vs, piles): 
    # distributeVotes(vs, piles) takes a list of votes vs and an election status piles, and it returns a 
    # tuple containing the new piles where each vote in vs has been distributed to its highest-ranked 
    # surviving candidate, and the number of empty votes from vs. 

    # Note that if a vote v is distributed to a candidate c, then all entries on v up to and including c
    # should be deleted. 
    # e.g. if ["A", "B", "C", "D"] is distributed to C (presumably because "A" and "B" have already been 
    # eliminated from the election), then the vote added to C's pile should be just ["D"].

    # piles is a list ie - {"AB": (0, [], 0, ["AB", "EFG", "C D"]), "C D": (0, [], 1, ["C D"]), 
    # "EFG": (0, [], 2, ["EFG"]), "HJ K": (0, [], 3, ["HJ K", "AB"])}. 
    # 
    # determine if the votes are marked, written or ranked
    # loop that goes through each vote (for each vote in vs, add it to the candidate's list and increase
    # count. also keep a counter for number of empty votes)
    emptyVotes = 0
    found = False
    for vote in vs:
        for i in range(len(vote)):
            candidate = vote[i]
            if candidate in piles:
                found = True
                piles[candidate][1].append(vote[i:])
                piles[candidate][0] += 1
                break
        if found == False:
            emptyVotes += 1
    return (piles, emptyVotes)

def leader(piles):
    # piles not empty: 
    # leader(piles) takes an election status piles, and it returns the name of the top candidate 

    # just double check 
    if piles == {}: print('uh oh - piles was not empty!')

    # sort the list by vote score and return the last name
    return sorted(piles, key=lambda x: x[0], reverse=False)[0]


def loser(piles):
    # piles not empty:  
    # loser(piles) takes an election status piles, and it returns 
    # the name of the candidate who has the least votes.

    # just double check 
    if piles == {}: print('uh oh - piles was not empty!')

    # sort the list by vote score and return the first name
    return sorted(piles, key=lambda x: x[0], reverse=True)[0]


def nextRound(piles):
    # piles not empty: 
    # nextRound(piles) takes an election status piles, it identifies the trailing candidate c, and it 
    # returns a tuple containing piles after c has been removed and c's votes have been re-distributed, and
    # the number of c's votes that expired. 
    # The re-distributed votes should be cut back as described under distributeVotes.

    # get the votes from the losing candidate's tuple in piles
    vs = piles[loser(piles)][1]

    # delete the losing candidate
    del piles[loser(piles)]

    # redistribute the votes minus the losing candidate
    (piles, emptyVotes) = distributeVotes(vs, piles)
    
    # return
    return (piles, emptyVotes)

def displayStandings(piles, winningLine):
    # assume piles not empty 
    # displayStandings(piles, ...) takes an election status piles, and it uses turtle graphics to display the 
    # current standings on the screen. results.txt lists the kind of information that your display should 
    # include. If you want to pass other arguments to displayStandings, that's fine: it will not be called 
    # directly by the testing or marking programs.
    print('----------------------')
    for key in piles:
        print(key + ': ' + str(piles[key][0]) + ' votes')
    print('The winning line is at ' + str(winningLine) + '.')
    print(str(leader(piles)) + ' has x votes...')
    print(str(winner(piles)) + ' has won the election!')

def main(): 
    # main() prompts the user for the names of a file of candidates' information and a file of completed 
    # ballot papers, and it conducts an Antarctican election and displays the results on the screen.

    # sort candidates
    cs = candidates(str(input("Enter the candidates' info text filename please: ")))

    #load ballot papers
    papers = lines(str(input("Enter the ballot papers text filename please: ")))

    piles = {}
    piles = zeroElection(cs)

    # parse vote papers
    vs = []
    informalVotes = 0
    for paper in papers:
        result = paperToVote(paper, cs, piles)
        if result == []:
            informalVotes += 1
        else:
            vs.append(result)

    # get piles
    piles = zeroElection(cs)

    # INTRODUCTION
    print(str(len(papers)) + ' ballot papers were cast.')
    print('However, some ' + str(informalVotes) + ' were invalid.')

    # variable typing/defn
    winningLine = len(vs) // 2 + 1        # ie an integer
    winner = ""                                # ie a string

    (piles, emptyVotes) = distributeVotes(vs, piles)
    
    # PARAGRAPH
    while piles[leader(piles)][0] > winningLine:
        # output some status info
        displayStandings(piles, winningLine)

        # if no clear winner, then run nextRound
        piles = nextRound(piles)

        # calculate winning line
        winningLine = len(vs) // 2 + 1
    # CONCLUSION
    print('The winner is...   ' + str(winner))


main()
