def main():
    ex = input("File name: ").lower().strip()
    if ex.endswith("gif"):
        print("image/gif")
    elif ex.endswith("png"):
        print("image/png")
    elif ex.endswith("jpg") or ex.endswith("jpeg"):
        print("image/jpeg")
    elif ex.endswith("zip"):
        print("application/zip")
    elif ex.endswith("pdf"):
        print("application/pdf")
    elif ex.endswith("txt"):
        print("text/plain")
    else:
       print("application/octet-stream")

main()