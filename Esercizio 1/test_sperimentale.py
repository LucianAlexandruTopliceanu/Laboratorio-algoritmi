import Dizionario_ListaConcatenata
import Dizionario_ABR
import Dizionario_HashHeap
import random
import timeit as timeit
import matplotlib.pyplot as plt 
import numpy as numpy

def genera_num_ordinati(numero):
    x=[]
    for i in range(numero):
        x.append(i+1)
    return x

def genera_num_casuali(numero):
    x=[]
    numeri=genera_num_ordinati(numero)
    while len(numeri) != 0:
        index=random.randint(0, len(numeri)-1)
        x.append(numeri[index])
        del numeri[index]
    return x

def riempi_dizionario(dizionario,chiavi,valori):
        for i in range(len(chiavi)):
            dizionario.insert(chiavi[i],valori[i])

def run_all_tests(numero_elementi,hash_table_size):
    #generazione di chiavi e valori casuali, le copie saranno definite dal indice ({chiavi[i],valori[i]} forma un elemnto)
    print("TEST SU DIZIONARI IMPLEMENTATI CON LISTE CONCATENATE, ABR E HASHHEAP")
    print("TEST N° 1 CON CHIAVI E VALORI CASUALI")
    chiavi=genera_num_casuali(numero_elementi+1)
    valori=genera_num_casuali(numero_elementi+1)
    run_test(chiavi,valori,hash_table_size,"1",numero_elementi)
    print("TEST N° 2 CON CHIAVI ORDINATE E VALORI CASUALI")
    chiavi=genera_num_ordinati(numero_elementi+1)
    valori=genera_num_casuali(numero_elementi+1)
    run_test(chiavi,valori,hash_table_size,"2",numero_elementi)
    print("TEST N° 3 CON CHIAVI CASUALI VALORI ORDINATI")
    chiavi=genera_num_casuali(numero_elementi+1)
    valori=genera_num_ordinati(numero_elementi+1)
    run_test(chiavi,valori,hash_table_size,"3",numero_elementi)
     
def run_test(chiavi,valori,hash_table_size,numero_test,numero_elementi):
    numero_iterazioni=1
    #Esecuzione test sul insermineto
    print("INIZIO TEST INSERIMENTO")
    t_lista,t_abr,t_hash_heap=[],[],[]
    run_insert_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size)
    print("Tempo medio:")
    print("Lista concatenata: "+str(format(numpy.mean(t_lista),'.8f')))
    print("ABR: "+str(format(numpy.mean(t_abr),'.8f')))
    print("HashHeap: "+str(format(numpy.mean(t_hash_heap),'.8f')))
    print("----------------------------------------------------------------")
    stampa_imagine("Inserimento","Elementi","Tempo",t_lista,"Lista concatenata","red",numero_test,numero_elementi)
    stampa_imagine("Inserimento","Elementi","Tempo",t_abr,"ABR","blue",numero_test,numero_elementi)
    stampa_imagine("Inserimento","Elementi","Tempo",t_hash_heap,"HashHeap","green",numero_test,numero_elementi)
    #Esecuzione test sulla ricerca
    print("INIZIO TEST RICERCA")
    t_lista,t_abr,t_hash_heap=[],[],[]
    run_search_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size)
    print("Tempo medio:")
    print("Lista concatenata: "+str(format(numpy.mean(t_lista),'.8f')))
    print("ABR: "+str(format(numpy.mean(t_abr),'.8f')))
    print("HashHeap: "+str(format(numpy.mean(t_hash_heap),'.8f')))
    print("----------------------------------------------------------------")
    stampa_imagine("Ricerca","Elementi","Tempo",t_lista,"Lista concatenata","red",numero_test,numero_elementi)
    stampa_imagine("Ricerca","Elementi","Tempo",t_abr,"ABR","blue",numero_test,numero_elementi)
    stampa_imagine("Ricerca","Elementi","Tempo",t_hash_heap,"HashHeap","green",numero_test,numero_elementi)
    #Esecuzione test sulla rimozione
    print("INIZIO TEST RIMOZIONE")
    t_lista,t_abr,t_hash_heap=[],[],[]
    run_delete_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size)
    print("Tempo medio:")
    print("Lista concatenata: "+str(format(numpy.mean(t_lista),'.8f')))
    print("ABR: "+str(format(numpy.mean(t_abr),'.8f')))
    print("HashHeap: "+str(format(numpy.mean(t_hash_heap),'.8f')))
    print("----------------------------------------------------------------")
    stampa_imagine("Rimozione","Elementi","Tempo",t_lista,"Lista concatenata","red",numero_test,numero_elementi)
    stampa_imagine("Rimozione","Elementi","Tempo",t_abr,"ABR","blue",numero_test,numero_elementi)
    stampa_imagine("Rimozione","Elementi","Tempo",t_hash_heap,"HashHeap","green",numero_test,numero_elementi)

def run_insert_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size):
    for i in range(len(chiavi)-1):
        #test sulla lista concatenata
        dizionario=Dizionario_ListaConcatenata.Dizionario_ListaConcatenata()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.insert(chiavi[i+1],valori[i+1]),number=numero_iterazioni)
        t_lista.append(tempo_totale/numero_iterazioni)
        #test sul ABR
        dizionario=Dizionario_ABR.Dizionario_ABR()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.insert(chiavi[i+1],valori[i+1]),number=numero_iterazioni)
        t_abr.append(tempo_totale/numero_iterazioni)
        #test sul HashHeap
        dizionario=Dizionario_HashHeap.Dizionario_HashHeap(hash_table_size)
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.insert(chiavi[i+1],valori[i+1]),number=numero_iterazioni)
        t_hash_heap.append(tempo_totale/numero_iterazioni)

def run_search_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size):
    for i in range(len(chiavi)-1):
        #test sulla lista concatenata
        dizionario=Dizionario_ListaConcatenata.Dizionario_ListaConcatenata()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.search(chiavi[i//2]),number=numero_iterazioni)
        t_lista.append(tempo_totale/numero_iterazioni)
        #test sul ABR
        dizionario=Dizionario_ABR.Dizionario_ABR()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.search(chiavi[i//2]),number=numero_iterazioni)
        t_abr.append(tempo_totale/numero_iterazioni)
        #test sul HashHeap
        dizionario=Dizionario_HashHeap.Dizionario_HashHeap(hash_table_size)
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.search(chiavi[i//2]),number=numero_iterazioni)
        t_hash_heap.append(tempo_totale/numero_iterazioni)

def run_delete_test(chiavi,valori,t_lista,t_abr,t_hash_heap,numero_iterazioni,hash_table_size):
    for i in range(len(chiavi)-1):
        #test sulla lista concatenata
        dizionario=Dizionario_ListaConcatenata.Dizionario_ListaConcatenata()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.delete(chiavi[i//2]),number=numero_iterazioni)
        t_lista.append(tempo_totale/numero_iterazioni)
        #test sul ABR
        dizionario=Dizionario_ABR.Dizionario_ABR()
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.delete(chiavi[i//2]),number=numero_iterazioni)
        t_abr.append(tempo_totale/numero_iterazioni)
        #test sul HashHeap
        dizionario=Dizionario_HashHeap.Dizionario_HashHeap(hash_table_size)
        riempi_dizionario(dizionario,chiavi[0:i],valori[0:i])
        tempo_totale=timeit.timeit(lambda:dizionario.delete(chiavi[i//2]),number=numero_iterazioni)
        t_hash_heap.append(tempo_totale/numero_iterazioni)

def stampa_imagine(title, x_lab, y_lab,tempi,nome_struttura,colore,numero_test,numero_elementi):
    x=range(0,numero_elementi)
    figura = plt.figure()
    plt.title(numero_test+" "+title+" "+nome_struttura)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.plot(x,tempi, color=colore, label=nome_struttura)
    plt.legend()
    #plt.show()
    figura.savefig(numero_test+" "+title+" "+nome_struttura+".png",dpi=300)
    plt.close()

if __name__ == "__main__":
    numero_elementi=1000
    hash_table_size=51
    run_all_tests(numero_elementi,hash_table_size)
    print("OK")