# am2320 sensor

Raspberry Pi上でAM2320センサーを使うためのPythonコード。

## usage

smbusのインストール

    $ sudo apt-get install python-smbus

Pythonコードは以下。

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python am2320.py

