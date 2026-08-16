"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add, clamp  # noqa: E402


def test_add() -> None:
    assert add(2, 3) == 5


def test_clamp_within_range() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range() -> None:
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_range() -> None:
    assert clamp(11, 0, 10) == 10
