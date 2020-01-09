from gym.envs.registration import register
 
register(id='CustomGym-v0', 
    entry_point='custom_gym.envs:CustomGymEnv', 
)