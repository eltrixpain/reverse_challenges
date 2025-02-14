from PIL import Image
import crc8

def timg_to_image(timg_path, output_path):
    with open(timg_path, 'rb') as f:
        magic = f.read(4)
        if magic != b'TIMG':
            raise ValueError("Not a valid TIMG file")
        
        version = f.read(4)  
        width = int.from_bytes(f.read(4), byteorder='big')
        height = int.from_bytes(f.read(4), byteorder='big')
        signature = f.read(4)  
        
        red_data = []
        green_data = []
        blue_data = []
        
        for _ in range(height):
            chunk_header = f.read(4)
            if chunk_header != b'DATR':
                raise ValueError(f"Expected DATR, got {chunk_header}")
            red_row = list(f.read(width))
            crc_byte = f.read(1)
            red_data.append(red_row)
        
        for _ in range(height):
            chunk_header = f.read(4)
            if chunk_header != b'DATG':
                raise ValueError(f"Expected DATG, got {chunk_header}")
            green_row = list(f.read(width))
            crc_byte = f.read(1)
            green_data.append(green_row)
        
        for _ in range(height):
            chunk_header = f.read(4)
            if chunk_header != b'DATB':
                raise ValueError(f"Expected DATB, got {chunk_header}")
            blue_row = list(f.read(width))
            crc_byte = f.read(1)
            blue_data.append(blue_row)
        
        pixels = []
        for row in range(height):
            for col in range(width):
                r = red_data[row][col]
                g = green_data[row][col]
                b = blue_data[row][col]
                pixels.append((r, g, b))
        
        footer = f.read(4)
        if footer != b'DATE':
            print("Warning: Missing DATE footer")

    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    img.save(output_path)

timg_to_image("flag.timg", "recovered.png")
