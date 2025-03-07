#### Inicializamos el container de los contenedores


# ir a api y dar permisos
cd ./api
chmod +x wait-for-it.sh
cd ../

# ir a Sensores y dar permisos
cd ./Sensores
chmod +x wait-for-it.sh
cd ../

# ir a Consumers y dar permisos
cd ./Consumers
chmod +x wait-for-it.sh
cd ../


docker network create sensores
docker network create consumer



# Define your compose files or directories
COMPOSE_FILES=(
    "./Consumers/docker-compose.yml"
    "./docker-compose.yml"
    "./Sensores/docker-compose.yml"
)

echo "Starting all Docker Compose services..."

# Loop through each compose file and start the services
for COMPOSE_FILE in "${COMPOSE_FILES[@]}"; do
    echo "Starting services in $COMPOSE_FILE..."
    docker-compose -f "$COMPOSE_FILE" up -d
done


cd ./Sensores
docker-compose up -d --scale temperature-humidity-sensors=4
docker-compose up -d --scale occupancy-sensors=6
docker-compose up -d --scale power-consumption-meters=7
docker-compose up -d --scale security-cameras=3

echo "All services are up and running!"
