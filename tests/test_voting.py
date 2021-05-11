import brownie


def test_give_rights(accounts, ballot, chain):
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    
    assert ballot.voters(accounts[1])[0] == 1

def test_not_chairperson(accounts, ballot, chain):

    with brownie.reverts():
        ballot.giveRightToVote(accounts[3], {'from': accounts[1]})

def test_giverights_already_voted(accounts, ballot, chain):
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    ballot.vote(0, {'from': accounts[1]})
    
    with brownie.reverts():
        ballot.giveRightToVote(accounts[1], {'from': accounts[0]})

def test_vote(accounts, ballot):
    proposal = 1
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    ballot.vote(proposal, {'from': accounts[1]})

    assert ballot.voters(accounts[1])[1] == True
    assert ballot.voters(accounts[1])[2] == proposal
    assert ballot.proposals(proposal)[1] == ballot.voters(accounts[1])[2]

def test_vote_with_no_rights(accounts, ballot):
    
    with brownie.reverts():
        ballot.vote(1, {'from': accounts[1]})

def test_vote_with_no_rights(accounts, ballot):
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    ballot.vote(1, {'from': accounts[1]})

    with brownie.reverts():
        ballot.vote(1, {'from': accounts[1]})

def test_vote_out_of_count(accounts, ballot):
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[2], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[3], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[4], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[5], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[6], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[7], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[8], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[9], {'from': accounts[0]})
    
    with brownie.reverts():
        ballot.giveRightToVote(accounts[10], {'from': accounts[0]})



def test_results(accounts, ballot):
    ballot.giveRightToVote(accounts[1], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[2], {'from': accounts[0]})
    ballot.giveRightToVote(accounts[3], {'from': accounts[0]})

    ballot.vote(0, {'from': accounts[1]})
    ballot.vote(0, {'from': accounts[2]})
    ballot.vote(1, {'from': accounts[3]})

    assert ballot.results()[0][1] == 2
    assert ballot.results()[1][1] == 1
    # assert 1 == 2

