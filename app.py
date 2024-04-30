# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import io

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pdf_database.db"
# db = SQLAlchemy(app)

# class PDF(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     pdf_data = db.Column(db.LargeBinary)

#     def __repr__(self):
#         return f"PDF({self.id})"
    

# @app.route("/upload", methods=["POST"])
# def upload_pdf():
#     pdf_file = request.files["pdf_file"]
#     pdf_data = pdf_file.read()
#     pdf = PDF(pdf_data=pdf_data)
#     db.session.add(pdf)
#     db.session.commit()
#     return "PDF uploaded successfully"


# @app.route("/download/<int:pdf_id>", methods=["GET"])
# def download_pdf(pdf_id):
#     pdf = PDF.query.get(pdf_id)
#     if pdf is None:
#         return "PDF not found", 404
#     return send_file(io.BytesIO(pdf.pdf_data), as_attachment=True, attachment_filename="example.pdf")