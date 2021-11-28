# Voice-recognized-music-bot
A voice recognized python program that will search the song on YouTube and will play it for you.

Reason to make this bot:

This program will help any kind of people to play song without having to give input manually.
All you need is to say some words.
Its a better solution for old age people as its easy to use and dont need much input in order to listen to their favourite songs.
Because of voice recognition theres no complex UI for those who are not familiar with applications and computers in general.
The idea behind making this is to help old age people to listen to favourite songs to keep them mentally happy and active.
As these people have alot less things to do leading to boredom and unhealthy boring life.
Music will keep them happy and cheerful all the time.
As we all know music acts a therapy and helps with the mood.

How it works:

What this program basicall does is, it collects input from the user via voice recognization and takes that input to search the song on youtube and play it for the user.
to search and play the song selenium is used. The process is automated to play the requested song.
 
Dependencies:

You will need python to run this program, you can download it from :https://www.python.org/downloads/
After installing python you will need to install speech recognition you can type this command into your command prompt to download and install it : pip install SpeechRecognition.
After that you will need to install pyaudio you can type this command into your command prompt to download and install it : pip install PyAudio.
At last you will need to install selenium that you can type this command into your command prompt to download and install it: pip install selenium.
You will also need chromedriver.exe and you will have to keep it in the same folder as the program file. To download chromedriver https://chromedriver.chromium.org/
You need to update the chromdriver only when theres a new chrome version.

Important : This chromedriver is used for Chrome 96 so make sure you have chrome version 96 before running the program.

How to run this program :

Step 1 : Once you run the program it will show some text where it will tell you to say a word.
         Try to say that word 2-3 times as sometimes it takes time to recognise the voice from the microphone.
       
  ![Desktop Screenshot 2021 11 28 - 22 23 43 07](https://user-images.githubusercontent.com/78537973/143778273-61072072-5934-402f-b8a2-92dee8bf5f01.png)
      
  ![Desktop Screenshot 2021 11 28 - 22 28 36 68](https://user-images.githubusercontent.com/78537973/143778338-53b136a6-966f-4936-9d98-8a524f9adbcb.png)


Step 2 : After that it will ask you to say the song name. When you give the song name it will search and play the song within 2-3 seconds.
![Desktop Screenshot 2021 11 28 - 22 33 43 20](https://user-images.githubusercontent.com/78537973/143778298-539085e6-f64a-4ef1-bd9c-7454f70c78b6.png)

![Desktop Screenshot 2021 11 28 - 22 33 44 12](https://user-images.githubusercontent.com/78537973/143778302-fecc2e1f-3235-4cb5-8df3-72d67d58e3b7.png)

Step 3: To put another song just say "Play songname" and it will start another song for you.
        if you say close then it will close the bot for you.
        
![Desktop Screenshot 2021 11 28 - 23 32 04 87](https://user-images.githubusercontent.com/78537973/143780230-739670ba-ff90-4448-bd2f-cd24090ef90c.png)
        
![Desktop Screenshot 2021 11 28 - 23 32 05 31](https://user-images.githubusercontent.com/78537973/143780233-9ccbd1c9-a778-443c-9d87-79f41a5d89d6.png)

And thats it, its easy as that.
Make sure you download both chromedriver.exe and Musicbot.py and put them in the same folder.
