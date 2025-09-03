Para el desarrollo del proyecto se usó un IRobot Create 3 (también llamado Roomba) y una Raspberry pi 4, junto con un Lidar YDLidar T-mini pro
Una vez instalado Ubuntu 22.04, se procedió a instalar la distribución ROS 2 Humble
(ros-base). El proceso consistió en los siguientes pasos:

a. Configurar repositorios de ROS:

sudo apt update && sudo apt install curl gnupg lsb-release

sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu

$(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

b. Instalar ROS 2 Humble (versión base):

sudo apt update

sudo apt install ros-humble-ros-base

c. Configurar entorno ROS para cada terminal:

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

source ~/.bashrc

d. Instalar colcon (herramienta de compilación recomendada para ROS 2):

sudo apt install python3-colcon-common-extensions

*Configuración de herramientas para gestión de redes*
Con el objetivo de facilitar la gestión de redes Wi-Fi sin editar manualmente archivos del sistema, se instalaron herramientas complementarias:

a. Wireless Tools (iwlist):
sudo apt install wireless-tools


b. Network Manager:
sudo apt install network-manager


*Inicio y actualización del robot*
Para comenzar con la configuración del iRobot Create 3, se utilizó como referencia la documentación oficial proporcionada por iRobot Education:
https://iroboteducation.github.io/create3_docs/setup/ubuntu2204/


*El procedimiento inicial de encendido y actualización se realizó de la siguiente forma:*


● El robot se enciende automáticamente al colocarlo sobre su base de carga.


● Para ingresar al modo de configuración, se debe mantener presionados simultáneamente los dos botones físicos del robot (ubicados a cada lado del botón del power) hasta que el anillo LED cambie a color azul. Esto indica que el robot ha entrado en modo hotspot.


● En este estado, el robot genera una red Wi-Fi con el nombre Create-03A9, a la cual se puede conectar un computador o la Raspberry Pi para realizar la configuración.


● Desde un navegador web se accede a la dirección IP del robot en este modo:
http://192.168.10.1/


● En la pestaña “About” del portal web se puede verificar la información del robot, incluyendo su número de serie:
S/N: e17628 - este es el número de serie del Roomba que se tiene en RAMEL


● En el mismo portal se puede actualizar el firmware del robot. Este proceso puede tardar varios minutos y es esencial completarlo antes de continuar. Al finalizar correctamente,
el anillo LED del robot cambia a blanco brillante.


● En la pestaña de red del mismo portal, se configura la conexión Wi-Fi deseada, ingresando el SSID (nombre) y la contraseña de la red doméstica. Aquí es importante puntualizar que la red debe ser la misma a la que se va a conectar la raspberry para poder leer y compartir los tópicos del robot y manejarlos según convenga.


*Configuración red wifi del Roomba*

Información del Roomba - aquí se ve el número de serie y su RMW para comunicación

Instalación en la Raspberry Pi del entorno del Roomba para conexión

Una vez instalado ROS 2 Humble en la Raspberry Pi 4, se procedió a instalar los paquetes necesarios para la comunicación con el robot:

sudo apt install -y ros-humble-irobot-create-msgs

sudo apt install -y build-essential python3-colcon-common-extensions python3-rosdep ros-humble-rmw-cyclonedds-cpp

El robot Create 3 utiliza el middleware Fast DDS (Fast RTPS) por defecto. Por ello, es necesario especificarlo en la configuración del entorno ROS 2:

echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ~/.bashrc

source ~/.bashrc

*Acceso remoto a la Raspberry Pi (SSH desde Windows o Ubuntu)*

Desde un computador con Windows, se puede acceder remotamente a la Raspberry Pi

mediante SSH:

ssh pi@<IP_de_la_Pi>

Se debe aceptar la clave SSH (escribir yes sí es la primera conexión) y luego ingresar la contraseña del usuario:

*Verificación de estado del robot*

Para comprobar el estado general del robot, se utilizaron los siguientes comandos:

ros2 topic echo /p1/battery_state

ros2 topic echo /p1/dock_status

ros2 topic echo /p1/hazard_detection

ros2 topic echo /p1/kidnap_status

ros2 topic echo /p1/mobility_monitor/transition_event

ros2 topic echo /p1/robot_state/transition_event

ros2 topic echo /p1/stop_status

ros2 topic echo /p1/wheel_status

ros2 topic echo /p1/slip_status

ros2 topic echo /p1/odom

*INSTALACIÓN DE LIDAR EN LA RASPBERRY*

Instalación del paquete para ROS 2 en la Raspberry

Lo primero es acceder al github de YDLidar (link arriba) para obtener el paquete de ROS 2.

Se debe clonar el Branch de Humble ya que estamos usando Ubuntu 22.04:

git clone -b humble https://github.com/YDLIDAR/ydlidar_ros2_driver.git

ydlidar_ros2_ws/src/ydlidar_ros2_driver

Lo siguiente es hacer la construcción y compilación de la paquetería. En este caso el paquete se llamará ydlidar_ros2-ws:

cd ydlidar_ros2_ws

colcon build --symlink-install

Siempre se debe recordar hacer la inicialización del paquete:

source ./install/setup.bash

SI se quiere que el paquete arranque junto con el encendido del sistema, se puede agregar al bash de inicio con los siguientes comandos:

echo "source ~/ydlidar_ros2_ws/install/setup.bash" >> ~/.bashrc

source ~/.bashrc

Si llegase a ser necesario, se otorgan los siguientes comandos para darle los permisos necesarios al puerto para que pueda hacer la lectura correcta de los datos del módulo adaptador UART:

chmod 0777 src/ydlidar_ros2_driver/startup/*

sudo sh src/ydlidar_ros2_driver/startup/initenv.sh
