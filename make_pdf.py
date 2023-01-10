import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
# streamlit.components.v1 import iframe
def make_pdf(option_subject, kt13, bt13, btl13, thi13):
    #st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
    #st.title("🎓 Diploma PDF Generator")

    #st.write(
     #   "This app shows you how you can use Streamlit to make a PDF generator app in just a few lines of code!"
    #)

    #left, right = st.columns(2)

    #right.write("Here's the template we'll be using:")

    #right.image("template.png", width=300)

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("template.html")


    #left.write("Fill in the data:")
    #form = left.form("template_form")
#student = form.text_input("Student name")
    #course = form.selectbox(
        #"Choose course",
        #["Report Generation in Streamlit", "Advanced Cryptography"],
        #index=0,
    #)
    #grade = form.slider("Grade", 1, 100, 60)
    #submit = form.form_submit_button("Generate PDF")

    html = template.render(
            option_subject=option_subject,
            kt13=kt13,
            bt13=bt13,
            btl13=btl13,
            thi13=thi13,
            date=date.today().strftime("%B %d, %Y"),
        )
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config)
    st.balloons()

    st.success("🎉 Your diploma was generated!")
        # st.write(html, unsafe_allow_html=True)
        # st.write("")
    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )