def lines(f): 
lines(f) takes the name of a file, and it returns a list of strings, each holding one line from the file. lines(f) returns [] if f doesn't exist.

def candidates(f): 
candidates(f) takes the name of a file describing the candidates in an election, and it returns a list of tuples, each containing the name of a candidate and their pre-registered voting ticket (or an empty string if there is no ticket). 
e.g. given file.txt, candidates("file.txt") returns [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]. 
You may assume that the format of the file is always correct, and you should disregard any blank lines in the file.

def rankedVote(p, cs): 
rankedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, and it returns a list of strings holding the interpretation of p as a ranked vote. 
e.g. given cs = [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]: 
rankedVote("21 3", cs) returns ["C D", "AB", "HJ K"], 
rankedVote("2 12", cs) returns ["EFG"], and 
rankedVote(p, cs) returns [] for all p which aren't valid ranked votes. See formal.html for more examples.

def zeroElection(cs): 
zeroElection(cs) takes a list of tuples cs that describes the candidates in an election, and it returns a dictionary containing one entry for each candidate. Each entry is a tuple of the form (0, [], k, x), where k is a distinct index from 0 for each candidate, and x is the vote corresponding to the candidate's pre-registered voting ticket. 
e.g. zeroElection([("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]) returns the dictionary 
{"AB": (0, [], 0, ["AB", "EFG", "C D"]), "C D": (0, [], 1, ["C D"]), "EFG": (0, [], 2, ["EFG"]), "HJ K": (0, [], 3, ["HJ K", "AB"])}. 

In each tuple, the second field holds the current list of votes for that candidate, and the first field always holds the length of that list. We shall refer to a dictionary of this form as an election status.

def markedVote(p, cs): 
markedVote(p, cs) takes a string p and a list of tuples cs that describes the candidates in an election, and it returns a list of strings holding the interpretation of p as a marked vote. 
e.g. given cs = [("AB", "132"), ("C D", ""), ("EFG", ""), ("HJ K", "2 1")]: 
markedVote(" x", cs) returns ["C D"], 
markedVote("2 ", cs) returns ["AB"], and 
markedVote(p, cs) returns [] for all p which aren't valid marked votes. See formal.html for more examples.

def writtenVote(p, piles): 
writtenVote(p, piles) takes a string p and an election status piles, and it returns a list of strings holding the interpretation of p as a written vote wrt piles. writtenVote(p, piles) returns [] for all p which aren't valid written votes. See formal.html for more examples.

def paperToVote(p, cs, piles): 
paperToVote(p, cs, piles) takes a string p, a list of tuples cs that describes the candidates in an election, and a corresponding election status piles, and it returns a list of strings holding the interpretation of p as a vote. paperToVote(p, cs, piles) returns [] for all p which aren't valid votes.

def distributeVotes(vs, piles): 
distributeVotes(vs, piles) takes a list of votes vs and an election status piles, and it returns a tuple containing the new piles where each vote in vs has been distributed to its highest-ranked surviving candidate, and the number of empty votes from vs. 

Note that if a vote v is distributed to a candidate c, then all entries on v up to and including c should be deleted. 
e.g. if ["A", "B", "C", "D"] is distributed to C (presumably because "A" and "B" have already been eliminated from the election), then the vote added to C's pile should be just ["D"].

def leader(piles), piles not empty: 
leader(piles) takes an election status piles, and it returns the name of the candidate who has the most votes.

def loser(piles), piles not empty: 
loser(piles) takes an election status piles, and it returns the name of the candidate who has the least votes.

def nextRound(piles), piles not empty: 
nextRound(piles) takes an election status piles, it identifies the trailing candidate c, and it returns a tuple containing
piles after c has been removed and c's votes have been re-distributed, and
the number of c's votes that expired.
The re-distributed votes should be cut back as described under distributeVotes.

def displayStandings(piles, ...), piles not empty: 
displayStandings(piles, ...) takes an election status piles, and it uses turtle graphics to display the current standings on the screen. results.txt lists the kind of information that your display should include. 

If you want to pass other arguments to displayStandings, that's fine: it will not be called directly by the testing or marking programs.

def main(): 
main() prompts the user for the names of a file of candidates' information and a file of completed ballot papers, and it conducts an Antarctican election and displays the results on the screen.

