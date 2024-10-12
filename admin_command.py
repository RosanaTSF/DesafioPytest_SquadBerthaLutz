def admin_command(command, sudo=True):
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    
    if sudo:
        command = command[0]  # Acessando o primeiro item da lista
    
    if command == "start":
        return "Starting"
    elif command == "stop":
        return "Stopping"
    else:
        return "Unknown command"
