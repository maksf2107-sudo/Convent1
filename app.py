import streamlit as st
from PIL import Image
import io

st.title("Конвертер PNG в PDF")
st.write("Загрузите изображения, чтобы конвертировать каждое из них в отдельный PDF-файл.")

# Компонент для загрузки нескольких файлов
uploaded_files = st.file_uploader(
    "Выберите файлы (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
    st.success(f"Загружено файлов: {len(uploaded_files)}")

    # Кнопка для запуска конвертации
    if st.button("Конвертировать все в PDF"):
        st.write("### Готовые к скачиванию файлы:")
        
        for uploaded_file in uploaded_files:
            try:
                # Открываем изображение через Pillow
                img = Image.open(uploaded_file)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Создаем буфер в памяти для конкретного файла
                pdf_buffer = io.BytesIO()
                img.save(pdf_buffer, format="PDF", resolution=100.0)
                pdf_buffer.seek(0)

                # Формируем имя нового файла (меняем расширение на .pdf)
                original_name = uploaded_file.name
                base_name = original_name.rsplit('.', 1)[0]
                pdf_filename = f"{base_name}.pdf"

                # Выводим кнопку скачивания для каждого обработанного файла
                st.download_button(
                    label=f"📥 Скачать {pdf_filename}",
                    data=pdf_buffer,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    key=original_name # Уникальный ключ для каждой кнопки
                )
            except Exception as e:
                st.error(f"Ошибка при обработке файла {uploaded_file.name}: {e}")
