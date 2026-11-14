import streamlit as st
from PIL import Image
import io

st.title("Конвертер PNG в PDF")
st.write("Загрузите изображения в формате PNG, чтобы объединить их в один PDF-файл.")

# Компонент для загрузки файлов (поддерживает выбор нескольких картинок)
uploaded_files = st.file_uploader(
    "Выберите PNG файлы", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if uploaded_files:
  st.success(f"Загружено файлов: {len(uploaded_files)}")

  # Кнопка для запуска конвертации
  if st.button("Конвертировать в PDF"):
    try:
      images = []
      for file in uploaded_files:
        img = Image.open(file)
        # Конвертируем в RGB (необходимо для сохранения в PDF формата RGB)
        if img.mode != "RGB":
          img = img.convert("RGB")
        images.append(img)

      # Создаем буфер в памяти для сохранения PDF
      pdf_buffer = io.BytesIO()

      if images:
        # Сохраняем первую картинку с добавлением остальных страниц
        images[0].save(
            pdf_buffer,
            format="PDF",
            save_all=True,
            append_images=images[1:],
            resolution=100.0,
        )
        pdf_buffer.seek(0)

        st.success("PDF успешно создан!")

        # Кнопка скачивания готового файла
        st.download_button(
            label="Скачать готовый PDF",
            data=pdf_buffer,
            file_name="converted_images.pdf",
            mime="application/pdf",
        )
    except Exception as e:
      st.error(f"Произошла ошибка при конвертации: {e}")
