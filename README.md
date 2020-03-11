
Passwordつきｚｉｐ暗号化ファイルを送ります
Passwordを送ります
Aん号化（暗号化）
Protocol

2020年3月現在、世間にはPPAPなどと呼ばれる作法があるようです。
ついカッとなってPythonで本ツールを作りました。

「実行するのにPythonを入れろって？なんだいそれは。冗談だろ？」

はいはい。わかってますよ。
環境を作るとか、そういうしちめんどくさいことはやりたくないですよね。
だから今回はそのまま使えるexeファイルも用意しました。

とはいえ大事なデータを守ろうというツールです。
中でどんな処理が行われているか分からないものは使いたくないでしょう。

そこで、本ツールのソースコードを公開することで、必要に応じ中身を確認した上で利用したい人が自分でビルドできるようにすることにしました。
もしかすると、改造してGUIをつけたい人もいるかもしれません。
お好きにどうぞ。ご自由にご活用ください。


### 現在利用可能な機能

・秘密鍵ファイルと公開鍵ファイルの生成  
・指定された公開鍵を用いたデータの暗号化  
・指定された秘密鍵を用いたデータの復号  


## 依存関係:

    Python ：3.6以降
    PyCryptodome ： (pip install pycryptodome)
    PyInstaller ： (pip install pyinstaller)


# 利用手順

### Tested System:
* windows10が動くそこらへんのPC

### 通常の利用方法
1. 公開鍵と秘密鍵の生成

```bash:
key_gen <password_for_your_keys>
```

2. 指定した公開鍵を使って暗号化


```bash:
enc <target_file_name> <path_to_rsa_pub_key> <result_file_name>
```

3. 自分の秘密鍵を使って暗号化データを復号

```bash:
dec <path_to_target_data> <path_to_rsa_private_key> <password_for_your_keys>
```


## 実行ファイルの作成方法

```bash:
pyinstaller key_gen.py --onefile
```

```bash:
pyinstaller enc.py --onefile
```

```bash:
pyinstaller dec.py --onefile
```


## 参考文献

### 参考リンク

「私たちはなぜパスワード付きｚｉｐファイルをメール添付するのか」
https://digitalforensic.jp/2019/12/23/column595/



