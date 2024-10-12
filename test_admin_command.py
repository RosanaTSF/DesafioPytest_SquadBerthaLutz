from admin_command import admin_command  # Importando a função a ser testada

def test_admin_command_start():
    assert admin_command(["start"]) == "Starting"  # Testa o comando "start"

def test_admin_command_stop():
    assert admin_command(["stop"]) == "Stopping"  # Testa o comando "stop"

def test_admin_command_unknown():
    assert admin_command(["pause"]) == "Unknown command"  # Testa um comando desconhecido
