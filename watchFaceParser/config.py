class Config:
    _dimensions = {
        "width": 360,
        "height": 360,
        "preview_width": 210,
        "preview_height": 210,
    }

    @staticmethod
    def getDimensions():
        return Config._dimensions

    @staticmethod
    def getImageWidth():
        return Config._dimensions["width"]

    @staticmethod
    def getImageWidthHalf():
        return Config.getImageWidth() // 2

    @staticmethod
    def getImageHeight():
        return Config._dimensions["height"]

    @staticmethod
    def getImageHeightHalf():
        return Config.getImageHeight() // 2

    @staticmethod
    def getPreviewWidth():
        return Config._dimensions["preview_width"]

    @staticmethod
    def getPreviewHeight():
        return Config._dimensions["preview_height"]
