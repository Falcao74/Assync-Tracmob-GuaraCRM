# Consumo de dados Assíncronos  - API Trackmob - GuaraCRM - API -V1
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Django?style=for-the-badge">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img alt="Mysql" src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
<h1> </h1>

<h1> Descrição </h1>
<p>Implementação em Python do consumo dos dados, via API V1, disponibilizados pela Trackmob, para utilização dos recursos vindos do GuaraCRM</p>

<h1>Instalação e primeiro uso: </h1>

<ul>
<h2> Para iniciar o projeto, digite os comandos abaixo: </h2>
        <li> (Dependendo do seu SO) python3 ou python -m venv env </li>
        <li> source env/bin/activate (Linux/Mac) ou .\env\Scripts\activate (Windows - Prompt ou Powershell) </li>
        <li> pip install -r requirements.txt </li>
        <li> Pode ser necessário atualizar seu pip. Se for o caso, atualize e repita o processo anterior </li>
        <li> Atenção: Caso vá executar este processo utilizando banco de dados diferente do mysql, algumas adaptações são necessárias </li>
</ul>

<h1> Criando as tabelas no seu banco de dados: MYSQL</h1>
<ul>
    <li> Acesse o diretório SQL deste projeto </li>
    <li>Abra o arquivo <b>script.sql</b> que está dentro do diretório e copie o código.</li>
    <li>Crie um banco de dados MySQL com o nome que desejar na sua máquina ou na nuvem.</li>
    <li>Abra seu editor de SQL - Como o MySQL Workbench ou HeidiSQL ou outro.</li>
    <li>Crie uma nova consulta SQL, cole o código que está no arquivo e execute.</li>
    <li><i>Obs.: Caso o banco seja na nuvem, não esqueça de autorizar o firewall para aceitar conexões do ip da máquina que vai executar o processo.</i></li>
</ul>
    <br />

<h1> Setando as configurações de acesso à api e ao banco de dados: </h1>
<ul>
    <li> Renomeie o arquivo <b>settings_example.py </b>para <b>settings.py</b> </li>
    <li> Preencha os dados de configuração do banco de dados e seu token de acesso. </li>
</ul>
<br />

<h1> Uso </h1>
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

