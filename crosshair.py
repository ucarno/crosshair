from tkinter import Tk, Canvas, PhotoImage, NW


class CrosshairWindow:
    def __init__(self):
        self.root = Tk()
        self.root.attributes(
            '-transparentcolor', '#ffffff',
            '-topmost', '1'
        )
        self.root.overrideredirect(1)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

    def start(self):
        image = PhotoImage(file='crosshair.png')

        canvas = Canvas(self.root, width=image.width(), height=image.height(), highlightthickness=0)
        canvas.pack(fill='both')
        canvas.create_image(0, 0, anchor=NW, image=image)

        self.root.geometry(f'%sx%s+%s+%s' % (
            image.width(),  # width
            image.height(),  # height
            round(self.screen_width/2 - image.width()/2),  # x offset
            round(self.screen_height/2 - image.height()/2),  # y offset
        ))

        self.root.lift()
        self.root.mainloop()
