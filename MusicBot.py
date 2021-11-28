#importing all speech_recognition and selenium modules
#importing os to kill the process running in background

import os
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#creating objects of Recognizer class
response1=sr.Recognizer()
response2=sr.Recognizer()

#using with to set mircphone as our input source
with sr.Microphone() as source:  
        print("Say Max to start.(Repeat 2 times)")
        #audio variable will store the input from microphone.
        response1.adjust_for_ambient_noise(source,duration=1)
        response1.energy_threshold = 300
        audio=response1.listen(source)
        try:
            #we are using while loop so the code will execute only when the
            #user says specific words to avoid random words or miscommunication.
            #and it will run until we get the right word that is Max.
            while(1):
                if ('Max' in response2.recognize_google(audio)):
                    audio=response1.listen(source)
                    break
                audio=response1.listen(source)
                print("Try again..")
        except Exception as e:
            print("Error",e)
            
# using if just to check if the input was right only then execute the following code            
if 'Max' in response2.recognize_google(audio):
        try:
            response2=sr.Recognizer()
            #using with to set mircphone as our input source.
            with sr.Microphone() as source:
                response2.adjust_for_ambient_noise(source,duration=1)
                print("What song you would like to listen to.") 
                #taking input of the song name.
                audio = response2.listen(source)
                #storing the song name in a variable so we can use it for youtube search.
                songName=response2.recognize_google(audio)
                print("Searching for",songName)
                #defined a url string for youtube search query.
                url="https://www.youtube.com/results?search_query="
                #we are using selenium to automate youtube to play a song.
                #creating chromeoptions object for chromedriver.
                #basically these are arguments that control the behaviour of chrome automation.
                options = webdriver.ChromeOptions()
                #headless makes the browser run in background without having to open it.
                options.add_argument('headless')
                #passing the options to chrome webdriver.
                driver = webdriver.Chrome('./chromedriver', chrome_options=options)
                #get method is used to reach a webpage.
                driver.get(url+songName)
                #this element path is used to click on the song that is displayed in search results.
                driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()
                print("Playing ",songName)

        except Exception as e:
            print("Error",e)
            
#while loop so user can request another song or close bot.
response3=sr.Recognizer()        
while(1):
    with sr.Microphone() as source:  
        response3.adjust_for_ambient_noise(source,duration=1)
        audio = response3.listen(source)
        if ('Play' in response3.recognize_google(audio)):
            cl=response3.listen(source)
            #storing the song name in a variable so we can use it for youtube search.
            songName=response3.recognize_google(cl)
            print("Searching for",songName)
            #defined a url string for youtube search query.
            url="https://www.youtube.com/results?search_query="
            #we are using selenium to automate youtube to play a song.
            #creating chromeoptions object for chromedriver.
            #basically these are arguments that control the behaviour of chrome automation.
            options = webdriver.ChromeOptions()
            #headless makes the browser run in background without having to open it.
            options.add_argument('headless')
            #passing the options to chrome webdriver.
            driver = webdriver.Chrome('./chromedriver', chrome_options=options)
            #get method is used to reach a webpage.
            driver.get(url+songName)
            #this element path is used to click on the song that is displayed in search results.
            driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()
            print("Playing ",songName)
            audio = response3.listen(source)     
        if ('Close' in response3.recognize_google(audio)):
            cl=response3.listen(source)
            print("Closing the bot.")
            #closing the chromedriver
            driver.quit()
            os.system("taskkill /chromedriver.exe")
            break
                        
  

