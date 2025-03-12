# TransitFinder

基于高德api的线路查询工具

### 上手指南

#### 使用前配置
1. 下载python3并配置到环境环境变量
2. 下载requests模块，可以运行以下命令：
```
pip install requests
```

使用```-h```查看相应的参数选项
```
python Navic.py -h
```
#### 调用示例：
```
python Navic.py -k <your key> -c <city> -w <LineName>
```
参数解释，-k是临时的高德api密钥，-c是要查询的城市名，-w是是相应的线路名<br>
城市名支持中文和城市编码

#### 设置默认配置
使用```--set```选项开启设置模式，这个模式下能继续使用```-k```，```-c```以及```-f```
这会让程序保存默认的key,city,file，
设置好默认的参数之后就不需要调用相应参数，程序可以直接使用-w运行
***注意***：一旦设定默认的file，那么程序会默认输出到相应文件
```
python Navic.py -w <lineName>
```
#### 删除默认设置
使用```-r```选项进入删除模式
```
python Navic.py -r
```
程序会需要输入k/c/f来删除默认配置，k/c/f可以任意组合，可以大写
```
