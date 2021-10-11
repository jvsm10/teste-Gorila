from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CDB
from .serializer import CDBSerializer
import csv
from datetime import date, datetime
from collections import deque
from decimal import *

#View da requisição
class CDBList(APIView):
    #Requisição POST que realizará os cálculos e retornará a evolução do investimento CDB
    def post(self, request):
        serializer = CDBSerializer(data=request.data)
        if serializer.is_valid():
            resultado = self.calculo(serializer.data)
            return Response(resultado, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #Função para leitura do arquivo csv
    def lerCsv(self,dado):
        with open('CDI_Prices.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=["sSecurityName","Data", "Taxa"])
            csv_reader.__next__()
            arqcsv = deque()
            for row in csv_reader:
                arqcsv.appendleft(row)
        return arqcsv

    #Função para para criar a lista com a evolução do investimento, realizando o acumulo do TCDI
    def calculo(self,dado):
        arqCSV = self.lerCsv(dado)
        resul = []
        tcdik = 1
        dataInvest = datetime.strptime(dado.get("investmentDate"), '%Y-%m-%d').date()
        dataAtu = datetime.strptime(dado.get("currentDate"), '%Y-%m-%d').date()
        for row in arqCSV:
            dataArq = datetime.strptime(row["Data"], '%d/%m/%Y').date()
            if dataAtu<=dataArq:
                break
            if dataInvest <= dataArq:
                tcdik = self.calculaTCDI(dado.get("cdbRate"),row["Taxa"],tcdik)
                #calcula o preço unitário do CDB para o dia em questão
                price = 1000*round(tcdik,8)
                teste = {'date': dataArq, 'unitPrice': price}
                resul.append(teste)
        return resul[::-1]

    #Função para o calculo do TCDI acumulado
    def calculaTCDI(self,tcdb,cdik,tcdi):
        tcdik = round(self.calculaTCDIK(cdik),8)
        tcdi = round(tcdi,16)*(1+tcdik*(Decimal(tcdb)/100))
        return round(tcdi,16)

    #Função para o calculo do TCDI ao dia
    def calculaTCDIK(self, cdik):
        TCDIk = ((round(Decimal(cdik),2)/Decimal(100))+1)**(Decimal(1)/Decimal(252))-1
        return TCDIk