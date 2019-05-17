# LogPlayBacker

log 再生機能のデモコード. リファクタが間に合っておらずゴミが混じっており、ご容赦ください...

## 環境

```
$ python -v

$ pip -v
```

## 起動

バージョンを揃える

```
$ pyenv install 3.5.1

$ pyenv local
```

依存パッケージの DL, 直で入れたくない場合は virtual-env などを使うこと

```
$ pip install -r requirements.txt
```

Server を立ち上げておく (server コードは[こちら](https://github.com/sadnessOjisan/Form-Museum))

```
$ yarn run start:local

$ yarn run mock:local
```

selenium を実行

```
$ python main.py
```
