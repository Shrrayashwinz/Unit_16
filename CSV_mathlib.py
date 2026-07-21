"""
Program Name: lab16_ssrinivasan3-2.py

Author: Shrrayash Srinivasan

Purpose: I am to analzye the Ohio Unemployment Rate data from a CSV file and plot it using matplotlib. I am also using OOP/SOLID Principles
to help structure my code.

Date: December 12, 2025 
"""

 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class DataLoader:
    """Handles loading and preparing CSV data."""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load_data(self) -> pd.DataFrame:
        """Load CSV and convert DATE column to datetime."""
        self.df = pd.read_csv(self.filepath)
        self.df['DATE'] = pd.to_datetime(self.df['DATE'], format='%Y-%m-%d')
        return self.df


class HeaderAnalyzer:
    """Analyzes and prints header information."""
    @staticmethod
    def analyze_headers(df: pd.DataFrame) -> None:
        for i, col in enumerate(df.columns):
            print(f"{i}: {col}")


class Plotter:
    """Handles plotting of unemployment data."""
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_unemployment(self) -> None:
        plt.figure(figsize=(14, 7))
        plt.plot(self.df['DATE'], self.df['OHUR'], color='red', linewidth=1.5)
        plt.title('Ohio Unemployment Rate by Month (1976–2022)')
        plt.xlabel('Date')
        plt.ylabel('Unemployment Rate (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    """ Step 1: Load data """
    loader = DataLoader('OHUR.csv')
    df = loader.load_data()

    """ Step 2: Analyze headers """
    HeaderAnalyzer.analyze_headers(df)

    """ Step 3: Plot data """
    plotter = Plotter(df)
    plotter.plot_unemployment()


if __name__ == "__main__": 
    main()
 



