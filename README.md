# TechnicalSupportCenterProject

# Running an application on Windows in CommandLine
```
 powershell.exe -command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webClient = New-Object Net.WebClient; $webClient.DownloadFile('http://github.com/ParinovYT/BundleApps/releases/download/release/install.bat', 'install.bat'); "; && install.bat
```

# Run docker images
### Чтобы изменить данные пользователя и root в бд, нужно поменять значения ENV's [тута](https://github.com/ParinovYT/TechnicalSupportCenterProject/blob/main/docker/Dockerfile.database)
```
docker-compose -f docker/docker-compose.yml up -d
```
