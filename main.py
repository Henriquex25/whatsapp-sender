import time
from libs.supabase_client import SupabaseClient
from libs.zapi_client import ZAPIClient
import random
from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    # Inicializa os clientes
    supabase = SupabaseClient()
    zapi = ZAPIClient()

    # busca os dados
    data = supabase.fetch_data("sent_messages")

    if not data:
        print("Nenhum dado encontrado. 🫤")

    # Envia as mensagens
    for item in data:
        if zapi.send_message(
            item["cell_number"],
            item["customer_name"],
            item["message"]['body']
        ):
            supabase.mark_as_sent(item["id"])
            print(f"✅ Mensagem enviada com sucesso para o número {item['cell_number']}.")
        else:
            print(f"❌ Erro ao enviar mensagem para o número {item['cell_number']}.")

        pause = random.uniform(2, 5)
        time.sleep(pause)

    print("✅ Processo concluído!")

if __name__ == "__main__":
    main()