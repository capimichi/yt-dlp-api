import mimetypes
from injector import inject
from fastapi import APIRouter, HTTPException, status, Query
from fastapi.responses import StreamingResponse  # Import necessario
from ytdlpapi.service.download_service import DownloadService  # Import del service


class DownloadController:

    @inject
    def __init__(self, download_service: DownloadService):
        self.router = APIRouter(prefix="/download", tags=["Download"])
        self.download_service = download_service  # Inizializzazione del service
        self._register_routes()
    
    def _register_routes(self):
        """Registra le rotte per il controller"""
        self.router.add_api_route("", self.get_download, methods=["GET"])

    async def get_download(
            self,
            url: str = Query(..., description="URL del contenuto da scaricare"),
            format: str = Query(None, description="Formato opzionale del contenuto"),
            playlistend: int = Query(None, description="Numero massimo di elementi della playlist da scaricare")
    ):
        """Scarica il video e lo restituisce come streaming response"""
        try:
            file_path = await self.download_service.download_video(url, format, playlistend)  # Chiamata al service

            def iter_file():
                with open(file_path, "rb") as file:
                    yield from file

            return StreamingResponse(
                iter_file(),  
                media_type=mimetypes.guess_type(file_path)[0] or "application/octet-stream",
                headers={"Content-Disposition": f"attachment; filename={file_path.split('/')[-1]}"}
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    