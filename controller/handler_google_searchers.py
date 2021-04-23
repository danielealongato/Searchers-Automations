from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from view.google_views import GoogleHandler
from components.utils import Utils
from tqdm import tqdm


class HandlerSearchers:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.utils = Utils(self.browser)
        self.searcher_google = GoogleHandler(self.browser)
        self.list_search = ["Automação de processos", "Python", "Agilizando tarefas repetitivas"]

    def flow_search(self):

        print('Abrindo o Browser...')
        self.searcher_google.open_google()
        self.utils.maximize_window()
        for item in tqdm(self.list_search):
            print('Iniciando as pesquisas...')
            self.searcher_google.new_search(text=item)
            self.utils.scrolling_page()

            print('Coletando retorno da busca...')
            links = self.searcher_google.get_links_list_by_searched()

            print('Validando links para aprofundamento das buscas...')
            list_links = self.searcher_google.validate_list_links(link_list=links)

            print('Aplicando para as buscas encontradas...')
            for link in tqdm(list_links):
                self.utils.open_new_tab(link_page=link)
                self.utils.open_link(link=link)
                print('Tirando um printscreen... ;p')
                self.utils.take_picture(name_photo=item)
                self.utils.scrolling_page()
                # print('Coletando os dados da tela...')
                # self.utils.get_text_page(link_page=link)
                print('Fechando a aba...')
                self.utils.close_tab()

        print('Fechando o browser...')
        self.utils.close_window()

        print('Fim.')
