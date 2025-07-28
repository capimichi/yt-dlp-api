import tempfile
from yt_dlp import YoutubeDL
from injector import inject
from ytdlpapi.model.default_logger import DefaultLogger
from ytdlpapi.model.proxy import Proxy


class YtDlpClient:

    @inject
    def __init__(self, proxy: Proxy, default_logger: DefaultLogger):
        self.proxy = proxy
        self.logger = default_logger

    def _get_options(self, format: str = 'best', playlistend: int = None) -> dict:
        """
        Prepara le opzioni comuni per yt-dlp.
        Args:
            format (str): Formato del video (default: 'best').
            playlistend (int): Numero massimo di elementi della playlist.
        Returns:
            dict: Dizionario delle opzioni.
        """
        options = {
            'quiet': False,
            'no_warnings': False,
            'format': format,
            # 'logger': self.logger,
        }
        if playlistend:
            options['playlistend'] = playlistend
        if self.proxy.get_proxy():
            options['proxy'] = self.proxy.get_proxy()
        return options

    def download_video(self, url: str, format: str = None, playlistend: int = None) -> str:
        """
        Scarica un video utilizzando yt-dlp.
        Args:
            url (str): URL del video da scaricare.
            format (str): Formato opzionale del video.
            playlistend (int): Numero massimo di elementi della playlist da scaricare.
        Returns:
            str: Percorso del file scaricato.
        """
        tmp_dir = tempfile.mkdtemp()
        options = self._get_options(format or 'best', playlistend)
        options['outtmpl'] = f'{tmp_dir}/%(id)s.%(ext)s'  # Salva il file nella tmp_dir
        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info)
        except Exception as e:
            raise Exception(f"Errore durante il download del video: {str(e)}")

    def get_info(self, url: str, playlistend: int = None) -> dict:
        """
        Ottiene le informazioni di un video utilizzando yt-dlp.
        Args:
            url (str): URL del video da analizzare.
            playlistend (int): Numero massimo di elementi della playlist da analizzare.
        Returns:
            dict: Dizionario contenente le informazioni del video.
        """
        options = self._get_options(playlistend=playlistend)
        try:
            with YoutubeDL(options) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            raise Exception(f"Errore durante l'esecuzione di yt-dlp: {str(e)}")
