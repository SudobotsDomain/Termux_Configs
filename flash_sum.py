class Manufacturer:
    def __init__(self, name, cpu_model=None, cpu_cores=None, total_ram=None, boot_image_path=None, scatter_file_path=None, hardware_info=None):
        self.name = name
        self.cpu_model = cpu_model
        self.cpu_cores = cpu_cores
        self.total_ram = total_ram
        self.boot_image_path = boot_image_path
        self.scatter_file_path = scatter_file_path
        self.hardware_info = hardware_info

    def update_info(self, cpu_model=None, cpu_cores=None, total_ram=None, boot_image_path=None, scatter_file_path=None, hardware_info=None):
        if cpu_model:
            self.cpu_model = cpu_model
        if cpu_cores:
            self.cpu_cores = cpu_cores
        if total_ram:
            self.total_ram = total_ram
        if boot_image_path:
            self.boot_image_path = boot_image_path
        if scatter_file_path:
            self.scatter_file_path = scatter_file_path
        if hardware_info:
            self.hardware_info = hardware_info

    def generate_flash_summary(self):
        summary = f"Flash Summary for {self.name} Devices:\n"
        summary += f"CPU Model: {self.cpu_model}\n" if self.cpu_model else ""
        summary += f"CPU Cores: {self.cpu_cores}\n" if self.cpu_cores else ""
        summary += f"Total RAM: {self.total_ram} KB\n" if self.total_ram else ""
        summary += f"Boot Image Path: {self.boot_image_path}\n" if self.boot_image_path else ""
        summary += f"Scatter File Path: {self.scatter_file_path}\n" if self.scatter_file_path else ""
        summary += f"Hardware Info: {self.hardware_info}\n" if self.hardware_info else ""
        return summary


# Example Usage
samsung = Manufacturer(name="Samsung", cpu_model="Exynos 990", cpu_cores=8, total_ram=8192, boot_image_path="/path/to/boot.img.gz", scatter_file_path="/path/to/scatterfile.txt", hardware_info="Detected Samsung Hardware Info")
motorola = Manufacturer(name="Motorola", cpu_model="Snapdragon 730", cpu_cores=8, total_ram=6144, boot_image_path="/path/to/boot.img.gz", scatter_file_path="/path/to/scatterfile.txt", hardware_info="Detected Motorola Hardware Info")
nokia = Manufacturer(name="Nokia", cpu_model="Snapdragon 665", cpu_cores=8, total_ram=4096, boot_image_path="/path/to/boot.img.gz", scatter_file_path="/path/to/scatterfile.txt", hardware_info="Detected Nokia Hardware Info")

print(samsung.generate_flash_summary())
print(motorola.generate_flash_summary())
print(nokia.generate_flash_summary())
