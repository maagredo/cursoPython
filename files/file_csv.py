import csv

csvsalida = open("analisis_archivo.csv", 'w', newline='')    
salida = csv.writer(csvsalida, delimiter='\t')
header=['Fecha','Mean-Min-Max','Concepto']
salida.writerow(header)


with open("archivos\FB_2.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
        
    cadena=""
    data=[]
    lowest_mean=0
    for row in reader:
        if lowest_mean==0:
            prom=(float(row['High'])+float(row['Low']))/2     
            lowest_mean=prom
            highest_mean=prom
            date_lowest_mean=row['Date']
            date_highest_mean=row['Date']
        else:
            prom=(float(row['High'])+float(row['Low']))/2     
        if prom < 239:
            cadena="MUY BAJO"
        elif prom >= 239 and prom < 265:
            cadena="BAJO"
        elif prom >= 265 and prom < 291:
            cadena="MEDIO"
        elif prom >= 291 and prom < 317:
            cadena="ALTO"
        else:
            cadena="MUY ALTO"

        data=[row['Date'],prom,cadena]
        salida.writerow(data)
        if lowest_mean>prom:            
            date_lowest_mean=row['Date']
            lowest_mean=prom
        if highest_mean<prom:
            highest_mean=prom
            date_highest_mean=row['Date']

csvfile.close()
print (date_lowest_mean,str(lowest_mean),date_highest_mean,str(highest_mean))





