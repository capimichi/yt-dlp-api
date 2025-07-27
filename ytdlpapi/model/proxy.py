class Proxy:
    """
    Class to manage proxies used by yt-dlp.
    This class allows configuring a proxy for download operations.
    """

    def __init__(self, proxy_string: str):
        """
        Initializes a Proxy object with a proxy string.
        Args:
            proxy_string (str): The proxy string to use.
        """
        self.proxy_string = proxy_string

    def get_proxy(self) -> str:
        """
        Returns the proxy string.
        """
        return self.proxy_string
        
