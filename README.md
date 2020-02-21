# My Stack


## How to setup initial configurations

### Setup database configuration
Make a copy of .env-sample 
```bash
cp .env-sample .env
```

Setup database configuration. Update values for:
```ini
DB_NAME=<db_name>
```

### Setup Celery configuration
In file **.env**, created before when *[setup database configuration](#setup-database-configuration)*; update values for:
```ini
# RABBITMQ
BROKER_USER=<broker_user>
BROKER_PASSWORD=<broker_user_password>
BROKER_HOST=<broker_server_ip_or_hostname|localhost>
BROKER_PORT=<broker_server_port|5672>

# CELERY
CELERY_TASK_DEFAULT_QUEUE=<default_tasks_queue_name|my_stack_dq>
CELERY_TASK_DEFAULT_EXCHANGE=<default_tasks_exchange_name|my_stack_ex>
CELERY_TASK_DEFAULT_ROUTING_KEY=<default_tasks_routing_key|my_stack_rk>
```


### Start the stack with Docker
From root directory execute:
```
docker-compose -f .container/docker-compose up -d
```


### Using RabbitMQ Manager tool
[Start the stack with Docker](#start-the-stack-with-docker)

Visit url http://localhost:15672/
```
username: rabbitmq_admin
password: RabbitMqAdminPassWord
```

#### Create user for Celery Worker and Celery Beat
Login in [RabbitMQ Manager Tool](#using-rabbitmq-manager-tool)

Click in **Admin** menu option

Click in **Add a user**
* Set as Username: *celery_user*
* Set as Passowrd: *celery_password*
* Set as Tags: *management*
* Click button **Add User**

#### Set permissions for created user
Login in [RabbitMQ Manager Tool](#using-rabbitmq-manager-tool)

Edit the created user: *celery_user*

In **Permissions** section, set as *Virtual Host* the value: / 

Click the button **Set permission**  


### Using Celery Browser
[Start the stack with Docker](#start-the-stack-with-docker)

Visit url http://localhost:8008/