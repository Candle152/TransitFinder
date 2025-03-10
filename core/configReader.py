import os

class ConfigReader:
    def __init__(self, filename="_navicrc"):
        self.filename = filename
        self.config = {}
        self._load_config()

    def _load_config(self):
        """加载配置文件"""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"配置文件 {self.filename} 不存在")

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                # 忽略空行和注释
                if not line or line.startswith("#"):
                    continue
                # 解析键值对
                if "=" in line:
                    key, value = line.split("=", 1)
                    self.config[key.strip()] = value.strip()

    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)

    def __getitem__(self, key):
        """支持通过 config['key'] 的方式获取值"""
        return self.config[key]

    def __contains__(self, key):
        """支持 'key' in config 的语法"""
        return key in self.config


# 示例用法
if __name__ == "__main__":
    try:
        config = ConfigReader("_navicrc")
        print("Host:", config.get("host"))
        print("Port:", config.get("port"))
        print("Username:", config["username"])
        print("Password:", config.get("password", "未设置"))
    except FileNotFoundError as e:
        print(e)
