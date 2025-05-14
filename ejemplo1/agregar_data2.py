import pandas as pd
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Leer archivo con separador '|'
df = pd.read_csv("data/saludos_mundo.csv", sep='|')

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Recorrer el DataFrame y crear objetos Saludo2
for _, row in df.iterrows():
    saludo = Saludo2(
        mensaje=row['saludo'],
        tipo=row['tipo'],
        origen=row['origen']
    )
    session.add(saludo)

# Confirmar transacciones
session.commit()
