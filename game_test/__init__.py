
from gym.envs.registration import register


register(
    id = "testgame-v1",
    entry_point = "game_test.env:TestGame",
    kwargs = {}
)