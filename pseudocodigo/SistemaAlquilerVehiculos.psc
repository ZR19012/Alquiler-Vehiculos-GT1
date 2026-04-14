Proceso SistemaAlquilerVehiculos
	
    Definir opcion, i Como Entero
    Definir vehiculoMarca, vehiculoTipo Como Cadena
    Definir vehiculoAnio Como Entero
    Definir vehiculoEstado Como Cadena
	
    Dimension vehiculoMarca[8]
    Dimension vehiculoTipo[8]
    Dimension vehiculoAnio[8]
    Dimension vehiculoEstado[8]
	
    vehiculoMarca[1] <- "Toyota"
    vehiculoTipo[1] <- "Sedan"
    vehiculoAnio[1] <- 2020
    vehiculoEstado[1] <- "Disponible"
	
    vehiculoMarca[2] <- "Nissan"
    vehiculoTipo[2] <- "Sedan"
    vehiculoAnio[2] <- 2021
    vehiculoEstado[2] <- "Disponible"
	
    vehiculoMarca[3] <- "Ford"
    vehiculoTipo[3] <- "Pickup"
    vehiculoAnio[3] <- 2019
    vehiculoEstado[3] <- "Disponible"
	
    vehiculoMarca[4] <- "Chevrolet"
    vehiculoTipo[4] <- "Pickup"
    vehiculoAnio[4] <- 2022
    vehiculoEstado[4] <- "Disponible"
	
    vehiculoMarca[5] <- "Volvo"
    vehiculoTipo[5] <- "Camion"
    vehiculoAnio[5] <- 2018
    vehiculoEstado[5] <- "Disponible"
	
    vehiculoMarca[6] <- "Isuzu"
    vehiculoTipo[6] <- "Camion"
    vehiculoAnio[6] <- 2020
    vehiculoEstado[6] <- "Disponible"
	
    vehiculoMarca[7] <- "Hyundai"
    vehiculoTipo[7] <- "Microbus"
    vehiculoAnio[7] <- 2021
    vehiculoEstado[7] <- "Disponible"
	
    vehiculoMarca[8] <- "Mercedes"
    vehiculoTipo[8] <- "Microbus"
    vehiculoAnio[8] <- 2022
    vehiculoEstado[8] <- "Disponible"
	
    Repetir
		
        Escribir "===== SISTEMA DE ALQUILER ====="
        Escribir "1. Ver vehiculos"
        Escribir "2. Reservar vehiculo"
        Escribir "3. Cambiar estado"
        Escribir "4. Salir"
        Leer opcion
		
        Segun opcion Hacer
			
            1:
                Para i <- 1 Hasta 8 Hacer
                    Escribir i, ". ", vehiculoMarca[i], " - ", vehiculoTipo[i], " - ", vehiculoAnio[i], " - ", vehiculoEstado[i]
                FinPara
				
            2:
                Escribir "Seleccione numero de vehiculo:"
                Leer i
				
                Si vehiculoEstado[i] = "Disponible" Entonces
                    vehiculoEstado[i] <- "Alquilado"
                    Escribir "Vehiculo reservado correctamente"
                SiNo
                    Escribir "Vehiculo no disponible"
                FinSi
				
            3:
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
				
            4:
                Escribir "Saliendo del sistema"
				
            De Otro Modo:
                Escribir "Opcion invalida"
				
        FinSegun
		
    Hasta Que opcion = 4
	
FinProceso