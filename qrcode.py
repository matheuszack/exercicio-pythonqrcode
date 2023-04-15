# Importar a biblioteca qrcode
import qrcode

# Solicitar o texto para gerar o código QR
texto = input("Digite o texto para gerar o código QR: ")

# Criar o objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionar os dados ao objeto QRCode
qr.add_data(texto)
qr.make(fit=True)

# Criar a imagem do código QR
img = qr.make_image(fill_color="black", back_color="white")

# Salvar a imagem do código QR em um arquivo PNG
nome_arquivo = input("Digite o nome do arquivo de saída (sem a extensão): ")
img.save(nome_arquivo + ".png")

print("O código QR foi gerado com sucesso!")
