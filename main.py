from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

            
            self.drive = Chrome()

        
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

                self.drive.get('https://saj.pgfn.fazenda.gov.br/saj/login.jsf?dswid=982')
                
                time.sleep(2)
                
                campo_login = self.drive.find_element(By.ID, "frmLogin:username")
                
                campo_senha = self.drive.find_element(By.ID, "frmLogin:password")

                campo_login.send_keys("44355326896")
                
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
        
        def Meio(self):

                pass
        
        def Noite(self):

                pass
        

cl = empiezo()
cl.Login_Saj()



        
        