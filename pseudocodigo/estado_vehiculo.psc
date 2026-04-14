Proceso CambiarEstadoVehiculo
    Definir i, opcion Como Entero
	
    Escribir "Seleccione vehiculo:"
    Leer i
	
    Escribir "1. Disponible"
    Escribir "2. Alquilado"
    Escribir "3. Mantenimiento"
    Leer opcion
	
    Segun opcion Hacer
        1:
            vehiculoEstado[i] <- "Disponible"
        2:
            vehiculoEstado[i] <- "Alquilado"
        3:
            vehiculoEstado[i] <- "Mantenimiento"
        De Otro Modo:
            Escribir "Opcion invalida"
    FinSegun
	
FinProceso