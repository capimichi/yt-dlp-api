from injector import inject
from ytdlpapi.client.yt_dlp_client import YtDlpClient


class InfoService:

    @inject
    def __init__(self, yt_dlp_client: YtDlpClient):
        self.yt_dlp_client = yt_dlp_client

    async def get_info(self, url: str) -> dict:
        """
        Ottiene le informazioni di un video utilizzando YtDlpClient.
        Args:
            url (str): URL del video da analizzare.
        Returns:
            dict: Dizionario contenente le informazioni del video.
        """
        return self.yt_dlp_client.get_info(url)
