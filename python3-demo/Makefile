.PHONY: help
help:
	@echo '                                                                          '
	@echo 'Makefile                                                  '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make help                           show help                          '
	@echo '                                                                          '
	@echo '   make up                             启动服务                            '
	@echo '   make down                           停止服务                            '
	@echo '   make logs                           查看日志                            '
	@echo '                                                                          '
	@echo '                                                                          '

.PHONY: run
run:
	. venv/activate
	python check_redis_key.py

.PHONY: build-docker
build-docker:
	docker build -t python3-demo .

.PHONY: chmod
chmod:
	chmod 777 data -f
	chmod 777 logs -f

.PHONY: run-docker-backend
run-docker-backend:
	docker run  -d  \
	-v $(PWD)/logs:/home/app/logs \
	-v $(PWD)/app:/home/app/app \
	python3-demo


.PHONY: run-docker-front
run-docker-front:
	docker run  \
	-v $(PWD)/logs:/home/app/logs \
	-v $(PWD)/app:/home/app/app \
	python3-demo