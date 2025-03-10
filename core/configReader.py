import os


class ConfigReader:
    def __init__(self, filename="_navicrc"):
        self.filename = filename
        self.config = {}
        self.original_lines = []
        self._load_config()

    def _load_config(self):
        """Load and parse the configuration file."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Config file {self.filename} not found")

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                self.original_lines.append(line)
                line = line.strip()
                # 忽略空行和注释
                if not line or line.startswith("#"):
                    continue
                # 解析键值对
                if "=" in line:
                    key, value = line.split("=", 1)
                    self.config[key.strip()] = value.strip()

    def get(self, key, default=None):
        """
        Get a configuration value by key.
        Return default if key does not exist.
        """
        return self.config.get(key, default)

    def set(self, key, value):
        """
        Set a configuration value.
        If the key exists, update it;
        otherwise, add it.
        """
        self.config[key] = value

    def save(self, filename=None):
        """
        Save the configuration back to the file,
        preserving comments and formatting.
        """
        if filename is None:
            filename = self.filename

        with open(filename, "w", encoding="utf-8") as file:
            for line in self.original_lines:
                stripped_line = line.strip()
                # If the line is a key-value pair, update it
                if "=" in stripped_line and not stripped_line.startswith("#"):
                    key = stripped_line.split("=", 1)[0].strip()
                    if key in self.config:
                        # Replace the value with the updated one
                        file.write(f"{key}={self.config[key]}\n")
                        continue
                file.write(line)

    def __getitem__(self, key):
        """Support accessing values using config['key'] syntax."""
        return self.config[key]

    def __contains__(self, key):
        """Support 'key in config' syntax."""
        return key in self.config


# Example usage
if __name__ == "__main__":
    try:
        config = ConfigReader("_navicrc")
        print("Host:", config.get("host"))
        print("Port:", config.get("port"))
        print("Username:", config["username"])
        print("Password:", config.get("password", "未设置"))
        # Update a value
        config.set("port", "8080")
        config.set("new_key", "new_value")  # Add a new key-value pair

        # Save the updated configuration
        config.save()
        print("Configuration saved successfully.")
    except FileNotFoundError as e:
        print(e)
