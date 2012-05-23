"""
Short test file for Project 2, election night. 

We do not claim that this file is a complete testing scheme: 
its primary purpose is to check the spelling of the function names. 
You should supplement the tests in this file with your own tests. 
The correctness of your program is your responsibility. 

Author: Lyndon While 
Date: 12/5/12
"""

version = 1.11

import antarctica

def test_lines():
    tests = [("wrongname.txt", [])
            ,("file.txt",     ['AB:132', 'C D', 'EFG', 'HJ K:2  1'])
            ]
    return [(a, z, antarctica.lines(a)) for (a, z) in tests]

def test_candidates():
    tests = [("namewrong.txt", [])
            ,("file.txt",     [('AB', '132'), ('C D', ''), ('EFG', ''), ('HJ K', '2  1')])
            ]
    return [(a, z, antarctica.candidates(a)) for (a, z) in tests]

def test_rankedVote():
    cs = [('AB', '132'), ('C D', ''), ('EFG', ''), ('HJ K', '2  1')]
    tests = [("4321", ["HJ K", "EFG", "C D", "AB"])
            ,("3121", [])
            ,("",     [])
            ]
    return [(a, cs, z, antarctica.rankedVote(a, cs)) for (a, z) in tests]

def test_zeroElection():
    cs = [('AB', '132'), ('C D', ''), ('EFG', ''), ('HJ K', '2  1')]
    piles = {'AB': (0, [], 0, ["AB", "EFG", "C D"]), 'C D': (0, [], 1, ["C D"]), \
             'EFG': (0, [], 2, ["EFG"]), 'HJ K': (0, [], 3, ["HJ K", "AB"])}
    tests = [(cs, piles)
            ]
    return [(a, z, antarctica.zeroElection(a)) for (a, z) in tests]

def test_markedVote():
    cs = [('AB', '132'), ('C D', ''), ('EFG', ''), ('HJ K', '2  1')]
    tests = [("  ? ", ["EFG"])
            ,("  ?1", [])
            ,("",     [])
            ]
    return [(a, cs, z, antarctica.markedVote(a, cs)) for (a, z) in tests]

def test_writtenVote():
    piles = {'AB': (0, [], 0, ["AB", "EFG", "C D"]), 'C D': (0, [], 1, ["C D"]), \
             'EFG': (0, [], 2, ["EFG"]), 'HJ K': (0, [], 3, ["HJ K", "AB"])}
    tests = [("C D", ["C D"])
            ,("C d", [])
            ,("",    [])
            ]
    return [(a, piles, z, antarctica.writtenVote(a, piles)) for (a, z) in tests]

def test_paperToVote():
    cs = [('AB', '132'), ('C D', ''), ('EFG', ''), ('HJ K', '2  1')]
    piles = {'AB': (0, [], 0, ["AB", "EFG", "C D"]), 'C D': (0, [], 1, ["C D"]), \
             'EFG': (0, [], 2, ["EFG"]), 'HJ K': (0, [], 3, ["HJ K", "AB"])}
    tests = [("3142", ["C D", "HJ K", "AB", "EFG"])
            ,("4   ", ["AB"])
            ,("AB",   ["AB", "EFG", "C D"])
            ,("",     [])
            ]
    return [(a, cs, piles, z, antarctica.paperToVote(a, cs, piles)) for (a, z) in tests]

def test_distributeVotes():
    piles = {'AB': (3, [[], [], ["Y"]], 0, ["AB", "EFG", "C D"]), 'C D': (3, [[], [], []], 1, ["C D"]), \
             'EFG': (2, [["Z", "C D"], ["Z"]], 2, ["EFG"]), 'HJ K': (3, [[], [], []], 3, ["HJ K", "AB"])}
    newpiles = {'AB': (5, [[], [], ["Y"], [], ["Z"]], 0, ["AB", "EFG", "C D"]), 'C D': (3, [[], [], []], 1, ["C D"]), \
                'EFG': (2, [["Z", "C D"], ["Z"]], 2, ["EFG"]), 'HJ K': (4, [[], [], [], ["Y"]], 3, ["HJ K", "AB"])}
    tests = [([["Z", "HJ K", "Y"], ["Y"], [], ["AB"], ["AB", "Z"]], (newpiles, 2))
            ]
    return [(a, piles, z, antarctica.distributeVotes(a, piles)) for (a, z) in tests]

def test_leader():
    piles = {'AB': (2, [[], []], 0, ["AB", "EFG", "C D"]), 'C D': (3, [[], [], []], 1, ["C D"]), \
             'EFG': (1, [["Z", "C D"]], 2, ["EFG"]), 'HJ K': (2, [[], []], 3, ["HJ K", "AB"])}
    tests = [(piles, "C D")
            ]
    return [(a, z, antarctica.leader(a)) for (a, z) in tests]

def test_loser():
    piles = {'AB': (2, [[], []], 0, ["AB", "EFG", "C D"]), 'C D': (3, [[], [], []], 1, ["C D"]), \
             'EFG': (1, [["Z", "C D"]], 2, ["EFG"]), 'HJ K': (2, [[], []], 3, ["HJ K", "AB"])}
    tests = [(piles, "EFG")
            ]
    return [(a, z, antarctica.loser(a)) for (a, z) in tests]

def test_nextRound():
    piles = {'AB': (3, [[], [], []], 0, ["AB", "EFG", "C D"]), 'C D': (3, [[], [], ["Z"]], 1, ["C D"]), \
             'EFG': (2, [["Z", "C D"], ["Z"]], 2, ["EFG"]), 'HJ K': (3, [[], [], []], 3, ["HJ K", "AB"])}
    newpiles = {'AB': (3, [[], [], []], 0, ["AB", "EFG", "C D"]), 'C D': (4, [[], [], ["Z"], []], 1, ["C D"]), \
                'HJ K': (3, [[], [], []], 3, ["HJ K", "AB"])}
    tests = [(piles, (newpiles, 1))
            ]
    return [(a, z, antarctica.nextRound(a)) for (a, z) in tests]

def msgs(f, ts):
    if ts == []:
        print(f + " untested")
    elif all([t[-1] == t[-2] for t in ts]):
        print(f + " passed all " + str(len(ts)) + " test(s)")
    else:
        for t in ts:
            if t[-1] != t[-2]:
                args = str(t[0:-2])[1:-1].rstrip(",")
                print(f + "(" + args + ") returns " + str(t[-1]) \
                + " instead of " + str(t[-2]))

print("Project 2 testing program, v" + str(version))
print()
print("This is a minimal testing program: add (many of!) your own tests")
print("if you want to be confident that your program works correctly")
print()

msgs("lines",           test_lines())
msgs("candidates",      test_candidates())
msgs("rankedVote",      test_rankedVote())
msgs("zeroElection",    test_zeroElection())
msgs("markedVote",      test_markedVote())
msgs("writtenVote",     test_writtenVote())
msgs("paperToVote",     test_paperToVote())
msgs("distributeVotes", test_distributeVotes())
msgs("leader",          test_leader())
msgs("loser",           test_loser())
msgs("nextRound",       test_nextRound())
print("displayStandings untested")
print("main untested")
print()
print("Now we shall run your program")
print()
antarctica.main()
input("Close testing program? ")
