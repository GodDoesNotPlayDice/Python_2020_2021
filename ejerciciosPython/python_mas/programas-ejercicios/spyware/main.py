def main():
    import src
    user = src.UserSelect()
    docs = src.DocsLocation(user)
    return src.ExtractDocs(docs)

if __name__ == '__main__':
    print(main())