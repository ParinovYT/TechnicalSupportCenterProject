# TechnicalSupportCenterProject

## Running an application on Windows in CommandLine
```
 powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webClient = New-Object Net.WebClient; $webClient.DownloadFile('http://github.com/ParinovYT/BundleApps/releases/download/release/install.bat', 'install.bat'); "; && install.bat
```

# Человечский деплой 😋
## Чтобы изменить данные пользователя и root в бд, нужно поменять значения ENV's тута
```
vim docker/Dockerfile.database
```
```
make docker-deploy
```

## Запуск програмули 😎
```
make init
```
### `release`
```
make app-run-release
```
### `debug`
```
make app-run-debug
```
## Для того чтобы работать с базкой данных нужен пароль, который находиться в файле docker/Dockerfile.database `MYSQL_ROOT_PASSWORD`, нужно зайти в php my admin, сюда 👉 [http://localhost:8090/](http://localhost:8090/) 👈
## Поработал с базкой данных и внес туда изменения, тогда не забудь сохранить ее схему 😉
## Нужно указать пароль от root пользователя, тута
```
vim Makefile
```
```
MYSQL-ROOT-PASSWORD = rootpassword
```
## И потом выполнить команду
```
make docker-database-create-shema
```
