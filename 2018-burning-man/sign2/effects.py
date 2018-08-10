from PIL import Image


class FlatImage:
    def __init__(self, cols, rows, file_name):
        self.cols = cols
        self.rows = rows
        self.image = Image.open(file_name)

    def get_pixels(self, _ts):
        arr = self.image.load()
        return [arr[c, r][:3]
                for r in range(0, self.rows)
                for c in range(0, self.cols)]
