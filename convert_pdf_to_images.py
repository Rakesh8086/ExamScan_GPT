from pdf2image import convert_from_path


def convert_specific_pages(pdf_path, page_type, total_pages, output_folder=None):
    # print(pdf_path)
    images = []
    if page_type == "Every page":
        for page_number in range(1, total_pages + 1):
            image = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, fmt='jpeg')
            images.extend(image)
    if page_type == "Every Even-numbered page":
        for page_number in range(1, total_pages + 1):
            if page_number % 2 == 0:
                image = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, fmt='jpeg')
                images.extend(image)
    if page_type == "Every Odd-numbered page":
        for page_number in range(1, total_pages + 1):
            if page_number % 2 != 0:
                image = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, fmt='jpeg')
                images.extend(image)
    return images

