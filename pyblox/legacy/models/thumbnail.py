from enum import Enum

class ThumbnailResponse:
    def __init__(self, data: dict):
        self.target_id = data.get("targetId")
        self.state = data.get("state")
        self.image_url = data.get("imageUrl")
        self.version =  data.get("version")

class ThumbnailFormat(Enum):
    PNG = "png"
    JPEG = "jpeg"
    WEBP = "Webp"

class ThumbnailSize(Enum):
    SIZE_30X30 = "30x30"
    
    SIZE_42X42 = "42x42"
    SIZE_48X48 = "48x48"
    
    SIZE_50X50 = "50x50"
    
    SIZE_60X62 = "60x62"
    
    SIZE_75X75 = "75x75"
    
    SIZE_110X110 = "110x110"
    SIZE_140X140 = "140x140"
    SIZE_150X150 = "150x150"
    SIZE_160X100 = "160x100"
    SIZE_160X600 = "160x600"
    
    SIZE_250X250 = "250x250"
    SIZE_256X144 = "256x144"
    SIZE_300X250 = "300x250"
    
    SIZE_304X166 = "304x166"
    SIZE_330X110 = "330x110"
    SIZE_384X216 = "384x216"
    SIZE_396X216 = "396x216"
    
    SIZE_420X420 = "420x420"
    SIZE_480X270 = "480x270"

    SIZE_512X512 = "512x512"
    SIZE_576X324 = "576x324"

    SIZE_660X220 = "660x220"

    SIZE_700X700 = "700x700"
    SIZE_728X90 = "728x90"
    SIZE_768X432 = "768x432"

    SIZE_930X280 = "930x480"

    SIZE_1200X80 = "1200x80"
    SIZE_1320X440 = "1320x440"
    SIZE_1440X456 = "1440x456"