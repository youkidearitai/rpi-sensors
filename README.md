# am2320 sensor

Raspberry Pi上でセンサーを使うためのPythonコード。

+ AM2320
+ LPS25H

## usage

smbusのインストール

    $ sudo apt-get install python-smbus

Pythonコードは以下。

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python am2320.py # am2320を実行する
    $ python lps25h.py # lps25hを実行する

