#!/usr/bin/python3

from brownie import Ballot, accounts


def main():
    return Ballot.deploy([("BTC rules!").encode('utf-8'), ("ETH rules too!").encode('utf-8')], {'from': accounts[0]}) 
