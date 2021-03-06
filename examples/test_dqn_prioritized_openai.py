


from fasterrl.common.experiment import UntilWinExperiment, MultiAgentExperiment

params = {
    "PLATFORM": "openai",
    "ENV_NAME": "CartPole-v0",
    "METHOD": "DQN",
    "LOGGER_METHOD": "DQNLogger",
    "NETWORK_TYPE": "SimpleValueNetwork",
    "REPORTING_INTERVAL": 10,
    "LOG_LEVEL": 2, #debugging level
    "NUMBER_EPISODES_MEAN": 10,
    "MEAN_REWARD_BOUND": 130, # 199,
    "NUM_TRIALS": 2, # 10,
    "MAX_EPISODES": 3000,
    "EPSILON_DECAY_LAST_FRAME": 4000, # 4000
    "EPSILON_START": 1.0,
    "EPSILON_FINAL": 0,
    "LEARNING_RATE": 1e-3,
    "GAMMA": 0.99,
    "REPLAY_BATCH_SIZE": 32,
    "EXPERIENCE_BUFFER_SIZE": 50000, # increased from 5000 to 50000
    "GRADIENT_CLIPPING": False,
    "DOUBLE_QLEARNING": True,
    "SOFT_UPDATE": True,
    "SOFT_UPDATE_TAU": 5e-3,
    "PRIORITIZED_REPLAY": True,
    "PRIO_REPLAY_ALPHA": 0.6,
    "PRIO_REPLAY_BETA_START": 0.4,
    "PRIO_REPLAY_BETA_FRAMES": 10000,
}

exp = UntilWinExperiment(params)

# add sharing
new_params = {
    "NUM_AGENTS": 2,
    "SHARE_BATCH_SIZE": 128,
    "SHARING": True,
    "FOCUSED_SHARING": True,
    "FOCUSED_SHARING_THRESHOLD": 3,
}
params.update(new_params)
exp = MultiAgentExperiment(params)

result = exp.run()
print("Method {} took an average of {:.2f} episodes".format(params["METHOD"], result))

# Method DQN took an average of 263.90 episodes

# Method DQN took an average of 145.40 episodes
# with a much larger buffer and prioritized replay



# Meth
