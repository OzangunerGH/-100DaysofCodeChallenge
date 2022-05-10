import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermark App")
        self.geometry("300x100")
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
 
        self.create_widgets()
 
    def create_widgets(self):
        self.file_btn()
        self.quit_btn()
 
    def file_btn(self):
        self.button = tk.Button(text="Search for Picture", command=self.fileDailog)
        self.button.grid(column=0, row=0, sticky=tk.W, pady=10)
 
    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                   filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
        self.label = tk.Label(text="Image Upload")
        self.label.grid(sticky=tk.N)
        self.label.configure(text=self.fileName)
        self.watermark_image()
 
    def quit_btn(self):
        self.quit_button = tk.Button(self, text='Quit',
                                     command=self.quit)
        self.quit_button.grid(column=0, row=1, sticky=tk.W)
 
    def watermark_image(self):
        # opens image
        image = self.fileName
        image = Image.open(image)
 
        # copies image to make changes
        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)
 
        # selects font
        font = ImageFont.truetype("arial.ttf", 100)
 
        # add watermark
        draw.text((0, 0), 'Ozan Guner © ', (255, 255, 255), font=font)
 
        # save the image
        self.save_image(watermark_image)
 
    def save_image(self, image):
        try:
            image.save('./images/watermarked-image.jpeg')
        except OSError:
            return print("Could not find file path")
 
        return print("Saved Successful")
 
 
app = App()
app.mainloop()
