import dotenv 
import os 

PROG_PATH= os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(PROG_PATH, ".." , '.env')

dotenv.load_dotenv(dotenv_path=ENV_FILE)