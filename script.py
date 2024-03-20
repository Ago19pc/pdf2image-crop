
# import module
from pdf2image import convert_from_path
from PIL import Image
 
# Store Pdf with convert_from_path function
pdf_path = r'C:\Users\ago19\IdeaProjects\IS24-AM04\risorse_grafiche\grafiche\CODEX_cards_gold_front.pdf'
OUTPUT = r"C:\Users\ago19\Desktop\pdf2img\images"
images = convert_from_path(pdf_path, poppler_path = r'C:\Users\ago19\Desktop\pdf2img\poppler-24.02.0\Library\bin')
 
for i, im in enumerate(images):
    left = 34
    top = 34
    right = 578
    bottom = 413
    print("Tagliando immagine...")
    im1 = im.crop((left, top, right, bottom))
    print("Salvando immagine...")
    im1.save(r'C:\Users\ago19\Desktop\pdf2img\cropped\\' + str(i) + '.jpeg')