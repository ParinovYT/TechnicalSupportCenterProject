#MYSQL
MYSQL-CONTAINER = docker-mysql-1
MYSQL-ROOT-PASSWORD = rootsroot12345:D
MYSQL-WORK-DATABASE = technical_support
MYSQL-PATH-TO-SCHEMA = database/schema.sql

docker-deploy:
	docker-compose -f docker/docker-compose.yml up -d

docker-database-create-shema:
	docker exec -i $(MYSQL-CONTAINER) mysqldump -u root --password="$(MYSQL-ROOT-PASSWORD)" $(MYSQL-WORK-DATABASE) > $(MYSQL-PATH-TO-SCHEMA)
	@echo !!!FILE "$(MYSQL-PATH-TO-SCHEMA)" IS SAVED IN UTF-16 ENCODING, AFTER CREATING A NEW DATABASE SCHEMA, YOU NEED TO CHANGE THE FILE ENCODING TO UTF-8 AND DEL