while true;do
	clear
	echo "====MENU===="
	echo "1)Mostrar Info del Sistema"
	echo "2)Mostrar procesos que consumen mas memoria"
	echo "3)Mostrar espacio en el disco"
	echo "4)Salir"
	read -p "Seleccione una opcion: " option
	case $option in
		1)
			echo "Datos del Sistema:"
			uname -a 
			read -p "Enter para continuar";;
		2)
			echo "Procesos que mas consumen memoria:"
			ps aux --sort=-%mem | head -n 6 
			read -p "Enter para continuar";;
		3)
			echo "Espacio en el disco: "
			df -h
			read -p "Enter para Continuar";;
		4)
			echo "Saliendo..."
			exit ;;
	esac
done

#script de prueba
