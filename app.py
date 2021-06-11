# Uso
# $ app.py WARN entrada.log salida.log
# $ app.py INFO entrada.log salida.log
# $ app.py ERROR entrada.log salida.log

#libs
import argparse

parser = argparse.ArgumentParser(description="---- App logs ---")
#flags
parser.add_argument('log',     type=str, help='tipo de log')
parser.add_argument('entrada', type=str, help='archivo entrada')
parser.add_argument('salida',  type=str, help='archivo salida')
args= parser.parse_args()

def buscarLogs (logs, archivoE, archivoS):
    listaLogs = []
    with open(archivoE, 'r') as f:
        for linea in f:
            linea = f.readline()
            if logs in linea :  # Esta WARN INFO ERROR
                listaLogs.append(linea)

    # Guardar lineas
    with open( archivoS, 'w') as f:
        for linea in listaLogs:
            f.write(linea)



if __name__ == '__main__':
    if args.log and args.entrada and args.salida :
        tipoLog     = args.log.upper()  # mayuscula
        if (tipoLog == 'INFO') or (tipoLog == 'ERROR') or (tipoLog == 'WARN'):
            archivoEntrada = args.entrada
            archivoSalida  = args.salida
            buscarLogs(tipoLog, archivoEntrada, archivoSalida)
        else:
            print('No valido')
