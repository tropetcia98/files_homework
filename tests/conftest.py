import os.path
import pytest
from zipfile import ZipFile
from set_path import *
import shutil


@pytest.fixture(scope="session", autouse=True)
def create_archive():
    files = ['english_for_everyone_level_1_course_book_beginner.pdf', 'file_example_XLSX_50.xlsx', 'industry.csv']
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with ZipFile(ZIP_FILE, 'w') as zf:
        for file in files:
            add_file = os.path.join(FILE_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCES_DIR)
