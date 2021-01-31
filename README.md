# 2or3-pay

## Build
1. Copy .env from .env.template

    ```
    cp .env.template .env
    ```

1. Edit your .env file. Please see Env section for detail.

1. Build docker image by docker-compose

```
$ docker-compose build
```

## Run
- Run a web & db server.

```
$ docker-compose run
```

## Env
- .env

| name | description |
| - | - |
| DB_PASS | password for database login |

