from sec_edgar_downloader import Downloader
from gooey import Gooey
import argparse


@Gooey
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c", "--companies", required=True, nargs="+", help="A list of company tickers"
    )

    parser.add_argument(
        "-f",
        "--form",
        required=True,
        type=str,
        help="The requested form type, ie: 10-K, 10-Q",
    )

    parser.add_argument(
        "-s",
        "--start",
        required=False,
        type=int,
        default=2014,
        help="The starting year as an integer",
    )

    parser.add_argument(
        "-e",
        "--end",
        required=False,
        type=int,
        default=2024,
        help="The ending year as an integer",
    )

    args = vars(parser.parse_args())

    companies = args["companies"]
    form = args["form"]
    start = args["start"]
    end = args["end"]

    # List of company tickers
    # companies = [
    #     "CLH",
    #     "DY",
    #     "EME",
    #     "FIX",
    #     "FSS",
    #     "HUBB",
    #     "MTZ",
    #     "PRIM",
    #     "RBC",
    #     "ROAD",
    #     "SPXC",
    #     "STRL",
    # ]

    for company in companies:

        dl = Downloader(
            "Gryzen Financial Group, LLC",
            "gryzencoaching@gmail.com",
        )

        # Set to 10 years
        for year in range(start, end):
            dl.get(
                form,
                company,
                after=f"{year}-01-01",
                before=f"{year+1}-01-01",
                # download_details=False,
            )


main()
