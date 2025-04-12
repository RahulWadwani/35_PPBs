def main(url):
    if url.startswith("https://"):
        print("This website uses HTTPS (secure).")
    elif url.startswith("http://"):
        print("This website uses HTTP (not secure).")
    else:
        print("This doesn't look like a complete URL.")
        

if __name__ == "__main__":
    url_link = input("Enter the link: ")
    main(url_link)
