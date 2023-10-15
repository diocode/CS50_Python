from fpdf import FPDF

class PDF():
    def __init__(self, prompt):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', 50)
        self._pdf.cell(0, 60, "CS50 Shirtificatite", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{prompt} took CS50")

    def save(self, prompt):
        self._pdf.output(prompt)

def main():
    prompt = input("Name: ").strip()
    pdf = PDF(prompt)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()