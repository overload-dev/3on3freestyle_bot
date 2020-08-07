# 3on3freestyle_bot Project
## 1. What is it?
This project is a bot that reports user game history of PlayStation 4 online game 3on3 FreeStyle using the Discord bot api.
The site used to request game records is as follows.</br>
<http://3on3rank.fsgames.com/></br><br/>
This project was developed using python3 in the ubuntu linux environment.</br>
You need to be subscribed to Discord to run this project.</br>
Detailed information required for the development of Discord Bot can be found in the official document.</br>
<https://discord.com/developers/docs/intro/></br>
* * *
## 2. Git Repository Download
<pre><code>git clone https://github.com/leekanghyo/3on3freestyle_bot.git</code></pre>
* * *
## 3. Install required packages
<pre>
<code>
$sudo apt-get install python3
$sudo apt-get install python3-pip

$pip3 install discord
$pip3 install tabulate
</code>
</pre>
* * *
## 4. Project structure
<pre>
<code>
.
├── README.md
├── bot_3on3freestyle.py
├── constants.py
└── controller
    ├── userController.py
    ├── crewController.py
    └── commonController.py
</code>
</pre>
- constants.py: Manages TOKEN, api, and necessary constant information.
- bot_3on3freestyle.py: Load the bot. This is a file to wait for user commands and parse information on the screen.
- userController.py: This file is processed when bot_3on3freestyle.py is requested for information about user.
- crewController.py: This file is processed when bot_3on3freestyle.py is requested for information about crew.
- commonController.py: This file is to receive the necessary parameters, finally request the result, and return it to the user.
* * *
## 5. Create bot and get token
Access the site below.   
<https://discord.com/developers/applications/><br/></br>
<img src="./imgs/sample_1.jpg"></img><br/>
Click the New Application button at the top right of the page to create an application with an appropriate name.<br/></br>
<img src="./imgs/sample_2.jpg"></img><br/>
Click the Bot item in the menu and then click the AddBot button to create a Bot with an appropriate name.<br/></br>
<img src="./imgs/sample_3.jpg"></img><br/>
Click the Copy button of the TOKEN item to copy the TOKEN, then paste it into the TOKEN variable of constants.py in the Python project.<br/><br/>
<img src="./imgs/sample_4.jpg"></img><br/>
In the Discord client, add an appropriately named test server.<br/></br>
<img src="./imgs/sample_5.jpg"></img><br/>
Return to the browser and click on the General Information item in the menu.<br/>
Copy the CLIENT ID, paste it into the client_id parameter at the address below, and load the page.</br>
<pre><code>
https://discord.com/oauth2/authorize?client_id=[Your Client ID]&scope=bot&permissions=8
</pre></code>
<br/><br/>
<img src="./imgs/sample_6.jpg"></img><br/>
Select the server you just created from the server list and complete the connection approval process.<br/><br/>
Now return to the project and run the Bot with the command below.
<pre><code>
python3 bot_3on3freestyle.py
</pre></code>
<br>
<img src="./imgs/sample_7.jpg"></img><br/>

If you connect to the test server from the Discord client, you can check that the bot is connected.<br/>
Enter the [!help] command to bring up the command list.<br/>
