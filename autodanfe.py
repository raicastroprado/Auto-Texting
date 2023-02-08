import time
from selenium import webdriver
from selenium.webdriver.common.by import By



print('Iniciando processo de automação...')
# Inicializa o navegador
driver = webdriver.Chrome()
print('Abrindo navegador..')

# tempo de espera para abrir o navegador
time.sleep(2)

# Acessa a página web desejada
driver.get("https://inscricoes.fmu.br/redacao/1fef9985-a492-4253-86a3-cae2a5a65f62")

# clica no botao iniciar redação
clicar0 = driver.find_element(By.ID, "bt_gerar_redacao").click()

# Localiza o elemento da página web onde você deseja escrever o texto
text_field = driver.find_element(By.CSS_SELECTOR, "textarea.essay-textarea.form-control.form-control-lg")

time.sleep(5)
# Escreve o texto
text_field.send_keys("O trabalho infantil é uma questão que deve ser tratada com muita atenção e seriedade. Embora seja proibido por lei, ainda existem crianças e adolescentes que são explorados e obrigados a trabalhar em condições precárias, principalmente nas regiões Norte, Nordeste e Sudeste do país.")

time.sleep(2)

text_field.send_keys("Esta situação é inaceitável e vai contra os direitos da criança, como o direito à educação, à saúde e à proteção contra a exploração. Além disso, essas crianças são impedidas de desfrutar da infância, desenvolver seus talentos e sonhos, e isso pode ter impactos negativos na sua vida futura.")

time.sleep(2)

text_field.send_keys("Para solucionar este problema, é necessário uma intervenção eficaz por parte do governo, das organizações sociais e da sociedade em geral. É importante que haja uma intensificação dos esforços para combater o trabalho infantil, por meio de campanhas de conscientização, fiscalização rigorosa e punição para os empregadores que exploram crianças e adolescentes.")

time.sleep(2)

text_field.send_keys("Além disso, é fundamental investir em programas de educação e formação para as crianças e adolescentes, para que eles possam ter acesso ao conhecimento e às habilidades necessárias para se desenvolver e ter uma vida digna. Isso inclui a implementação de programas de inclusão escolar e projetos sociais que ofereçam apoio a essas crianças e adolescentes.")

time.sleep(2)

text_field.send_keys("Em conclusão, o trabalho infantil é uma questão que precisa ser enfrentada com muita determinação e seriedade. É preciso proteger os direitos da criança e garantir que eles possam desfrutar da infância, desenvolver seus talentos e ter um futuro promissor. Para isso, é necessário uma intervenção eficaz de todos os envolvidos, incluindo governo, organizações sociais e sociedade em geral.")

time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)

clicar1 = driver.find_element(By.ID, "bt_finaliza_redacao").click()

time.sleep(25)

print('Finalizando processo..')

# Feche o navegador
driver.quit()
