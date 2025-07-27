from yt_dlp import YoutubeDL
from injector import inject
from ytdlpapi.model.default_logger import DefaultLogger
from ytdlpapi.model.proxy import Proxy


class YtDlpClient:

    @inject
    def __init__(self, proxy: Proxy, tmp_dir: str, default_logger: DefaultLogger):
        self.proxy = proxy
        self.tmp_dir = tmp_dir
        self.logger = default_logger

    def _get_options(self, format: str = 'best') -> dict:
        """
        Prepara le opzioni comuni per yt-dlp.
        Args:
            format (str): Formato del video (default: 'best').
        Returns:
            dict: Dizionario delle opzioni.
        """
        options = {
            'quiet': False,
            'no_warnings': False,
            'format': format,
            'logger': self.logger,
        }
        if self.proxy.get_proxy():
            options['proxy'] = self.proxy.get_proxy()
        return options

    def download_video(self, url: str, format: str = None) -> str:
        """
        Scarica un video utilizzando yt-dlp.
        Args:
            url (str): URL del video da scaricare.
            format (str): Formato opzionale del video.
        Returns:
            str: Percorso del file scaricato.
        """
        options = self._get_options(format or 'best')
        options['outtmpl'] = f'{self.tmp_dir}/%(title)s.%(ext)s'  # Salva il file nella tmp_dir
        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info)
        except Exception as e:
            raise Exception(f"Errore durante il download del video: {str(e)}")

    def get_info(self, url: str) -> dict:
        """
        Ottiene le informazioni di un video utilizzando yt-dlp.
        Args:
            url (str): URL del video da analizzare.
        Returns:
            dict: Dizionario contenente le informazioni del video.
        """
        options = self._get_options()
        try:
            with YoutubeDL(options) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            raise Exception(f"Errore durante l'esecuzione di yt-dlp: {str(e)}")
