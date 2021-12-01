# CAS Server
## Setup
### Create a new virtual environment
python3 -m venv cas_auth/venv
### Activate the virtual environment
#### Linux/MacOS
source cas_auth/venv/bin/activate
#### Windows
cas_auth\venv\Scripts\activate.bat
### Install the dependencies
pip3 install -r cas_auth/requirements.txt
### Prepare your settings.py and localsettings.py
In authserver/setup_templates you will find templates for the requires localsettings.py file. This file is gitignored and holds settings which are specific to your local project. Place it next to settings.py. A random secret key ycan be generated using the command "python manage.py newsecretkey". More Information is in the template files.