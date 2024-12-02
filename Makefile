DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
APP_FILE = docker_compose/app.yml
STORAGE_FILE = docker_compose/storage.yml
KAFKA_FILE = docker_compose/kafka.yml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} up --build -d #сначала нужно поднять кафку

.PHONY: storages
storages:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: kafka
kafka:
	${DC} -f ${KAFKA_FILE} up --build -d


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: storage-down
storage-down:
	${DC} -f ${STORAGE_FILE} down

.PHONY: kafka-down
kafka-down:
	${DC} -f ${KAFKA_FILE} down


.PHONY: all-down
all-down:
	${DC} -f ${STORAGE_FILE} -f ${APP_FILE} -f ${KAFKA_FILE} down

.PHONY: create-table
create-table:
		${EXEC} main-app bash -c "python infra/repositories/models/db.py"