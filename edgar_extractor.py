from sec_edgar_downloader import Downloader
from gooey import Gooey
from tkinter import messagebox
import tkinter as tk
import argparse


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
        "-s",
        "--start",
        required=False,
        type=int,
        default=2014,
        help="The starting year as an integer, ie: 2014",
    )

    parser.add_argument(
        "-e",
        "--end",
        required=False,
        type=int,
        default=2024,
        help="The ending year as an integer. Must be greater than the starting year, ie: 2024",
    )

    args = vars(parser.parse_args())

    companies = args["companies"]
    form = args["form"]
    start = args["start"]
    end = args["end"]

    if start > end:
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showwarning(
            "Input Error!",
            f"Ending year cannot be before starting year.",
        )
        return

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
