#importing all speech_recognition and selenium modules
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#creating objects of Recognizer class
response1=sr.Recognizer()
response2=sr.Recognizer()
#using with to set mircphone as our input source
with sr.Microphone() as source:  
        response1.adjust_for_ambient_noise(source,duration=1)
        print("Say Max to start.(Repeat 2 times)")
        #audio variable will store the input from microphone.
        audio=response1.listen(source)
        try:
            #we are using while loop so the code will execute only when the
            #user says specific words to avoid random words or miscommunication.
            #and it will run until we get the right word that is audio.
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

