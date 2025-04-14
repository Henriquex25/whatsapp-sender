# Exportações explícitas dos módulos
from .supabase_client import SupabaseClient
from .zapi_client import ZAPIClient

__all__ = [
    'SupabaseClient',
    'ZAPIClient',
]