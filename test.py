import game_test.env
import gym
import numpy as np

def attacker_policy(state):
    if np.random.rand() > 0.95:
        return 1
    return 0

def defender_policy(state):
    if np.random.rand() > 0.95:
        return 1
    return 0

def test():
    env = gym.make("testgame-v1")

    done = False
    s = env.reset()
    while not done:
        attacker_action = attacker_policy(s)
        defender_action = defender_policy(s)
        a = (attacker_action, defender_action)
        s, r, done, info = env.step(a)
        print(f"attacker_action:{attacker_action}, defender_action:{defender_action}, s:{s}, r:{r}, done:{done}, info:{info}")


if __name__ == '__main__':
    test()