'''Lembre-se de ativar o ambiente virtual (venv) dentro da pasta antes de executar!!!'''
import json
import socket
from cryptography.fernet import Fernet

#Lista para receber a chave e o conteúdo
cryptography = {
    'cryptographic_key': None,
      'encrypted_content': None
}

#Gerar uma chave
chave = Fernet.generate_key()
cipher_suite = Fernet(chave)

#Tranformar o dado do tipo base64 para string e excluindo o prefixo (b') e o sufixo (')
chave_editada = str(chave)[2:-1]
cryptography['cryptographic_key'] = chave_editada

#Abrir, ler e criptografar o conteúdo do arquivo
with open('arquivo.txt', 'rb') as arquivo:
    texto = arquivo.read()
    texto_cifrado = cipher_suite.encrypt(texto)

    #Tranformar o dado do tipo base64 para string e excluindo o prefixo (b') e o sufixo (')
    texto_cifrado_editado = str(texto_cifrado)[2:-1]
    cryptography['encrypted_content'] = texto_cifrado_editado

'''with open('arquivo_cifrado.txt', 'wb') as arquivo_cifrado:
    arquivo_cifrado.write(texto_cifrado)'''

#Converter dicionário para JSON
cryptography_json = json.dumps(cryptography)

#Configurações do servidor
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

#Criar socket
cryptography_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Criar socket
cryptography_socket.connect((SERVER_IP, SERVER_PORT))

#Enviar JSON
cryptography_socket.send(cryptography_json.encode('utf-8'))
print('Sucesso! Os dados foram enviados.')
print('• Chave: ' + cryptography['cryptographic_key'])
print('• Conteúdo cifrado: ' + cryptography['encrypted_content'])

#Fechar o socket do cliente                      
cryptography_socket.close()