class SafetyGuard:
    def __init__(self):
        self.danger_keywords = [
            "rm -rf", "sudo rm", "mkfs", ":(){:|:&};:", 
            "> /dev/sda", "dd if=", "chmod 777 /"
        ]

    def check(self, command):
        for keyword in self.danger_keywords:
            if keyword in command:
                return False, keyword
        return True, None