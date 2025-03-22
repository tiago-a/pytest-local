class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment (supported envs: {SUPPORTED_ENVS})')

        self.base_url = {
            'dev': 'https://my-dev-env.com',
            'qa': 'https://my-qa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 90
        }[env]