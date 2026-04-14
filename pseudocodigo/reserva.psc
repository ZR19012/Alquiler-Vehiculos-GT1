Proceso ReservaVehiculo
    Definir i Como Entero
    Definir opcion Como Entero
	
    Escribir "Seleccione el vehiculo que desea reservar:"
    Leer i
	
    Si vehiculoEstado[i] = "Disponible" Entonces
        vehiculoEstado[i] <- "Alquilado"
        Escribir "Reserva realizada correctamente"
    SiNo
        Escribir "El vehiculo no esta disponible para reserva"
    FinSi
	
FinProceso