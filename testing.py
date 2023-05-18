from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from multiprocessing import Process

def open_edge(url):
    edge_options = EdgeOptions()
    # Add any desired options here, e.g., headless mode
    # edge_options.add_argument("--headless")
    driver = webdriver.Edge(options=edge_options)
    driver.get(url)
    # Perform actions in Microsoft Edge browser
    driver.quit()

def open_firefox(url):
    firefox_options = FirefoxOptions()
    # Add any desired options here, e.g., headless mode
    # firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    # Perform actions in Firefox browser
    driver.quit()

if __name__ == '__main__':
    urls = ["https://web.whatsapp.com", "https://www.google.com","https://web.whatsapp.com", "https://www.google.com"]
    processes = []

    for url in urls:
        edge_process = Process(target=open_edge, args=(url,))
        firefox_process = Process(target=open_firefox, args=(url,))
        processes.append(edge_process)
        processes.append(firefox_process)
        edge_process.start()
        firefox_process.start()

    for process in processes:
        process.join()
