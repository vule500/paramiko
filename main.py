import paramiko
from netmiko import ConnectHandler

def gather_device_info(device_ip, username, password):
    # Parametri za SSH konekciju
    ssh_params = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'password': password,
    }

    try:
        # Konekcija preko SSH-a
        ssh_session = ConnectHandler(**ssh_params)

        # Izvršavanje komande "show interfaces"
        output = ssh_session.send_command('show interfaces')
        print(output)

        # Zatvaranje SSH sesije
        ssh_session.disconnect()

    except Exception as e:
        print(f"Greška pri povezivanju ili izvršavanju komande na uređaju {device_ip}: {str(e)}")

def main():
    # Spisak uređaja za dokumentaciju
    devices = [
        {"ip": "192.168.1.1", "username": "admin", "password": "password1"},
    ]

    for device in devices:
        gather_device_info(device["ip"], device["username"], device["password"])

if __name__ == "__main__":
    main()
