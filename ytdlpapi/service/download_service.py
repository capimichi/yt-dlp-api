from injector import inject
from ytdlpapi.client.yt_dlp_client import YtDlpClient


class DownloadService:

    @inject
    def __init__(self, yt_dlp_client: YtDlpClient):
        self.yt_dlp_client = yt_dlp_client

    async def download_video(self, url: str, format: str = None, playlistend: int = None) -> str:
        """
        Scarica un video utilizzando YtDlpClient.
        Args:
            url (str): URL del video da scaricare.
            format (str): Formato opzionale del video.
            playlistend (int): Numero massimo di elementi della playlist da scaricare.
        Returns:
            str: Percorso del file scaricato.
        """
        return self.yt_dlp_client.download_video(url, format, playlistend)
