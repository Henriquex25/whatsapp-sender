import requests
import os
import re


class ZAPIClient:
    def __init__(self):
        instance = os.getenv('ZAPI_INSTANCE')

        self._base_url = f"https://api.z-api.io/instances/{instance}"
        self._headers = {"Content-Type": "application/json"}
        self.__instance_token = os.getenv('ZAPI_INSTANCE_TOKEN')
        self.__client_token = os.getenv('ZAPI_CLIENT_TOKEN')

    def __validate_message(self, message: str) -> bool:
        message_clean = message.strip()

        # Verifica se os campos obrigatórios existem
        if not message_clean:
            print("❌ Dados incompletos: A mensagem é obrigatória.")
            return False

        return True

    def __validate_cell_number(self, cell_number: str) -> bool:
        # Verifica se os campos obrigatórios existem
        if not cell_number:
            print("❌ Dados incompletos: O número de telefone é obrigatório.")
            return False

        # Trata o telefone
        cell_number_clean = cell_number.strip()

        # Remove caracteres não numéricos
        cell_number_clean = re.sub(r'[^0-9]', '', cell_number_clean)

        # Verifica tamanho mínimo (11 dígitos com DDD)
        if len(cell_number_clean) < 11:
            print(f"Telefone inválido. O número de celular deve conter no mínimo 11 dígitos (com DDD): {cell_number_clean}")
            return False

        if len(cell_number_clean) > 13:
            print(f"Telefone inválido. O número de celular deve conter no máximo 13 dígitos (com DDI e DDD): {cell_number_clean}")
            return False

        return True

    def __resolve_cell_number_ddi(self, cell_number: str) -> str:
        if len(cell_number) == 11:
            return f"55{cell_number}"

        return cell_number

    def __resolve_message(self, message: str, costumer_name: str) -> str:
        return message.replace("[customer_name]", costumer_name)

    def send_message(self, cell_phone: str, customer_name: str, message: str) -> bool:
        if not self.__validate_message(message) or not self.__validate_cell_number(cell_phone):
            return False

        url = f"{self._base_url}/token/{self.__instance_token}/send-text"

        headers = {
            **self._headers,
            "Client-Token": self.__client_token
        }

        payload = {
            "phone": self.__resolve_cell_number_ddi(cell_phone),
            "message": self.__resolve_message(message, customer_name)
        }

        try:
            response = requests.post(url, json=payload, headers=headers)

            return response.status_code == 200
        except Exception as e:
            print(f"❌ Falha ao enviar mensagem: {e}")
            return False