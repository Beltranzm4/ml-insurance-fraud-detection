from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# Variables con orden natural: se codifican como números 0, 1, 2...
ORDINALES = {
    'AgeOfVehicle': ['new', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', 'more than 7'],
    'AgeOfPolicyHolder': ['16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40', '41 to 50', '51 to 65', 'over 65'],
    'VehiclePrice': ['less than 20000', '20000 to 29000', '30000 to 39000', '40000 to 59000', '60000 to 69000', 'more than 69000'],
    'PastNumberOfClaims': ['none', '1', '2 to 4', 'more than 4'],
    'Days_Policy_Accident': ['none', '1 to 7', '8 to 15', '15 to 30', 'more than 30'],
    'Days_Policy_Claim': ['8 to 15', '15 to 30', 'more than 30'],
}

# Variables sin orden: one-hot. Las categorías con menos de 100 casos en train se agrupan en "Otras".
NOMINALES = ['Make', 'AccidentArea', 'Sex', 'Fault', 'VehicleCategory', 'BasePolicy', 'AgentType',
             'Deductible', 'AddressChange_Claim', 'Month', 'MonthClaimed']

# Ya son numéricas (Age conserva sus NaN)
NUMERICAS = ['Age', 'retraso_meses']

COLUMNAS = list(ORDINALES) + NOMINALES + NUMERICAS


def crear_preprocesador(columnas=COLUMNAS):
    """Preprocesador para el subconjunto `columnas` (por defecto, todas)."""
    ordinales = {c: o for c, o in ORDINALES.items() if c in columnas}
    nominales = [c for c in NOMINALES if c in columnas]
    numericas = [c for c in NUMERICAS if c in columnas]
    return ColumnTransformer([
        ('ordinales', OrdinalEncoder(categories=list(ordinales.values()),
                                     handle_unknown='use_encoded_value', unknown_value=float('nan')), list(ordinales)),
        ('nominales', OneHotEncoder(min_frequency=100, handle_unknown='infrequent_if_exist', sparse_output=False), nominales),
        ('numericas', 'passthrough', numericas),
    ])
