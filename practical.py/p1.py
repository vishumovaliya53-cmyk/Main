import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    def __init__(self):
        self.df = None

    # -----------------------------------------------------------
    # 1. LOAD DATA (CSV)
    # -----------------------------------------------------------
    def load_data(self, file_path):
        try:
            if not file_path(retail_sales.csv):
                print("❌ Invalid file format! Please upload a CSV file.")
                return
            
            self.df = pd.read_csv(file_path)

            print("\n✅ File loaded successfully!")
            print("\n===== First 5 Rows =====")
            print(self.df.head())

            print("\n===== Missing Values =====")
            print(self.df.isnull().sum())

            # Handle missing values (fill with 0)
            self.df.fillna(0, inplace=True)
            print("\n✅ Missing values handled (filled with 0).")

        except FileNotFoundError:
            print("❌ File not found! Enter correct file path.")
        except Exception as e:
            print("❌ Error:", e)

    # -----------------------------------------------------------
    # 2. CALCULATE METRICS (TOTAL, AVG, POPULAR PRODUCT)
    # -----------------------------------------------------------
    def calculate_metrics(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        print("\n===== SALES METRICS =====")

        try:
            total_sales = self.df["Total Sales"].sum()
            avg_sales = self.df["Total Sales"].mean()
            most_sold = self.df.groupby("Product")["Quantity Sold"].sum().idxmax()

            print(f"✔ Total Sales: {total_sales}")
            print(f"✔ Average Sales: {avg_sales}")
            print(f"✔ Most Popular Product: {most_sold}")

        except KeyError:
            print("❌ Required columns missing in dataset!")

    # -----------------------------------------------------------
    # 3. FILTER DATA
    # -----------------------------------------------------------
    def filter_data(self, column, value):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        if column not in self.df.columns:
            print("❌ Invalid column name!")
            return

        filtered = self.df[self.df[column] == value]
        print(f"\n===== Filtered Data ({column} = {value}) =====")
        print(filtered)
        return filtered

    # -----------------------------------------------------------
    # 4. DISPLAY SUMMARY
    # -----------------------------------------------------------
    def display_summary(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        print("\n===== DATA SUMMARY =====")
        print(self.df.describe())

    # -----------------------------------------------------------
    # 5. VISUALIZATIONS
    # -----------------------------------------------------------

    # Bar Chart – Total Sales by Category
    def plot_bar_chart(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        plt.figure(figsize=(8,5))
        sns.barplot(data=self.df, x="Category", y="Total Sales")
        plt.title("Total Sales by Category")
        plt.show()

    # Line Graph – Sales Trend Over Time
    def plot_line_chart(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        self.df["Date"] = pd.to_datetime(self.df["Date"])

        plt.figure(figsize=(10,5))
        sns.lineplot(data=self.df, x="Date", y="Total Sales", marker="o")
        plt.title("Sales Trend Over Time")
        plt.show()

    # Heatmap – Price vs Quantity Sold
    def plot_heatmap(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        corr = self.df[["Price", "Quantity Sold", "Total Sales"]].corr()
        plt.figure(figsize=(6,4))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

    # Scatter Plot – Price vs Total Sales
    def plot_scatter(self):
        if self.df is None:
            print("❌ Load dataset first!")
            return

        plt.figure(figsize=(6,5))
        sns.scatterplot(data=self.df, x="Price", y="Total Sales")
        plt.title("Price vs Total Sales")
        plt.show()


# -----------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------
if __name__ == "__main__":

    analyzer = RetailAnalyzer()

    print("\n===== RETAIL SALES DATA ANALYZER =====")

    file_path = input("Enter CSV file path (e.g., retail_sales.csv): ")

    analyzer.load_data(file_path)

    while True:
        print("\n========= MENU =========")
        print("1. Calculate Metrics")
        print("2. Filter Data")
        print("3. Display Summary")
        print("4. Bar Chart (Category vs Sales)")
        print("5. Line Chart (Sales Over Time)")
        print("6. Heatmap (Correlation)")
        print("7. Scatter Plot (Price vs Sales)")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.calculate_metrics()

        elif choice == "2":
            col = input("Enter column to filter (Category/Product): ")
            val = input("Enter value: ")
            analyzer.filter_data(col, val)

        elif choice == "3":
            analyzer.display_summary()

        elif choice == "4":
            analyzer.plot_bar_chart()

        elif choice == "5":
            analyzer.plot_line_chart()

        elif choice == "6":
            analyzer.plot_heatmap()

        elif choice == "7":
            analyzer.plot_scatter()

        elif choice == "8":
            print("✔ Exiting program... Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")
