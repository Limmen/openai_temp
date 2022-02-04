import gym

class TestGame(gym.Env):

    def __init__(self):
        self.state = 0
        self.SERVICE_REWARD = 10
        self.INTRUSION_PENALTY = -100
        self.INTRUSION_PREVENTED = 100
        self.FALSE_ALARM_PENALTY = -100
        self.t = 0

    def step(self, action):
        attacker_action, defender_action = action
        done = False
        r = 0
        if self.state == 0 and defender_action == 1 and attacker_action == 0:
            r = self.FALSE_ALARM_PENALTY
            done = True
        elif self.state == 1 and defender_action == 1 and attacker_action == 1:
            r = self.INTRUSION_PREVENTED
            done = True
        elif self.state == 1 and defender_action == 0 and attacker_action == 0:
            r = self.INTRUSION_PENALTY + self.SERVICE_REWARD
            done = False
        elif self.state == 0 and defender_action == 0 and attacker_action == 0:
            r = self.SERVICE_REWARD
            done = False
        elif self.state == 0 and defender_action == 0 and attacker_action == 1:
            self.state = 1
            r = self.SERVICE_REWARD
            done = False
        elif self.state == 1 and attacker_action == 1:
            done = True

        info = {"t": self.t}
        self.t+=1
        return self.state, r, done, info

    def reset(self):
        self.state = 0
        self.t = 0

    def render(self):
        raise NotImplementedError("not supported")