"""Tests for CQ - Practice with conditionals, local variables, and user input."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"

import pytest
import re
from pytest import mark
from graders.helpers import assert_parameter_list, author_is_a_valid_pid, reimport_module
from graders.helpers import set_stdin, assert_return_type
from re import Pattern
from typing import Any
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

MODULE = "CQs/cq02_conditionals.py"
module: Any

def _regex_test_stdout(lines: list[str], regex: Pattern[Any]):
    match = False
    for line in lines:
        if regex.search(line) is not None:
            match = True
    assert match
  
def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines

@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)

@mark.weight(1)
def test_guess_a_number_params():
    """guess_a_number should take no inputs."""
    module = reimport_module(MODULE)
    assert_parameter_list(module.guess_a_number, [None])

@mark.weight(1)
def test_guess_a_number_return_type():
    """guess_a_number should return NoneType."""
    module = reimport_module(MODULE)
    assert_return_type(module.guess_a_number, None)

@mark.weight(1)
def test_guess_a_number_output_correct(capsys, monkeypatch):
    """Testing that guess_a_number has the correct output for a specific guess."""
    module = reimport_module(MODULE)

    # Test when guess is correct
    set_stdin(monkeypatch, ["7"])
    module.guess_a_number()
    out = _get_output(capsys)
    assert "You got it!" in out[-1]

    # Test when guess is too low
    set_stdin(monkeypatch, ["3"])
    module.guess_a_number()
    out = _get_output(capsys)
    assert "Your guess was too low! The secret number is 7" in out[-1]

    # Test when guess is too high
    set_stdin(monkeypatch, ["10"])
    module.guess_a_number()
    out = _get_output(capsys)
    assert "Your guess was too high! The secret number is 7" in out[-1]

@mark.weight(1)
def test_guess_a_number_prompts_user_input(capsys, monkeypatch):
    """guess_a_number function properly prompts for user input and prints it back."""
    module = reimport_module(MODULE)

    set_stdin(monkeypatch, ["5"])
    module.guess_a_number()
    out = _get_output(capsys)
    assert "Guess a number:" in out[0]
    assert "Your guess was 5" in out[1]