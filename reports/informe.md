# Detección de fraude en reclamaciones de seguro de coche

Hemos construido un modelo que ordena las reclamaciones por su riesgo de fraude: revisando solo el 20 % más sospechoso se encuentra el 60 % de todo el fraude, tres veces más que revisando al azar.

## Qué problema resuelve

Solo 6 de cada 100 reclamaciones son fraudulentas, y el equipo de investigación no puede revisarlas todas. El modelo da a cada reclamación nueva una probabilidad de fraude, para revisar primero las más sospechosas.

No decide por sí solo: señala dónde mirar. La decisión final sigue siendo de un investigador.

## Los datos

Se usaron 15.419 reclamaciones reales de seguro de coche de 1994 a 1996, de un conjunto de datos público ([Kaggle](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection)). De ellas, 923 resultaron ser fraude.

Cada reclamación describe la póliza (tipo de cobertura, franquicia), el vehículo (marca, precio, antigüedad), el asegurado (edad, sexo) y el accidente (fecha, zona, quién tuvo la culpa).

Antes de entrenar el modelo se corrigieron errores (edades a cero, nombres de marcas mal escritos, una reclamación sin fecha) y se quitaron datos que no aportaban o que podrían conocerse solo después de investigar.

El 20 % de las reclamaciones se apartó desde el principio y no se usó para nada hasta el final: los resultados de este informe se miden sobre esas reclamaciones que el modelo nunca había visto.

## Resultados

Cuantas más reclamaciones sospechosas se revisan, más fraude se encuentra, y siempre mucho más que revisando al azar.

| Reclamaciones revisadas | Fraude encontrado con el modelo | Fraude encontrado al azar |
| --- | --- | --- |
| 5 % | 23 % | 5 % |
| 10 % | 38 % | 10 % |
| 20 % | 60 % | 20 % |
| 30 % | 76 % | 30 % |

Se hicieron dos versiones del modelo, porque no sabemos si el dato de quién tuvo la culpa del accidente se conoce al abrir la reclamación. La tabla es la versión que lo usa. Sin ese dato, revisando el 20 % se encuentra el 46 % del fraude: sigue funcionando, pero peor.

## En qué se fija el modelo

Tres factores explican casi todas sus decisiones: quién tuvo la culpa, el tipo de cobertura y el tipo de vehículo.

| Factor | Más riesgo | Menos riesgo |
| --- | --- | --- |
| Culpa del accidente | Del asegurado: 8 de cada 100 son fraude | De otro conductor: menos de 1 de cada 100 |
| Tipo de cobertura | Todo riesgo: 10 de cada 100 | Solo daños a terceros: menos de 1 de cada 100 |
| Tipo de vehículo | Turismo: 8 de cada 100 | Deportivo: 2 de cada 100 |

La lógica es clara: si la culpa es de otro conductor o la póliza solo cubre daños a terceros, al asegurado no le compensa inventarse nada.

El modelo también combina señales menos frecuentes. La reclamación con más riesgo de todas (85 %) tenía un cambio de domicilio 2 o 3 años antes y una franquicia alta, dos situaciones poco habituales en las que el fraude es mucho más común. Esa reclamación era, efectivamente, un fraude.

## Cómo usarlo

La recomendación es ordenar las reclamaciones por la probabilidad que da el modelo y revisar de arriba abajo hasta donde llegue la capacidad del equipo.

Si investigar cuesta alrededor del 3 % del valor reclamado y cada fraude no detectado cuesta unas 3,75 veces lo reclamado, compensa investigar casi todo. En ese caso el modelo sirve para lo contrario: descartar con seguridad un tercio de las reclamaciones. En las pruebas, ese tercio descartado no contenía ningún fraude.

## Limitaciones

- **La culpa del accidente es clave y no sabemos cuándo se conoce.** Si la culpa se decide después de investigar, habría que usar la versión sin ese dato, que detecta menos fraude.
- **Tiene un punto ciego.** Los fraudes en pólizas de solo daños a terceros son tan raros que el modelo casi nunca los señala.
- **Los datos son antiguos (1994–1996) y de una sola fuente.** Antes de usarlo de verdad habría que entrenarlo y comprobarlo con datos actuales de la aseguradora.
- **Hay datos contradictorios.** En unas 5.000 pólizas, dos campos no coinciden en si el coche es turismo o deportivo, y no hay forma de saber cuál es el correcto.
- **Los costes son supuestos.** Las cifras de coste de investigación y de pérdida por fraude son estimaciones generales, no datos de la aseguradora.
