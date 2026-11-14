import streamlit as st
from PIL import Image
import io

# Словарь с переводами для интерфейса
translations = {
    "Русский": {
        "title": "Конвертер PNG в PDF",
        "desc": "Загрузите изображения, чтобы конвертировать каждое из них в отдельный PDF-файл.",
        "uploader": "Выберите файлы (PNG, JPG, JPEG)",
        "uploaded_count": "Загружено файлов:",
        "btn_convert": "Конвертировать все в PDF",
        "ready": "Готовые к скачиванию файлы:",
        "download": "📥 Скачать",
        "error": "Ошибка при обработке файла"
    },
    "Polski": {
        "title": "Konwerter PNG na PDF",
        "desc": "Prześlij obrazy, aby przekonwertować każdy z nich na osobny plik PDF.",
        "uploader": "Wybierz pliki (PNG, JPG, JPEG)",
        "uploaded_count": "Przesłano plików:",
        "btn_convert": "Konwertuj wszystko do PDF",
        "ready": "Pliki gotowe do pobrania:",
        "download": "📥 Pobierz",
        "error": "Błąd podczas przetwarzania pliku"
    },
    "English": {
        "title": "PNG to PDF Converter",
        "desc": "Upload images to convert each of them into a separate PDF file.",
        "uploader": "Choose files (PNG, JPG, JPEG)",
        "uploaded_count": "Uploaded files:",
        "btn_convert": "Convert all to PDF",
        "ready": "Ready to download:",
        "download": "📥 Download",
        "error": "Error processing file"
    }
}

# Выбор языка в боковой панели (сайдбаре)
selected_lang = st.sidebar.selectbox(
    "🌐 Language / Язык / Język", 
    ["Русский", "Polski", "English"]
)

# Получаем словарь текстов для выбранного языка
t = translations[selected_lang]

# Интерфейс приложения с использованием выбранного языка
st.title(t["title"])
st.write(t["desc"])

# Компонент для загрузки файлов
uploaded_files = st.file_uploader(
    t["uploader"], type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{t['uploaded_count']} {len(uploaded_files)}")

    # Кнопка для запуска конвертации
    if st.button(t["btn_convert"]):
        st.write(f"### {t['ready']}")
        
        for uploaded_file in uploaded_files:
            try:
                img = Image.open(uploaded_file)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                pdf_buffer = io.BytesIO()
                img.save(pdf_buffer, format="PDF", resolution=100.0)
                pdf_buffer.seek(0)

                original_name = uploaded_file.name
                base_name = original_name.rsplit('.', 1)[0]
                pdf_filename = f"{base_name}.pdf"

                st.download_button(
                    label=f"{t['download']} {pdf_filename}",
                    data=pdf_buffer,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    key=original_name
                )
            except Exception as e:
                st.error(f"{t['error']} {uploaded_file.name}: {e}")
