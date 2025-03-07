import pytest
from lib.models import Game
from lib.seed import session

def test_seed_creates_games():
    # Test that games were created
    games = session.query(Game).all()
    assert len(games) > 0

def test_game_attributes():
    # Test that games have valid attributes
    game = session.query(Game).first()
    assert isinstance(game.title, str)
    assert isinstance(game.genre, str)
    assert isinstance(game.platform, str)
    assert isinstance(game.price, int)
    assert 0 <= game.price <= 60