// ================================================
// SISTEMA DE ALQUILER DE VEHÍCULOS
// Proyecto Final - Lógica de Programación
// GT1
// ================================================

//Compara dos rangos de fechas y determina si no chocan. Retorna verdadero si esta disponible.
Funcion disponible <- VerificarDisponibilidad(fechaIniSolicitud, fechaFinSolicitud, fechaIniReserva, fechaFinReserva)
	Si (fechaFinSolicitud < fechaIniReserva) O (fechaIniSolicitud > fechaFinReserva) Entonces
		disponible <- VERDADERO
	SiNo
		disponible <- FALSO
	FinSi
FinFuncion

//Recorre todas las reservas existentes y verifica si un vehículo específico está libre en esas fechas.
//Retorna verdadero si el vehiculo esta disponible en esas fechas.
Funcion resultado <- VehiculoDisponibleEnFechas(idVehiculo, fechaIniSolicitada, fechaFinSolicitada, vectorIdVechiculoReservado, vectorFechaIniReservado, vectorFechaFinReservado, totalRes)
	resultado <- VERDADERO
	Para i <- 1 Hasta totalRes Con Paso 1 Hacer
		Si vectorIdVechiculoReservado[i] = idVehiculo Entonces
			Si VerificarDisponibilidad(fechaIniSolicitada, fechaFinSolicitada, vectorFechaIniReservado[i], vectorFechaFinReservado[i]) = FALSO Entonces
				resultado <- FALSO
			FinSi
		FinSi
	FinPara
FinFuncion

//Busca un vehículo por su ID y devuelve su posición en el vector.
Funcion indice <- BuscarVehiculo(idBuscado, vectorIdTotal, total)
	indice <- -1
	Para i <- 1 Hasta total Con Paso 1 Hacer
		Si vectorIdTotal[i] = idBuscado Entonces
			indice <- i
		FinSi
	FinPara
FinFuncion

Proceso SistemaAlquilerVehiculos
	
	// ---- Datos de vehículos ----
	Dimension vectorIdTotal[5], marcas[5], modelos[5], estados[5]
	vectorIdTotal[1] <- 101
	marcas[1] <- "Toyota"  
	modelos[1] <- "Corolla"  
	estados[1] <- "Disponible"
	
	vectorIdTotal[2] <- 102  
	marcas[2] <- "Honda"   
	modelos[2] <- "Civic"  
	estados[2] <- "Alquilado"
	
	vectorIdTotal[3] <- 103  
	marcas[3] <- "Nissan"  
	modelos[3] <- "Sentra"   
	estados[3] <- "Disponible"
	
	vectorIdTotal[4] <- 104  
	marcas[4] <- "Ford"    
	modelos[4] <- "Mustang"  
	estados[4] <- "En Mantenimiento"
	
	vectorIdTotal[5] <- 105  
	marcas[5] <- "Kia"     
	modelos[5] <- "Rio"      
	estados[5] <- "Disponible"
	
	totalVehiculos <- 5
	
	// ---- Reservas registradas ----
	Dimension vectorIdVechiculoReservado[20], clientesRes[20], vectorFechaIniReservado[20], vectorFechaFinReservado[20]
	
	vectorIdVechiculoReservado[1] <- 101  
	clientesRes[1] <- "Carlos Perez"   
	vectorFechaIniReservado[1] <- 20250110  
	vectorFechaFinReservado[1] <- 20250115
	vectorIdVechiculoReservado[2] <- 103  
	clientesRes[2] <- "Ana Gonzalez"   
	vectorFechaIniReservado[2] <- 20250120  
	vectorFechaFinReservado[2] <- 20250125
	totalReservas <- 2
	
	// ---- Menú principal ----
	
	
		Mientras opcion <> 5 Hacer
			
			Escribir ""
			Escribir "========================================="
			Escribir "    SISTEMA DE ALQUILER DE VEHICULOS"
			Escribir "========================================="
			Escribir "  1. Consultar disponibilidad"
			Escribir "  2. Registrar nueva reserva"
			Escribir "  3. Ver todas las reservas"
			Escribir "  4. Cancelar una reserva"
			Escribir "  5. Salir"
			Escribir "-----------------------------------------"
			Escribir "Seleccione una opcion: "
			Leer opcion
			
			Segun opcion Hacer
				
				1:
					// ================================================
					// MODULO 1 - CONSULTA DE DISPONIBILIDAD
					// ================================================
					Escribir ""
					Escribir "--- CONSULTAR DISPONIBILIDAD ---"
					Escribir "Fecha de inicio (AAAAMMDD): "
					Leer fechaIniSolicitada
					Escribir "Fecha de fin    (AAAAMMDD): "
					Leer fechaFinSolicitada
					
					Si fechaFinSolicitada <= fechaIniSolicitada Entonces
						Escribir "ERROR: La fecha de fin debe ser mayor a la de inicio."
					SiNo
						Escribir ""
						Escribir "-----------------------------------------"
						Escribir "  Vehiculos disponibles para esas fechas:"
						Escribir "-----------------------------------------"
						hayDisponibles <- FALSO
						
						Para i <- 1 Hasta totalVehiculos Con Paso 1 Hacer
							Si estados[i] = "Disponible" Entonces
								Si VehiculoDisponibleEnFechas(vectorIdTotal[i], fechaIniSolicitada, fechaFinSolicitada, vectorIdVechiculoReservado, vectorFechaIniReservado, vectorFechaFinReservado, totalReservas) Entonces
									Escribir "  ID: ", vectorIdTotal[i], " | ", marcas[i], " ", modelos[i]
									hayDisponibles <- VERDADERO
								FinSi
							FinSi
						FinPara
						
						Si hayDisponibles = FALSO Entonces
							Escribir "  No hay vehiculos disponibles para esas fechas."
						FinSi
						Escribir "-----------------------------------------"
					FinSi
					
				2:
					// ================================================
					// MODULO 2 - REGISTRAR NUEVA RESERVA
					// ================================================
					Escribir ""
					Escribir "--- NUEVA RESERVA ---"
					Escribir "Nombre del cliente: "
					Leer nombreCliente
					Escribir "ID del vehiculo a reservar: "
					Leer vectorIdTotalolicitado
					
					pos <- BuscarVehiculo(vectorIdTotalolicitado, vectorIdTotal, totalVehiculos)
					
					Si pos = -1 Entonces
						Escribir "ERROR: Vehiculo no encontrado."
					SiNo
						Si estados[pos] <> "Disponible" Entonces
							Escribir "ERROR: El vehiculo no esta disponible."
							Escribir "       Estado actual: ", estados[pos]
						SiNo
							Escribir "Fecha de inicio (AAAAMMDD): "
							Leer fechaIniSolicitada
							Escribir "Fecha de fin    (AAAAMMDD): "
							Leer fechaFinSolicitada
							
							Si fechaFinSolicitada <= fechaIniSolicitada Entonces
								Escribir "ERROR: La fecha de fin debe ser mayor a la de inicio."
							SiNo
								Si VehiculoDisponibleEnFechas(vectorIdTotalolicitado, fechaIniSolicitada, fechaFinSolicitada, vectorIdVechiculoReservado, vectorFechaIniReservado, vectorFechaFinReservado, totalReservas) Entonces
									totalReservas <- totalReservas + 1
									vectorIdVechiculoReservado[totalReservas]      <- vectorIdTotalolicitado
									clientesRes[totalReservas] <- nombreCliente
									vectorFechaIniReservado[totalReservas]     <- fechaIniSolicitada
									vectorFechaFinReservado[totalReservas]    <- fechaFinSolicitada
									estados[pos] <- "Alquilado"
									Escribir "Reserva registrada exitosamente para ", nombreCliente
								SiNo
									Escribir "ERROR: El vehiculo ya tiene una reserva en esas fechas."
								FinSi
							FinSi
						FinSi
					FinSi
					
				3:
					// ================================================
					// MODULO 3 - VER TODAS LAS RESERVAS
					// ================================================
					Escribir ""
					Escribir "--- RESERVAS REGISTRADAS ---"
					
					Si totalReservas = 0 Entonces
						Escribir "No hay reservas registradas."
					SiNo
						Para i <- 1 Hasta totalReservas Con Paso 1 Hacer
							Escribir "  Reserva #", i
							Escribir "    Cliente  : ", clientesRes[i]
							Escribir "    Vehiculo : ID ", vectorIdVechiculoReservado[i]
							Escribir "    Desde    : ", vectorFechaIniReservado[i]
							Escribir "    Hasta    : ", vectorFechaFinReservado[i]
							Escribir "  -------------------------"
						FinPara
					FinSi
					
				4:
					// ================================================
					// MODULO 4 - CANCELAR RESERVA
					// ================================================
					Escribir ""
					Escribir "--- CANCELAR RESERVA ---"
					
					Si totalReservas = 0 Entonces
						Escribir "No hay reservas para cancelar."
					SiNo
						Escribir "Numero de reserva a cancelar (1-", totalReservas, "): "
						Leer numCancelar
						
						Si numCancelar < 1 O numCancelar > totalReservas Entonces
							Escribir "ERROR: Numero de reserva invalido."
						SiNo
							posV <- BuscarVehiculo(vectorIdVechiculoReservado[numCancelar], vectorIdTotal, totalVehiculos)
							Si posV <> -1 Entonces
								estados[posV] <- "Disponible"
							FinSi
							
							Para i <- numCancelar Hasta totalReservas - 1 Con Paso 1 Hacer
								vectorIdVechiculoReservado[i]      <- vectorIdVechiculoReservado[i+1]
								clientesRes[i] <- clientesRes[i+1]
								vectorFechaIniReservado[i]     <- vectorFechaIniReservado[i+1]
								vectorFechaFinReservado[i]    <- vectorFechaFinReservado[i+1]
							FinPara
							totalReservas <- totalReservas - 1
							Escribir "Reserva cancelada. Vehiculo liberado."
						FinSi
					FinSi
					
				5:
					Escribir "Saliendo del sistema. Hasta luego!"
					
				De Otro Modo:
					Escribir "Opcion invalida. Intente de nuevo."
					
			FinSegun
		FinMientras
	
FinProceso