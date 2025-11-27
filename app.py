
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from pypdf import PdfReader, PdfWriter
import io

app = Flask(__name__)
# Em produção, troque por uma chave secreta forte
app.config["SECRET_KEY"] = "troque-esta-chave"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_file = request.files.get("original")
        pdf_5_file = request.files.get("pdf_5")
        pdf_2_file = request.files.get("pdf_2")

        # Validações básicas
        if not original_file or original_file.filename == "":
            flash("Envie o PDF original.", "error")
            return redirect(url_for("index"))

        if not pdf_5_file or pdf_5_file.filename == "":
            flash("Envie o PDF com as 5 páginas a serem inseridas após a primeira.", "error")
            return redirect(url_for("index"))

        if not pdf_2_file or pdf_2_file.filename == "":
            flash("Envie o PDF com as 2 páginas a serem inseridas após a última.", "error")
            return redirect(url_for("index"))

        try:
            # Lê os PDFs diretamente do upload (streams em memória)
            original_reader = PdfReader(original_file.stream)
            insert_first_reader = PdfReader(pdf_5_file.stream)
            insert_last_reader = PdfReader(pdf_2_file.stream)

            writer = PdfWriter()
            num_pages_original = len(original_reader.pages)

            if num_pages_original == 0:
                flash("O PDF original está vazio.", "error")
                return redirect(url_for("index"))

            # 1) Adiciona a primeira página do original
            writer.add_page(original_reader.pages[0])

            # 2) Adiciona TODAS as páginas do PDF das 5 páginas
            for page in insert_first_reader.pages:
                writer.add_page(page)

            # 3) Adiciona as páginas restantes do original (da 2ª até a última)
            for i in range(1, num_pages_original):
                writer.add_page(original_reader.pages[i])

            # 4) Adiciona TODAS as páginas do PDF das 2 páginas
            for page in insert_last_reader.pages:
                writer.add_page(page)

            # Gera o PDF em memória para download
            output_stream = io.BytesIO()
            writer.write(output_stream)
            output_stream.seek(0)

            return send_file(
                output_stream,
                as_attachment=True,
                download_name="pdf_modificado.pdf",
                mimetype="application/pdf",
            )
        except Exception as e:
            print("Erro ao processar PDFs:", e)
            flash("Ocorreu um erro ao processar os PDFs. Verifique se os arquivos são válidos.", "error")
            return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    # Execução local
    app.run(debug=True)
