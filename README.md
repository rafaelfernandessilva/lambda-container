# lambda-container

Executando container lambda. 

1. build na imagem

```
docker build -t container-lambda .

```

2. Iniciando o container 

```
 docker run -d -p 9000:8080 container-lambda

```

3. Chamando a funçao via post

```
 curl --request POST   --url http://localhost:9000/2015-03-31/functions/function/invocations   --header 'Content-Type: application/json'   --data '{"Input": 4}'; echo ""

 ```

 