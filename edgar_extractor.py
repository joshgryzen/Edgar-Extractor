from sec_downloader import Downloader
from sec_downloader.types import RequestedFilings
from gooey import Gooey
import argparse
from bs4 import BeautifulSoup
import os


@Gooey
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--companies",
        required=True,
        nargs="+",
        help="A list of company tickers separated by spaces, ie: AMZN CLH META",
    )

    parser.add_argument(
        "-f",
        "--form",
        required=True,
        type=str,
        help="The requested form type, ie: 10-K, 10-Q",
    )

    parser.add_argument(
        "-l",
        "--limit",
        required=False,
        type=int,
        default=10,
        help="The limit for the number of most recent documents.",
    )

    args = vars(parser.parse_args())

    companies = args["companies"]
    form = args["form"]
    limit = args["limit"]

    if not os.path.exists(os.path.join("sec-edgar-filings")):
        os.mkdir("sec-edgar-filings")

    # List of company tickers
    for company in companies:

        if not os.path.exists(os.path.join("sec-edgar-filings", company)):
            os.mkdir(os.path.join("sec-edgar-filings", company))

        dl = Downloader(
            "Gryzen Financial Group, LLC",
            "gryzencoaching@gmail.com",
        )

        metadatas = dl.get_filing_metadatas(
            RequestedFilings(
                form_type=form,
                ticker_or_cik=company,
                limit=limit,
            )
        )

        for metadata in metadatas:
            print(metadata, end="\n\n")

            html = dl.download_filing(url=metadata.primary_doc_url).decode()
            path = os.path.join("sec-edgar-filings", company)
            out_path = os.path.join(
                path,
                company + "-" + form + "-" + metadata.filing_date + ".txt",
            )
            with open(
                out_path,
                "w",
                encoding="utf-8",
            ) as text_file:
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text()
                text_file.write(text)


if __name__ == "__main__":
    main()
