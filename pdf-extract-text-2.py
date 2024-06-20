import logging
from slate3k import PDF
import slate3k as slate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path):
    """
  Extracts text from a PDF file.

  Args:
      pdf_path (str): The path to the PDF file.

  Returns:
      str: The extracted text.
  """

    with open(pdf_path, 'rb') as pdf_file:
        # Slate directly extracts text from the file object
        extracted_text = PDF(pdf_file)
    return "\n".join(extracted_text)


def extract_pdf_page_wise(pdf_path):
    """
    Extracts text from a PDF file page by page using slate3k and saves each page to a separate .txt file.

    Args:
        pdf_path (str): The path to the PDF file.
    """
    logger.info(f'File {pdf_path}: reading ...')

    with open(pdf_path, 'rb') as pdf_file:
        # Open the PDF using slate3k
        pdf = slate.PDF(pdf_file)

        # Iterate over each page in the PDF
        for page_num, page_text in enumerate(pdf):
            logger.info(f' p.{page_num + 1}')
            # Create a file name for the current page
            page_file_name = f"{pdf_path}_page_{page_num + 1}.txt"

            # Save the page text to the file
            with open(page_file_name, 'w', encoding='utf-8') as page_file:
                page_file.write(page_text)

            logger.info(f' p.{page_num + 1} saved: {page_file_name}')

    logger.info(f'Done!')


if __name__ == '__main__':
    pdf_file_path = 'data/UMAE_TRAUMA_PUEBLA_REQ_18023022639_MAYO_2023.pdf'
    # pdf_file_path = 'data/UMAE_ESP_SONORA_REQ_2023006432_AGOSTO_2023.pdf'

    # To extract page by page.
    extract_pdf_page_wise(pdf_file_path)

    # This was to extract the full doc.
    # extracted_text = extract_text_from_pdf(pdf_file_path)
    # print(extracted_text)
