# Gerador de longitude e latitude

import pandas as pd
import numpy as np

# Gerar dados aleatórios
np.random.seed(0)  # Para reprodutibilidade
latitudes = np.random.uniform(low=-90.0, high=90.0, size=200)
longitudes = np.random.uniform(low=-180.0, high=180.0, size=200)
descriptions = ['Avistamento de OVNI' for _ in range(200)]

# Criar DataFrame
ovni_data = pd.DataFrame({
    'ID': range(1, 201),
    'Latitude': latitudes,
    'Longitude': longitudes,
    'Descrição do Avistamento': descriptions
})

# Salvar o DataFrame como um arquivo CSV
ovni_data.to_csv('ovni_data.csv', index=False)

# Baixar o arquivo CSV para a máquina local
#from google.colab import files
#files.download('ovni_data.csv')
