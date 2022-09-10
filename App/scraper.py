from selenium import webdriver


def getTasks():
    allTasks = []
    driver = webdriver.Chrome('C:/Users/michj/Desktop/chromedriver.exe')
    driver.get('https://priceless-kalam-0bc3f2.netlify.app/')
    driver.implicitly_wait(3)
    taskList = driver.find_elements_by_id('taskname')
    for i in taskList:
        allTasks.append(taskList[taskList.index(i)].text)
        print(allTasks)
    return allTasks
