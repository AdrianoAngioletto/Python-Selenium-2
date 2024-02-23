from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path
import glob
import pandas as p
import os
import shutil
import time



class empiezo:

        def __init__(self) -> None:
            
            bemvindo_bb = '''
                +===========================================================================+
                |             BEM VINDO,  Ao Robô, PSE FISCAL FGTS                          |
                |                                                                           |
                |                                                                           |
                |          Procuradoria Geral da Fazenda 3° Regiao                          |
                |                                                                           |
                |                                                                           |    
                |                                                                           |
                | Dev:  AdrianoAngioletto                                                   |
                +===========================================================================+
                '''
            print(bemvindo_bb)

            
        
        
        def le_diretorio_e_planilha(self):
            
            caminho_absoluto_saj_ = Path.cwd()
            Processos_ = 'processos.xlsx'
            Caminho_Mais_Pasta_saj_ = caminho_absoluto_saj_ / Processos_

            self.ListaProcessos_ = Caminho_Mais_Pasta_saj_
            
            # self.processos = p.read_excel(self.ListaProcessos_)
       
        
            # for resultado in self.processos['PROCESSO TXT']:
                
            #   ...
                
                                       
        
        def verifica_se_Existe(self):
               
            diretorio_atual = os.getcwd()

            lista = os.listdir(diretorio_atual)

            encontrou_xlsx = any(arquivo.endswith('.xlsx') for arquivo in lista)

            if encontrou_xlsx:

                verifica_planilhas = os.listdir()

                lista = []

    # Filtra os arquivos ocultos e mantém apenas os arquivos .xlsx
                for arquivo in verifica_planilhas:

                    if os.path.isfile(arquivo) and arquivo.endswith('.xlsx'):
                        
                        lista.append(arquivo)

                for self.planilha in lista:
                    novo_nome = 'processos.xlsx' # Adiciona o nome original antes do 'processo'
                    
                    print(f'Movendo {self.planilha} para {novo_nome}')
                    
                    shutil.move(self.planilha, novo_nome)

                    print('Padronizando, nome da Planilha ...')

                else:
                    print('Planilha processos encontrada, Carregando..')

            else:
                print('Você precisa adicionar a planilha, para Consultar, sem ela não é possivel')

                time.sleep(7)

                quit()
        
                    
        
        def Login_Saj(self):
            
                self.drive = Chrome()
    

                self.drive.get('https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=982')
                
                time.sleep(2)
                
                campo_login = self.drive.find_element(By.ID, "frmLogin:username")
                
                campo_senha = self.drive.find_element(By.ID, "frmLogin:password")

                campo_login.send_keys("*****")
                
                campo_senha.send_keys("Pgfn@1234")

                botao_ok = self.drive.find_element(By.ID, "frmLogin:entrar")
                time.sleep(2)
                botao_ok.click()
                time.sleep(3)

                botao_processo = self.drive.find_element(By.CLASS_NAME, "ui-menuitem-text")  # PEGA  ID DA LISTA > PROCESS
                
                ActionChains(self.drive).move_to_element(botao_processo).perform() # MOVE MOUSE ATÉ A LISTA
                time.sleep(1) # TEMPO NECESSÁRIO

                botao_consulta = self.drive.find_element(By.XPATH, '//*[@id="j_idt15:formMenus:menuProcessosPendentes"]/span').click() # PEGA O ITEM DA LISTA >>> Processo
                time.sleep(7)
        
        def Parte_Consulta_Processo(self):
            
                botao_executa_tarefa = self.drive.find_element(By. XPATH, '//*[@id="j_idt551:mbExecutarTarefa_button"]/span[2]').click()
                
                time.sleep(1)
                
                botao_distribuir_procurador = self.drive.find_elements(By. XPATH, '//*[@id="j_idt551:menuDistribuirProcuradores"]/span')[0].click()
                
                time.sleep(5)
                
                self.le_diretorio_e_planilha()
                
                for processos in p.read_excel(self.ListaProcessos_):
                    
                    print(processos)
            
           
                

              
        
        def Noite(self):

                pass
        

cl = empiezo()
# cl.verifica_se_Existe()
# cl.Login_Saj()
# cl.Parte_Consulta_Processo()
cl.le_diretorio_e_planilha()


        
        
