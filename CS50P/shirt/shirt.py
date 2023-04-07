from PIL import Image,ImageOps
import sys

try:
    f = sys.argv
    if len(f) < 3:
        sys.exit('Too few command-line arguments')
    elif len(f) > 3:
        sys.exit('Too many command-line arguments')
    f1 = f[1].lower()
    f2 = f[2].lower()
    if f1.endswith('.jpg') or f1.endswith('.jpeg') or f1.endswith('.png'):
        if f2.endswith('.jpg') or f2.endswith('.jpeg') or f2.endswith('.png'):
            extension1 = f1.split('.')[-1]
            extension2 = f2.split('.')[-1]
            if extension1 != extension2:
                sys.exit('Input and output have different extensions')

            with Image.open(f1) as im1, Image.open('shirt.png') as shirt:
                shirt_size = shirt.size
                im1 = ImageOps.fit(im1, size=shirt_size)
                im1.paste(shirt, shirt)
                im1.save(f2)

        else:
            sys.exit('Invalid output')
    else:
        sys.exit('Invalid input')
except Exception:
    sys.exit('Input does not exist')