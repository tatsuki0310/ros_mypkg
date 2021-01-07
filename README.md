# ros_mypkg

ロボットシステム学の課題2のROSパッケージです。

## 動作環境

以下のような環境で動作確認を行っています。

- ROS Noetic
  - OS: Ubuntu 20.04.1 LTS
  - Device: Raspberry pi 4 Model B
  
## インストール方法

- [ros_setup_scripts_Ubuntu20.04_server](http://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04\server)を参照しROSのインストールを行います。

- [ロボットシステム学第10回](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)を参照しワークスペースの準備をします。

- `git`を使用してこのパッケージをダウンロードします。

　```bash
  cd ~/catkin_ws/src
  git clone https://github.com/tatsuki0310/ros_mypkg.git
  ```

- `catkin_make`を使用してパッケージをビルドします。

  ```bash
  cd ~/catkin_ws && catkin_make
  ```

## パッケージについて

send.pyで1～100000の数値をランダムで生成し、return.pyで偶数か奇数かを判断するためのトピック間通信を行います。

### [discrimination.launch](https://github.com/tatsuki0310/ros_mypkg/blob/main/launch/discrimination.launch)

- [send.py](https://github.com/tatsuki0310/ros_mypkg/blob/main/scripts/send.py)で数値をランダムに生成して
[return.py](https://github.com/tatsuki0310/ros_mypkg/blob/main/scripts/return.py)で受け取り偶数と奇数の判断を行う。

-　cloneした後、次のコマンドを実行します。

```bash
roslaunch ros_mypkg discrimination.launch
```

- 個別で実行する場合(端末は3つ用意してそれぞれのコマンドを実行)

```bash
roscore
rosrun ros_mypkg send.py
rosrun ros_mypkg return.py
```

- 実行すると左側に数値がランダムで出力され、右側で奇数(odd)か偶数(even)か判断します。

## デモ動画

- [デモ動画はこちらです。](https://youtu.be/GsKB5UEl5V4)

## 著者

[Tatsuki Saito](https://github.com/tatsuki0310)

ROSセットアップの参考:
[Ryuichi Ueda](https://github.com/ryuichiueda)

## ライセンス
[BSD 3-clause "New" or "Revised" License](https://github.com/tatsuki0310/ros_mypkg/blob/main/LICENSE)
