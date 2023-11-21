# configuration settings
config = {
    "database": {"host": "localhost", "port": 3306, "username": "admin", "password": "password"},
    "server": {"host": "127.0.0.1", "port": 8080, "timeout": 120},
    "logging": {"level": "INFO", "file": "app.log"}
}

# accessing server configuration
server_config = config.get("server")
if server_config:
    print("Server Host:", server_config["host"])
    print("Server Port:", server_config["port"])
    print("Timeout:", server_config["timeout"])
else:
    print("Server configuration not found")

# output --> 
    # Server Host: 127.0.0.1
    # Server Port: 8080
    # Timeout: 120