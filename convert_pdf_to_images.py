from pdf2image import convert_from_path


def convert_specific_pages(pdf_path, page_numbers, output_folder=None):
    images = []
    for page in page_numbers:
        image = convert_from_path(pdf_path, first_page=page, last_page=page, fmt='jpeg')
        images.extend(image)
    return images

