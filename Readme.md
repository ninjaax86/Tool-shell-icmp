
# Tool shell icmp

Esta es una herramienta que hice con el fin de seguir aprendiendo, y porque también me surgió una curiosidad de ver como podía usar este protocolo a mi gusto.

La herramienta es sencilla, actúa como un modelo p2p, donde, el **CLIENTE** se ejecuta y se queda **Escuchando** un paquete **ICMP** del **CAC** con su respectivas características como el ID.

Cuando el paquete **ICMP** cumple con esas caracteristicas, guarda el campo de datos de el encapsulado **ICMP** en texto plano, para agarrarlo y ejecutarlo.

Esto nos permite entre otras cosas poder ejecutar comandos sin que el firewall nos pueda llegar a bloquear ya que no analiza los datos de las cabeceras **ICMP**, a su vez, el protocolo no entabla conexiones, por lo tanto, no se puede analizar en herramientas como netstat o ss, esto nos muestra una ventaja grande en la postexplotacion frente al clasico reverse shell por tcp.


### Ejecución (solo sistemas linux)

#### Paquetes necesarios!
- Scapy
- Python 3
#### Uso (Maquina cliente)
 ```bash
icmp_client.py [-t TARGET] [-i IFACE]
 ```

#### Uso (Maquina cnc)
```bash
icmp_cnc.py [-t TARGET] [-i IFACE]
```
#### Parámetros
```bash
  -h, --help           Ayuda (Este menu)
  -t, --target TARGET  IP del objetivo
  -i, --iface IFACE    Interfaz a usar, default <interfaz_detectada>
```





### Video

[Video del PoC](https://youtu.be/1QsaWLAlI6Y?si=JG8Y7nbfu1uTbikj)

