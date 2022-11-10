# Template Selenium
# Comandos úteis, diagnósticos de erros etc


#---------Chrome---------
#Importações comuns
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #Pra controle de versões do webdriver
from selenium.webdriver.chrome.options import Options #Para configurações de opções(pasta download etc)
from selenium.webdriver.common.by import By #Pacote comum para encontrar os elementos
from selenium.webdriver.support.wait import WebDriverWait #Para pegar os elementos quando estiverem disponíveis etc
from selenium.webdriver.support import expected_conditions as EC #Para definir algumas condições
#Para utilização de teclas
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Configurações iniciais de opções
option = Options() 
#Definindo opções como pasta pra download e desabilitando as notificações
prefs = {"download.default_directory" : pasta_destino, "profile.default_content_setting_values.notifications": 2}
option.add_experimental_option("prefs", prefs)

#Para iniciar o webdriver com controle da versão, sem definir onde ele está e com as opções anteriormente definidas
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)

#Para definir uma espera geral para todas as buscas(não funciona muito bem)
driver.implicitly_wait(10)

#Para entrar em um site        
driver.get("https://sgi.e-boticario.com.br/Paginas/Inicializacao/AguardarAcao.aspx")

#Para maximizar a janela
driver.maximize_window()

#Para saber o título/cabeçalho do site
print(driver.title)

#Para saber a fonte do site
print(driver.page_source)

#Para lidar com várias abas
janela_bot = driver.current_window_handle

#Busca básica 
#Pode ser por xpath ou outr
driver.find_element(By.XPATH, 'XPATH').click() #- clicando
#Para colocar texto no local: 
driver.find_element(By.XPATH, 'XPATH').send_keys("aa")

#Busca com espera
#Definindo a espera primeiro - navedadpr/tempo d espera/ vezes de espera
wait = WebDriverWait(driver, timeout=5, poll_frequency=2)
#Buscando
wait.until(EC.element_to_be_clickable((By.XPATH, 'XPATH'))).click() 

#Lidando com mais de uma janela
#Mudo o controle para uma nova aba, fecho a nova aba e volto o controle para a primeira aba(principal)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#Utilizando teclas
#Pressiono a tecla seta pra baixo com key_down e key_up
ActionChains(driver).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
#Pressiono enter
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


#---------Firefox---------
#Importações comuns
from webdriver_manager.firefox import GeckoDriverManager #Pra controle de versões do webdriver
from selenium.webdriver.firefox.options import Options #Para configurações de opções(pasta download etc)

#Configurações iniciais de opções
option = Options() 
#Definindo opções como pasta pra download e desabilitando as notificações
option.set_preference("browser.download.dir", pasta_destino)
option.set_preference("browser.download.folderList", 2)

#Para iniciar o webdriver com controle da versão, sem definir onde ele está e com as opções anteriormente definidas
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = option)

#Para limpar dados de um campo no Gecko, precisamos primeiro clicar no campo para limpar
#Caso o campo seja data ou difícil de limpar, podemos usar o selecionar e deletar:
limpar = wait.until(EC.element_to_be_clickable((By.XPATH, 'XPATH')))
limpar.click() #Clique comum no campo
limpar.send_keys(Keys.CONTROL + "a") #Combinação de comandos para selecionar
limpar.send_keys(Keys.DELETE) #Tecla delete