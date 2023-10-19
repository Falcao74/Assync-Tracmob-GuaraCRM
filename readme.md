# Consumo de dados Assíncronos  - API Trackmob - GuaraCRM - API - V1
<h3> Readme in pt-BR, en-US and es-ES </h3>
<h1></h1>
<h1></p><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Django?style=for-the-badge">&nbsp;&nbsp;&nbsp;
<img alt="Mysql" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white"></h1>

<h1> Descrição (pt-BR) </h1>
<p>Implementação em Python do consumo dos dados, via API V1, disponibilizados pela Trackmob, para utilização dos recursos vindos do GuaraCRM</p>

<h1>Instalação e primeiro uso (pt-BR): </h1>

<ul>
<h2> Para iniciar o projeto, digite os comandos abaixo: </h2>
        <li> (Dependendo do seu SO) python3 ou python -m venv env </li>
        <li> source env/bin/activate (Linux/Mac) ou .\env\Scripts\activate (Windows - Prompt ou Powershell) </li>
        <li> pip install -r requirements.txt </li>
        <li> Pode ser necessário atualizar seu pip. Se for o caso, atualize e repita o processo anterior </li>
        <li> Atenção: Caso vá executar este processo utilizando banco de dados diferente do mysql, algumas adaptações são necessárias </li>
</ul>

<h1> Criando as tabelas no seu banco de dados: MYSQL (pt-BR)</h1>
<ul>
    <li> Acesse o diretório SQL deste projeto </li>
    <li>Abra o arquivo <b>script.sql</b> que está dentro do diretório e copie o código.</li>
    <li>Crie um banco de dados MySQL com o nome que desejar na sua máquina ou na nuvem.</li>
    <li>Abra seu editor de SQL - Como o MySQL Workbench ou HeidiSQL ou outro.</li>
    <li>Crie uma nova consulta SQL, cole o código que está no arquivo e execute.</li>
    <li><i>Obs.: Caso o banco seja na nuvem, não esqueça de autorizar o firewall para aceitar conexões do ip da máquina que vai executar o processo.</i></li>
</ul>
    <br />

<h1> Setando as configurações de acesso à api e ao banco de dados (pt-BR): </h1>
<ul>
    <li> Renomeie o arquivo <b>settings_example.py </b>para <b>settings.py</b> </li>
    <li> Preencha os dados de configuração do banco de dados e seu token de acesso. </li>
</ul>
<br />

<h1> Uso (pt-BR) </h1>
<ul>
    <li>Com o banco de dados já criado;</li>
    <li>Ambiente virtual ativado (<b>env</b>);</li>
    <li>No terminal do VSCode, Sublime, ou prompt do seu sistema operacional, digite: <b>python app.py</b> no Windows ou <b>python3 app.py</b> no Linux/Mac</li>
</ul>
<ul>
    <li><b>Outra opção:</b></li>
    <li>Você pode criar um executável para executar automaticamente </li>
    <li>Para isso, execute o comando: <b>pyinstaller --onefile app.py</b></li>
    <li>Será criada a pasta <i>dist</i> no seu diretório e um executável</li>
</ul>

---

# Asynchronous Data Consumption - Trackmob API - GuaraCRM - API V1

<h1> Description (en-US) </h1>
<p>Python implementation for data consumption, via API V1, provided by Trackmob, to utilize resources from GuaraCRM</p>

<h1> Installation and Initial Usage (en-US): </h1>

<ul>
<h2> To start the project, enter the following commands: </h2>
        <li> (Depending on your OS) python3 or python -m venv env </li>
        <li> source env/bin/activate (Linux/Mac) or .\env\Scripts\activate (Windows - Command Prompt or PowerShell) </li>
        <li> pip install -r requirements.txt </li>
        <li> You may need to update your pip. If so, update it and repeat the previous step. </li>
        <li> Note: If you plan to run this process using a different database than MySQL, some adaptations are required. </li>
</ul>

<h1> Creating tables in your database: MYSQL (en-US) </h1>
<ul>
    <li> Access the SQL directory of this project </li>
    <li> Open the script.sql file inside the directory and copy the code. </li>
    <li> Create a MySQL database with the desired name on your local machine or in the cloud. </li>
    <li> Open your SQL editor, such as MySQL Workbench, HeidiSQL, or another. </li>
    <li> Create a new SQL query, paste the code from the file, and execute it. </li>
    <li> (Note: If the database is in the cloud, don't forget to authorize the firewall to accept connections from the machine's IP that will execute the process.) </li>
</ul>
    <br />

<h1> Configuring API and Database Access Settings (en-US) </h1>
<ul>
    <li> Rename the file settings_example.py to settings.py. Fill in the configuration data for the database and your access token. </li>
</ul>
<br />

<h1> Usage (en-US) </h1>
<ul>
    <li> With the database already created, virtual environment activated (env), and in your VSCode terminal, Sublime, or your OS command prompt, type python app.py on Windows or python3 app.py on Linux/Mac. </li>
</ul>
<ul>
    <li> Another option: You can create an executable to run automatically. To do that, execute the command pyinstaller --onefile app.py. A dist folder will be created in your directory with an executable. </li>
</ul>

---------

# Consumo de datos Asíncronos - API Trackmob - GuaraCRM - API V1

<h1> </h1>

<h1> Descripción (es-ES) </h1>
<p>Implementación en Python del consumo de datos, a través de la API V1, proporcionada por Trackmob, para utilizar los recursos de GuaraCRM.</p>

<h1> Instalación y Uso Inicial (es-ES): </h1>

<ul>
<h2> Para iniciar el proyecto, ingrese los siguientes comandos: </h2>
        <li> (Dependiendo de su SO) python3 o python -m venv env </li>
        <li> source env/bin/activate (Linux/Mac) o .\env\Scripts\activate (Windows - Command Prompt o PowerShell) </li>
        <li> pip install -r requirements.txt </li>
        <li> Es posible que deba actualizar su pip. Si es así, actualícelo y repita el paso anterior. </li>
        <li> Nota: Si planea ejecutar este proceso utilizando una base de datos diferente de MySQL, se requieren algunas adaptaciones. </li>
</ul>

<h1> Creación de tablas en su base de datos: MYSQL (es-ES) </h1>
<ul>
    <li> Acceda al directorio SQL de este proyecto. </li>
    <li> Abra el archivo script.sql dentro del directorio y copie el código. </li>
    <li> Cree una base de datos MySQL con el nombre deseado en su máquina local o en la nube. </li>
    <li> Abra su editor SQL, como MySQL Workbench, HeidiSQL o cualquier otro. </li>
    <li> Cree una nueva consulta SQL, pegue el código del archivo y ejecútelo. </li>
    <li> (Nota: Si la base de datos está en la nube, no olvide autorizar el firewall para aceptar conexiones desde la IP de la máquina que ejecutará el proceso.) </li>
</ul>
    <br />

<h1> Configuración de la API y las configuraciones de acceso a la base de datos (es-ES) </h1>
<ul>
    <li> Cambie el nombre del archivo settings_example.py a settings.py. Rellene los datos de configuración de la base de datos y su token de acceso. </li>
</ul>
<br />

<h1> Uso (es-ES) </h1>
<ul>
    <li> Con la base de datos ya creada, el entorno virtual activado (env), y en su terminal de VSCode, Sublime o en el símbolo del sistema de su SO, escriba python app.py en Windows o python3 app.py en Linux/Mac. </li>
</ul>
<ul>
    <li> Otra opción: Puede crear un ejecutable para ejecutarse automáticamente. Para hacerlo, ejecute el comando pyinstaller --onefile app.py. Se creará una carpeta dist en su directorio con un ejecutable. </li>
</ul>
