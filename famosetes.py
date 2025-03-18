print("Un pequeno xogo")
deporte = input("Cual es tu deporte favorito? ")
if(deporte == "tenis"):
    país = input("En cual país prefieres vivir? ")
    if(país == "Estados unidos"):
        altura = input("Preferías ser alta?(más de 170cm) ")
        if(altura == "sí"):
            print("Eres Sera Williams la exjugadora de tenis estadounidense ganadora de 23 títulos individuales en torneos Grand Slam, con la hazaña de haber conquistado los 4 majors de manera consecutiva.")
elif(deporte == "gimnasta"):
    país = input("En cual país prefieres vivir? ")
    if(país == "Rumanía"):
        altura = input("Preferías ser alta?(más de 170cm) ")
        if(altura == "no"):
            print("Eres Nadia Elena Comaneci la exgimnasta rumana nacionalizada estadounidense. Fue una de las primeras gimnastas entrenadas por Béla Károlyi.​​ Conquistó nueve medallas olímpicas; cinco de oro. Fue la primera gimnasta que obtuvo diez puntos en una competición olímpica de gimnasia artística.")
elif(deporte == "atletismo"):
    país = input("En cual país prefieres vivir? ")
    if(país == "España"):
        altura = input("Preferías ser alta?(más de 170cm) ")
        if(altura == "sí"):
            print("Eres Ana Peleteiro-Compaoré Brión la deportista española que compite en atletismo, especialista en la prueba de triple salto.​ Está casada con el atleta francés Benjamin Compaoré.​Participó en los Juegos Olímpicos de Tokio 2020, obteniendo una medalla de bronce en el triple salto.")
    elif(país == "Estados Unidos"):
        altura = input("Preferías ser alta?(más de 170cm) ")
        if(altura == "sí"):
            print("Eres Alice Coachman la atleta estadounidense de salto de altura, ganadora de la medalla de oro en los Juegos Olímpicos de Londres 1948, con lo que se convirtió en la primera mujer negra que obtuvo una medalla de oro en unas olimpiadas")
elif(deporte == "badminton"):
    país = input("En cual país prefieres vivir? ")
    if(país == "España"):
        altura = input("Preferías ser alta?(más de 170cm) ")
        if(altura == "sí"):
            print("Eres Carolina Marín la jugadora española de bádminton que compite en la categoría individual, en la que llegó a alcanzar el número uno del ranking mundial de la BWF.​ Es comúnmente reconocida como la mejor jugadora europea y una de las mejores de la historia.")
else:
    print("Prueba otro deporte")






