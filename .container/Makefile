all: up ps
.PHONY: all


clean:
	docker-compose down --volumes --remove-orphans
down:
	docker-compose down --remove-orphans
ps:
	docker ps
stop:
	docker-compose stop
stop-celery-beat:
	docker-compose stop my_stack_celery_beat
stop-celery-worker:
	docker-compose stop my_stack_celery_worker
stop-celery-browser:
	docker-compose stop my_stack_celery_browser
stop-rabbit:
	docker-compose stop my_stack_rabbit
up:
	docker-compose up -d
up-celery-beat:
	docker-compose up -d my_stack_celery_beat
up-celery-worker:
	docker-compose up -d my_stack_celery_worker
up-celery-browser:
	docker-compose up -d my_stack_celery_browser
up-rabbit:
	docker-compose up -d my_stack_rabbit
