#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # выполнять откат цепи после завершения каждого теста, чтобы обеспечить надлежащую изоляцию
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def ballot(Ballot, accounts):
    return Ballot.deploy([("BTC rules!").encode('utf-8'), ("ETH rules too!").encode('utf-8')], {'from': accounts[0]}) 

