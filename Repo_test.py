import os
import shutil
from IPython.display import clear_output

#@title <h1><B><font color=red>𝗥𝗲𝗽𝗼 𝗧𝗲𝘀𝘁 𝗛𝗼𝘄 𝗧𝗼 𝗚𝗼𝗼𝗴𝗹𝗲  <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }
# @markdown <div><center><a href="https://github.com/SudoR2spr/text-leech-bot/graphs/contributors"><img height="200"  src="https://opengraph.githubassets.com/niszjzjrdlws31z4hurrzabavate8t0g/SudoR2spr/text-leech-bot"></center></div>
# @markdown <br><center><h2><strong><font color=red>🔗 𝗥𝗲𝗽𝗼 𝗧𝗲𝘀𝘁 𝗛𝗼𝘄 𝗧𝗼 𝗚𝗼𝗼𝗴𝗹𝗲  🔗</strong></h2></center>


#@markdown <font color=ORANGE>🔗 Please enter the GitHub repository URL: 🔗
GITHUB_URL = "https://github.com/terabox25/AMR-Url_Uploader.git"  #@param {type:"string"}

# Determine base directory based on environment
base_dir = './repo'  # Save repo in ./repo directory relative to current directory

# Function to clone or update the repository
def clone_or_update_repo(repo_url, base_directory):
    repo_name = os.path.basename(repo_url).replace('.git', '')
    project_dir = os.path.join(base_directory, repo_name)

    # Check if the repository directory exists
    if os.path.exists(project_dir):
        print(f"Deleting existing repository at: {project_dir} ...")
        shutil.rmtree(project_dir)
        print("Deleted existing repository successfully!")

    # Clone the repository
    print(f"Cloning repository from {repo_url}...")
    clone_cmd = f"git clone {repo_url} {project_dir}"
    os.system(clone_cmd)
    print("Repository cloned successfully!")

    return project_dir

# Clone or update the repository
project_dir = clone_or_update_repo(GITHUB_URL, base_dir)

# Navigate to the project directory
print(f"Entering project directory: {os.path.basename(project_dir)}...")
os.chdir(project_dir)
print("Entered project directory successfully!")

clear_output()

#@markdown <font color=ORANGE>🔧 Please enter the requirements.txt file path: 🔧
PIP_INSTALL = "requirements.txt"  #@param {type:"string"}

# Install required dependencies
print("Installing required dependencies...")
!pip install -r {PIP_INSTALL}
print("All requirements installed successfully!")

clear_output()

#@markdown ### <font color=ORANGE>🔧 Environment Variables 🔧

#@markdown <center> <font color=green>✍️ Paste Your Telegram API ID From ≫ my.telegram.org <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }

API_ID = ""  #@param {type:"string"}
os.environ['API_ID'] = API_ID

#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram API HASH From ≫ my.telegram.org <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }

API_HASH = ""  #@param {type:"string"}
os.environ['API_HASH'] = API_HASH

#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram BOT TOKEN From ≫ @BotFather <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }

BOT_TOKEN = ""  #@param {type:"string"}
os.environ['BOT_TOKEN'] = BOT_TOKEN

#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram OWNER ID  From ≫ @id_bot <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }


OWNER_ID = ""  #@param {type:"string"}
os.environ['OWNER_ID'] = OWNER_ID


#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram log Channel   From ≫ @id_bot <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }


LOG_CHANNEL = ""  #@param {type:"string"}
os.environ['LOG_CHANNEL'] = LOG_CHANNEL


#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram log Channel   From ≫ @id_bot <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }


DATABASE_URL = ""  #@param {type:"string"}
os.environ['DATABASE_URL'] = DATABASE_URL

#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram log Channel   From ≫ @id_bot <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }


URL = "vipurl.in"  #@param {type:"string"}
os.environ['URL'] = URL

#@markdown <center> </font> <font color=green>✍️ Paste Your Telegram log Channel   From ≫ @id_bot <img src='https://i.ibb.co/ZLbRGmT/Picsart-24-02-16-14-30-48-873.png' height="40" /> </center> { display-mode: "form" }


API = "b804a4eadf0a6b8171b7d3ef0ff64c675436b493"  #@param {type:"string"}
os.environ['API'] = API
clear_output()

#@markdown <font color=ORANGE>🔧 Please enter the Profile command: 🔧
RUN_COMMAND = "python3 bot.py"  #@param {type:"string"}

# Run the bot
print(f"Running command: {RUN_COMMAND} ...")
!{RUN_COMMAND}
print("✔️ Execution completed!")
