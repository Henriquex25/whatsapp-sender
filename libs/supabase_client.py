from supabase import create_client
import os

class SupabaseClient:
    def __init__(self):
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_KEY')

        self.client = create_client(url,key)

    def fetch_data(self, table_name: str) -> list:
        try:
            response = (
                self.client
                    .table(table_name)
                    .select("id, cell_number, customer_name, sent, message(id, body)")
                    .eq("sent", False)
                    .execute()
            )
            return response.data
        except Exception as e:
            print(f"❌ Erro ao buscar os dados: {e}")
            return []

    def mark_as_sent(self, message_id: int) -> None:
        try:
            (
                self.client
                    .table("sent_messages")
                    .update({"sent": True})
                    .eq("id", message_id)
                    .execute()
            )
        except Exception as e:
            print(f"❌ Erro ao marcar a mensagem como enviada: {e}")
