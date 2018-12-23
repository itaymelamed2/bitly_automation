class Config:
    def __init__(self, env):
        """
        Creates a new config object. Based on env param.
        :param env: the required environment to supply the urls to.
        """
        base_url = "bitly.com"

        self.url = {
            "qa": f"https://qa.{base_url}",
            "production": f"https://{base_url}"
        }[env]

        self.hub_endpoint = "http://127.0.0.1:4444/wd/hub"

        self.time_out = {
            "qa": 15,
            "production": 10
        }[env]
