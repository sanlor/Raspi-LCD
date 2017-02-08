# Programa : Teste display LCD 16x2 e Raspberry Pi B+
# (mostra Texto e endereco IP)
# Autor : Arduino e Cia

import Adafruit_CharLCD as LCD
import socket
import os
import time
import datetime

# Le as informacoes do endereco IP
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]

# Hora
hora = time.strftime("%H:%M:%S")

# Pinos LCD x Raspberry (GPIO)
lcd_rs        = 8
lcd_en        = 7
lcd_d4        = 22
lcd_d5        = 23
lcd_d6        = 24
lcd_d7        = 25
lcd_backlight = 4

# Define numero de colunas e linhas do LCD
lcd_colunas = 16
lcd_linhas  = 2

# Configuracao para display 20x4
# lcd_colunas = 20
# lcd_linhas  = 4

# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)


# Imprime texto na primeira linha
lcd.message('Boot:   ' + hora)
#lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))

# Mostra o endereco IP na segunda linha
lcd.message('\nIP %s' %(ipaddr))
