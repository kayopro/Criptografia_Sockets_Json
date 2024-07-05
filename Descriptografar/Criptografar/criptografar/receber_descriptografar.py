'''Lembre-se de ativar o ambiente virtual (venv) dentro da pasta antes de executar!!!'''
import json
import socket
from cryptography.fernet import Fernet

#Criar socket e configurar o servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 12345))
    s.listen()
    print("Aguardando conexões...")
    conn, addr = s.accept()

    #Receber os dados json
    with conn:
        print('Conectado por', addr)
        dados_json = conn.recv(1024)
        dados = json.loads(dados_json)

print('Você recebeu novos dados!')
print('• Chave: ' + dados['cryptographic_key'])
print('• Conteúdo cifrado: ' + dados['encrypted_content'])
print('Verifique seu diretório, um novo arquivo decifrado foi gerado!')

#Utilizar a chave enviada pelo json
chave = dados['cryptographic_key']
cipher_suite = Fernet(chave)

#Descriptografar o arquivo enviado pelo json
texto_decifrado = cipher_suite.decrypt(dados['encrypted_content'])

#Salvar o texto decifrado em um novo arquivo
with open('arquivo_decifrado.txt', 'wb') as arquivo_decifrado:
    arquivo_decifrado.write(texto_decifrado)