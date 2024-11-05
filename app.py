import os
import json
import hashlib
import multiprocessing
from datetime import datetime
from PIL import Image
import pytesseract
import streamlit as st
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor
import numpy as np

class OCRCache:
    def __init__(self, cache_dir="/tmp/ocr_cache"):
        self.cache_dir = cache_dir
        self.cache_index_file = os.path.join(cache_dir, "cache_index.json")
        self.initialize_cache()
    
    def initialize_cache(self):
        os.makedirs(self.cache_dir, exist_ok=True)
        if not os.path.exists(self.cache_index_file):
            self.save_cache_index({})
    
    def get_file_hash(self, file_path):
        modification_time = os.path.getmtime(file_path)
        file_size = os.path.getsize(file_path)
        hash_string = f"{file_path}_{modification_time}_{file_size}"
        return hashlib.md5(hash_string.encode()).hexdigest()
    
    def load_cache_index(self):
        try:
            with open(self.cache_index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    
    def save_cache_index(self, index):
        with open(self.cache_index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
    
    def get_cached_text(self, file_path):
        file_hash = self.get_file_hash(file_path)
        cache_index = self.load_cache_index()
        
        if file_hash in cache_index:
            cache_file = os.path.join(self.cache_dir, f"{file_hash}.txt")
            if os.path.exists(cache_file):
                try:
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        return f.read()
                except Exception as e:
                    st.error(f"Error loading cache: {e}")
        return None
    
    def save_text_to_cache(self, file_path, text):
        file_hash = self.get_file_hash(file_path)
        cache_index = self.load_cache_index()
        
        cache_file = os.path.join(self.cache_dir, f"{file_hash}.txt")
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        cache_index[file_hash] = {
            'file_path': file_path,
            'cached_date': datetime.now().isoformat(),
            'cache_file': f"{file_hash}.txt"
        }
        self.save_cache_index(cache_index)

def optimize_image_for_ocr(image):
    if image.mode != 'L':
        image = image.convert('L')
    max_dimension = 2000
    if max(image.size) > max_dimension:
        ratio = max_dimension / max(image.size)
        new_size = tuple(int(dim * ratio) for dim in image.size)
        image = image.resize(new_size, Image.LANCZOS)
    image = Image.fromarray(np.uint8(np.clip((np.array(image) * 1.2), 0, 255)))
    return image

def process_page(img, language='hin+eng'):
    try:
        img = optimize_image_for_ocr(img)
        custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
        text = pytesseract.image_to_string(img, lang=language, config=custom_config)
        return text.strip()
    except Exception as e:
        st.error(f"Error processing page: {str(e)}")
        return ""

def extract_text_with_ocr_cached(pdf_file_path, cache_system):
    cached_text = cache_system.get_cached_text(pdf_file_path)
    if cached_text is not None:
        st.info(f"Using cached text for {os.path.basename(pdf_file_path)}")
        return cached_text
    
    try:
        images = convert_from_path(pdf_file_path, dpi=200, thread_count=multiprocessing.cpu_count(), grayscale=True, size=(1800, None))
        max_workers = min(multiprocessing.cpu_count(), len(images))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(process_page, images))
        
        extracted_text = "\n".join(filter(None, results))
        
        if extracted_text.strip():
            cache_system.save_text_to_cache(pdf_file_path, extracted_text)
        
        return extracted_text
    
    except Exception as e:
        st.error(f"Error during OCR extraction: {str(e)}")
        return ""

def main():
    st.title("PDF OCR Text Extractor with Caching")
    
    uploaded_files = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        cache_system = OCRCache()
        combined_text = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, pdf_file in enumerate(uploaded_files):
            # Save uploaded PDF to a temporary location
            temp_file_path = os.path.join("/tmp", pdf_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            
            text = extract_text_with_ocr_cached(temp_file_path, cache_system)
            if text:
                combined_text.append(text)
            
            # Update progress
            progress = (i + 1) / len(uploaded_files)
            progress_bar.progress(progress)
            status_text.text(f"Processed {i + 1}/{len(uploaded_files)} files")
        
        st.subheader("Extracted Text")
        st.text_area("Extracted Text", value="\n\n".join(combined_text), height=300)

if __name__ == "__main__":
    main()
