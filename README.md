Para el desarrollo del proyecto se usó un IRobot Create 3 (también llamado Roomba) y una Raspberry pi 4, junto con un Lidar YDLidar T-mini pro
Una vez instalado Ubuntu 22.04, se procedió a instalar la distribución ROS 2 Humble
(ros-base). El proceso consistió en los siguientes pasos:
a. Configurar repositorios de ROS:
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o
/usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture)
signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu
$(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
b. Instalar ROS 2 Humble (versión base):
sudo apt update
sudo apt install ros-humble-ros-base
c. Configurar entorno ROS para cada terminal:
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
d. Instalar colcon (herramienta de compilación recomendada para ROS 2):
sudo apt install python3-colcon-common-extensions

Configuración de herramientas para gestión de redes
Con el objetivo de facilitar la gestión de redes Wi-Fi sin editar manualmente archivos del
sistema, se instalaron herramientas complementarias:
a. Wireless Tools (iwlist):
sudo apt install wireless-tools
b. Network Manager:
sudo apt install network-manager
