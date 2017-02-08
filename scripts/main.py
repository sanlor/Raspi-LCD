# Programa : Teste display LCD 16x2 e Raspberry Pi B+
# (mostra Texto e endereco IP)
# Autor : Arduino e Cia

import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import socket
import os
import time
import datetime
import psutil

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


# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)

# Setup Botoes
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(17, GPIO.RISING)
GPIO.add_event_detect(27, GPIO.RISING)

# Variaveis
state = 0
btoesq = 0
btodir = 0

# Loop
while (True):
	
	try:	
		# Imprime texto na primeira linha
		print state
                if (state == 0):
                        # Hora
                        hora = time.strftime("%H:%M:%S")
                        lcd.message('IP %s' %(ipaddr) + '\nHora:   ' + hora)
			lcd.home()
			time.sleep(0.5)
                if (state == 1):
#			lcd.message('Teste 1\nTeste 1')
			cpu = psutil.cpu_percent()
			mem = psutil.virtual_memory().percent
			lcd.message('CPU: ' + str(cpu) + '\n' + 'Mem: ' + str(mem) + '')
			lcd.home()
			time.sleep(0.5)
		if (state == 2):
                        lcd.message('Teste 2\nTeste 2')
			time.sleep(0.5)
                if (state == 3):
                        lcd.message('Teste 3\nTeste 3')
			time.sleep(0.5)

		if (GPIO.event_detected(17)):
			print "Direita"
			state += 1
                        lcd.clear()
			time.sleep(0.1)
	        if (GPIO.event_detected(27)):
			print "Esquerda"
			state -= 1
                        lcd.clear()
                        time.sleep(0.1)
		# Mostra o endereco IP na segunda linha
		#lcd.message('\nIP %s' %(ipaddr))
		#lcd.clear()
		#time.sleep(0.1)
		
		if (state > 3):
                        state = 0
                if (state < 0):
                        state = 3
                        
	except (KeyboardInterrupt, SystemExit):
                lcd.clear()
                lcd.message('Script\nCancelado')
		raise

else:
	exit
