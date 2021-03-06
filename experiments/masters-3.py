"""
- DQN
- DQN + prioritized replay
- DQN with regular experience sharing
- DQN with regular experience sharing + prioritized replay
- DQN with focused experience sharing
- DQN with focused experience sharing + prioritized replay

First version of experiments
Using simple control problems in OpenAI, specifically CartPole
General guideline is:
- hyperparameters are the same for most experiments
- for a few experiments, they will change, when necessary

improve how it is done later

"""




from fasterrl.common.experiment import UntilWinExperiment, MultiAgentExperiment

# tuned based on intuition - not really sure

# base DQN
dqn = {
    "PLATFORM": "openai",
    "ENV_NAME": "MountainCar-v0",
    "METHOD": "DQN",
    "LOGGER_METHOD": "DQNLogger",
    "NETWORK_TYPE": "SimpleValueNetwork",
    "REPORTING_INTERVAL": 40,
    "LOG_LEVEL": 2,
    "NUMBER_EPISODES_MEAN": 10,
    "MEAN_REWARD_BOUND": -110,
    "NUM_TRIALS": 4,
    "MAX_EPISODES": 2000, # limited for performance
    "EPSILON_DECAY_LAST_FRAME": 80000, # multiplied by 20. need more exploration.
    "EPSILON_START": 1.0,
    "EPSILON_FINAL": 0.02, # leave some exploration
    "LEARNING_RATE": 5e-4, # halved, since more tries
    "GAMMA": 0.995, # halved the remaining difference, account for temporally spaced reward
    "REPLAY_BATCH_SIZE": 32,
    "EXPERIENCE_BUFFER_SIZE": 400000, # multiplied by 20
    "GRADIENT_CLIPPING": False,
    "DOUBLE_QLEARNING": True,
    "SOFT_UPDATE": True,
    "SOFT_UPDATE_TAU": 5e-3,
}

prio = {
    "PRIORITIZED_REPLAY": True,
    "PRIO_REPLAY_ALPHA": 0.6,
    "PRIO_REPLAY_BETA_START": 0.4,
    "PRIO_REPLAY_BETA_FRAMES": 200000, # multiplied by 20
}

dqn_prio = dqn.copy()
dqn_prio.update(prio)

sharing = {
    "NUM_AGENTS": 2,
    "SHARE_BATCH_SIZE": 128,
    "SHARING": True,
    "NUM_TRIALS": 2,
}

dqn_sharing = dqn.copy()
dqn_sharing.update(sharing)

focus = {
    "FOCUSED_SHARING": True,
    "FOCUSED_SHARING_THRESHOLD": 40, # multiplied by 4 the threshold
}

dqn_focus_sharing = dqn_sharing.copy()
dqn_focus_sharing.update(focus)


# others
dqn_prio_sharing = dqn_sharing.copy()
dqn_prio_sharing.update(prio)

dqn_prio_focus_sharing = dqn_sharing.copy()
dqn_prio_focus_sharing.update(prio)
dqn_prio_focus_sharing.update(focus)

## prepare the experiment
exp_group = 'masters3-mountaincar'
experiments = {
    'dqn': dqn,
    'dqn_prio': dqn_prio,
    'dqn_sharing': dqn_sharing,
    'dqn_prio_sharing': dqn_prio_sharing,
    'dqn_focus_sharing': dqn_focus_sharing,
    'dqn_prio_focus_sharing': dqn_prio_focus_sharing,
}

for exp_name, params in experiments.items():
    print(exp_name, params)
    if 'sharing' in exp_name:
        exp = MultiAgentExperiment(params, exp_name, exp_group)
    else:
        exp = UntilWinExperiment(params, exp_name, exp_group)
    exp.run()
