
from PIL import Image


def convert_png_to_pdf():
    # Открываем диалоговое окно для выбора исходных PNG-файлов
    file_paths = filedialog.askopenfilenames(
        title="Выберите PNG файлы",
        filetypes=[("PNG files", "*.png")]
    )

    if not file_paths:
        return

    success_count = 0
    for file_path in file_paths:
        try:
            # Открываем изображение через Pillow
            image = Image.open(file_path)

            # Конвертируем в RGB (если был альфа-канал)
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Предлагаем пользователю выбрать место и имя для сохранения готового PDF
            pdf_path = filedialog.asksaveasfilename(
                title="Сохранить как PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialfile="converted.pdf"  # Имя по умолчанию
            )

            # Если пользователь нажал «Отмена» в окне сохранения, пропускаем этот файл
            if not pdf_path:
                continue

            # Сохраняем в выбранный файл
            image.save(pdf_path, "PDF", resolution=100.0)
            success_count += 1

        except Exception as e:
            print(f"Ошибка при конвертации {file_path}: {e}")

    if success_count > 0:
        messagebox.showinfo("Успех", f"Успешно конвертировано и сохранено файлов: {success_count}")

# Инструкция в окне
label = tk.Label(root, text="Нажмите кнопку ниже, чтобы\nвыбрать и сохранить PNG как PDF", font=("Arial", 11), pady=20)
label.pack()

# Кнопка запуска конвертации
btn = tk.Button(root, text="Выбрать PNG и сохранить PDF", command=convert_png_to_pdf, bg="#4CAF50", fg="white",
                font=("Arial", 10, "bold"), padx=10, pady=5)
btn.pack(pady=10)

# Запуск главного цикла окна
root.mainloop()
