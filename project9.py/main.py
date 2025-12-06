import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ===============================================================
#   SALES DATA ANALYZER CLASS  (OOP IMPLEMENTATION)
# ===============================================================

class SalesDataAnalyzer:

    def __init__(self):
        self.df = None  # main dataset variable

    # -----------------------------------------------------------
    # 1. LOAD CSV DATA
    # -----------------------------------------------------------
    def load_data(self):
        try:
            file = input("\nEnter CSV file path: ")
            self.df = pd.read_csv(file)
            print("\nDataset loaded successfully!\n")
            print(self.df.head())
        except:
            print("\nError: Unable to load file. Please check path.\n")

    # -----------------------------------------------------------
    # 2. EXPLORE DATA  (FIXED: NOW INSIDE CLASS)
    # -----------------------------------------------------------
    def explore_data(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")

            ch = int(input("Enter your choice: "))

            # 1. First 5 rows
            if ch == 1:
                print("\n===== First 5 rows =====")
                print(self.df.head())

            # 2. Last 5 rows
            elif ch == 2:
                print("\n===== Last 5 rows =====")
                print(self.df.tail())

            # 3. Column names
            elif ch == 3:
                print("\n===== Column Names =====")
                print(list(self.df.columns))

            # 4. Data types
            elif ch == 4:
                print("\n===== Data Types =====")
                print(self.df.dtypes)

            # 5. Basic info
            elif ch == 5:
                print("\n===== Basic Info =====")
                print(self.df.info())

            # Back
            elif ch == 6:
                return

            else:
                print("Invalid choice! Please try again.")

    # -----------------------------------------------------------
    # 3. PERFORM DATAFRAME OPERATIONS
    # -----------------------------------------------------------
    def dataframe_operations(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Select a specific column")
            print("2. Filter rows based on a condition")
            print("3. Add a new column")
            print("4. Delete a column")
            print("5. Sort data by column")
            print("6. Show updated DataFrame")
            print("7. Back to Main Menu")

            ch = input("Enter your choice: ")

            # 1. show column
            if ch == "1":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(self.df[col])
                else:
                    print("Column not found!")

            # 2. filter rows
            elif ch == "2":
                col = input("Enter column name to filter: ")
                if col not in self.df.columns:
                    print("Column not found!")
                    continue
                val = input("Enter value to match: ")
                print(self.df[self.df[col] == val])

            # 3. add column
            elif ch == "3":
                col = input("Enter new column name: ")
                val = input("Enter value for all rows: ")
                self.df[col] = val
                print("Column added successfully!")

            # 4. delete column
            elif ch == "4":
                col = input("Enter column name to delete: ")
                if col in self.df.columns:
                    self.df.drop(columns=[col], inplace=True)
                    print("Column deleted!")
                else:
                    print("Column not found!")

            # 5. sort data
            elif ch == "5":
                col = input("Enter column name to sort: ")
                if col in self.df.columns:
                    self.df = self.df.sort_values(by=col)
                    print("Data sorted successfully!")
                else:
                    print("Column not found!")

            # 6. show final df
            elif ch == "6":
                print("\n=== Updated DataFrame ===")
                print(self.df)

            elif ch == "7":
                return

            else:
                print("Invalid choice!")

    # -----------------------------------------------------------
    # 4. HANDLE MISSING DATA
    # -----------------------------------------------------------
    def handle_missing_data(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to Main Menu")

            ch = input("Enter your choice: ")

            # 1. show missing rows
            if ch == "1":
                missing = self.df[self.df.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print("\nRows with missing values:")
                    print(missing)

            # 2. fill with mean
            elif ch == "2":
                num_cols = self.df.select_dtypes(include=['float64', 'int64'])
                if num_cols.empty:
                    print("No numeric columns available!")
                else:
                    self.df[num_cols.columns] = num_cols.fillna(num_cols.mean())
                    print("Missing values filled with mean!")

            # 3. drop missing rows
            elif ch == "3":
                before = len(self.df)
                self.df.dropna(inplace=True)
                after = len(self.df)
                print(f"Dropped {before - after} rows containing missing values.")

            # 4. replace with custom value
            elif ch == "4":
                val = input("Enter value to replace missing values with: ")
                self.df.fillna(val, inplace=True)
                print("Replacement completed!")

            elif ch == "5":
                return

            else:
                print("Invalid choice!")

    # -----------------------------------------------------------
    # 5. GENERATE DESCRIPTIVE STATISTICS
    # -----------------------------------------------------------
    def descriptive_statistics(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Generate Descriptive Statistics ==")
            print("1. Show summary statistics")
            print("2. Show statistics for a specific column")
            print("3. Show correlation matrix")
            print("4. Show unique values for a column")
            print("5. Back to Main Menu")

            ch = input("Enter your choice: ")

            # 1. Full summary
            if ch == "1":
                print("\n===== Summary Statistics =====")
                print(self.df.describe(include='all'))

            # 2. stats for single column
            elif ch == "2":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(f"\n===== Statistics for '{col}' =====")
                    print(self.df[col].describe())
                else:
                    print("Column not found!")

            # 3. correlation matrix
            elif ch == "3":
                numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
                if numeric_df.empty:
                    print("No numeric columns available for correlation.")
                else:
                    print("\n===== Correlation Matrix =====")
                    print(numeric_df.corr())

            # 4. unique values
            elif ch == "4":
                col = input("Enter column name: ")
                if col in self.df.columns:
                    print(f"\nUnique values in '{col}':")
                    print(self.df[col].unique())
                else:
                    print("Column not found!")

            elif ch == "5":
                return

            else:
                print("Invalid choice! Try again.")
                
    # -----------------------------------------------------------
    # 6. DATA VISUALIZATION  (FULL CODE WITH STACK PLOT)
    # -----------------------------------------------------------
    def visualize_data(self):
        if self.df is None:
            print("Load dataset first!")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Line Plot")
            print("2. Bar Plot")
            print("3. Histogram")
            print("4. Scatter Plot")
            print("5. Heatmap (Correlation)")
            print("6. Stack Plot")
            print("7. Back to Main Menu")

            ch = input("Enter your choice: ")

            # ----------------------------------------------
            # 1. LINE PLOT
            # ----------------------------------------------
            if ch == "1":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.plot(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Line Plot: {y} vs {x}")
                    plt.grid()
                    plt.show()
                else:
                    print("Invalid columns!")

            # ----------------------------------------------
            # 2. BAR PLOT
            # ----------------------------------------------
            elif ch == "2":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.bar(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Bar Chart: {y} by {x}")
                    plt.show()
                else:
                    print("Invalid columns!")

            # ----------------------------------------------
            # 3. HISTOGRAM
            # ----------------------------------------------
            elif ch == "3":
                col = input("Enter column for histogram: ")
                if col in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.hist(self.df[col], bins=20)
                    plt.xlabel(col)
                    plt.title(f"Histogram of {col}")
                    plt.show()
                else:
                    print("Column not found!")

            # ----------------------------------------------
            # 4. SCATTER PLOT
            # ----------------------------------------------
            elif ch == "4":
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                if x in self.df.columns and y in self.df.columns:
                    plt.figure(figsize=(8,5))
                    plt.scatter(self.df[x], self.df[y])
                    plt.xlabel(x)
                    plt.ylabel(y)
                    plt.title(f"Scatter Plot: {y} vs {x}")
                    plt.show()
                else:
                    print("Invalid columns!")

            # ----------------------------------------------
            # 5. HEATMAP
            # ----------------------------------------------
            elif ch == "5":
                numeric_df = self.df.select_dtypes(include=['int64', 'float64'])
                if numeric_df.empty:
                    print("No numeric columns available for heatmap.")
                else:
                    plt.figure(figsize=(10,6))
                    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
                    plt.title("Correlation Heatmap")
                    plt.show()

            # ----------------------------------------------
            # 6. STACK PLOT
            # ----------------------------------------------
            elif ch == "6":
                print("\nEnter multiple numeric columns for stack plot (comma separated):")
                print("Example: sales,profit,expenses")

                columns = input("Enter column names: ").replace(" ", "").split(",")

                # Check if columns exist
                missing = [c for c in columns if c not in self.df.columns]
                if missing:
                    print("These columns do not exist:", missing)
                    continue

                # Confirm numeric columns
                non_numeric = [c for c in columns if self.df[c].dtype not in ['int64', 'float64']]
                if non_numeric:
                    print("Non-numeric columns cannot be used:", non_numeric)
                    continue

                x_col = input("Enter X-axis column: ")

                if x_col not in self.df.columns:
                    print("X-axis column not found!")
                    return

                plt.figure(figsize=(10,6))
                plt.stackp
                
    # -----------------------------------------------------------
    # 7. SAVE VISUALIZATION
    # -----------------------------------------------------------
    def save_visualization(self):
        if self.last_plot is None:
            print("\nNo visualization found! Create a plot first.\n")
            return

        print("\n== Save Visualization ==")
        file_name = input("Enter filename (e.g., chart.png): ")

        try:
            self.last_plot.savefig(file_name)
            print(f"Visualization saved successfully as '{file_name}'\n")
        except Exception as e:
            print("Error saving file:", e)



# ===============================================================
#                     MAIN MENU PROGRAM
# ===============================================================

def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n==============================")
        print(" Sales Data Analysis Program ")
        print("==============================")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Values")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.load_data()

        elif choice == "2":
            analyzer.explore_data()
            
        elif choice == "3":
            analyzer.dataframe_operations()
        
        elif choice == "4":
            analyzer.handle_missing_data()
 
        elif choice == "5":
            analyzer.descriptive_statistics()
    
        elif choice == "6":
            analyzer.visualize_data()
        
        elif choice == "7":
            analyzer.save_visualization()

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Feature not added yet!")


# Run program
main()
