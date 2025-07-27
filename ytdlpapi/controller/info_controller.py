from injector import inject
from fastapi import APIRouter, HTTPException, status, Query
from ytdlpapi.service.info_service import InfoService  # Import del service


class InfoController:

    @inject
    def __init__(self, info_service: InfoService):
        self.router = APIRouter(prefix="/info", tags=["Info"])
        self.info_service = info_service  # Inizializzazione del service
        self._register_routes()
    
    def _register_routes(self):
        """Registra le rotte per il controller"""
        self.router.add_api_route("", self.get_info, methods=["GET"])

    async def get_info(
        self,
        url: str = Query(..., description="URL del video"),
        playlistend: int = Query(None, description="Numero massimo di elementi della playlist da analizzare")
    ):
        """Ottiene tutte le informazioni"""
        try:
            info = await self.info_service.get_info(url, playlistend)  # Chiamata al service
            return info
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

