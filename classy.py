# jsdavo 31st May 2012
# James Davidson + Cynthia Tam (for CITS1401 @ UWA)

# Basically an Antarctican Election using optional preferential voting
# rewritten for Lyndon While in a way that makes... well.. sense?

"""
FAT DEFN FOR SOME SEMANTIC SCOPE
	Basically, the whole program is about distributing votes to piles,
	one pile for each candidate. The votes arrive in a bit of a messy
	format but are parsed to a useful list of preferences. Similarly,
	information about the candidates is messy but sorted out eventually.
	
	The tricky (and crucial) thing however is that it is not a simple
	'first past the post' election. A winning line is set and the votes
	are counted. If there is no winner then the lowest ranked candidate's
	pile is removed and the votes are either redistributed or expire.
	
	The process of rounds is continued until one candidate eventually
	passes the winning line.
"""

class OPV(object):

	def __init__(self):
		# variable typing
		self.Votes = []
		self.Piles = []
		self.Candidates = []
		self.Papers = []

	class CandidateList(self

	class Vote(object):		# definition for a Vote object

		def __init__(self, raw):
			# parse the raw input
			self.raw = raw
			for letter in raw:
				if(letter != alphabetical): return 'ok'


	class Pile(list):
		def __init__(self, candidate):
			# some stuff here
		def sort(self):
			return self.sorted(yadyayda)

	class Candidate(object):		# definition for a Pile object
		def __init__(self, raw):
			# variable typing
			self.raw = raw
			# parse raw into variables
			self.name = raw.split(':')[0]
			self.ticket = Vote(raw.split(':')[1])

	def loadCandidates(self, f):	# get the information from file and pass it to the Pile constructor
		for rawLine in lines(f):
			# generate a Pile for each candidate entry
			self._votes.pile(Election.Pile(rawLine))

	def loadPapers(self, f):	# get the information from file and pass it to the Vote constructor
		for rawLine in lines(f):
			# generate a Vote for each ballot paper
			self._votes.append(Election.Vote(rawLine))


"""
MAIN PROGRAM
"""

Election = OPV()		# instantiate an election of the Optional Preferential Voting class

Election.loadCandidates('candidates.txt')	# get some input from file
Election.loadPapers('papers.txt')		# get some more input

print('Election candidates: ' + str(Election.Candidates))
print('Ballot papers cast: ' + str(Election.Papers.count))	# update the audience
print('Valid votes: ' + str(Election.Votes.count))		# more updates

while Election.winner == '':		# ie counting in progress
	Election.distributeVotes()	# sort the votes into piles
	print(str(Election.status))	# ie displayStandings

print('The winner is... ' + str(Election.winner))




