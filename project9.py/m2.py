import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================

# Load Dataset Function
# ============================================================


def load_dataset():
    print("\n== Load Dataset ==")
    path = input("Enter the path of the dataset (CSV file): ")

    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None


# ============================================================
# Explore Data Function
# ============================================================


def explore_data(df):
    while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Back to Main Menu")

        ch = int(input("\nEnter your ch: "))

        if ch ==  1 : 
            print("\n== First 5 Rows ==")
            print(df.head())

        elif ch == 2 :  
            print("\n== Last 5 Rows ==")
            print(df.tail())

        elif ch == 3 :  
            print("\n== Column Names ==")
            print(df.columns.tolist())

        elif ch == 4 :  
            print("\n== Data Types ==")
            print(df.dtypes)

        elif ch == 5 :  
            print("\n== Basic Info ==")
            print(df.info())

        elif ch == 6 :
            break
        else:
            print("Invalid choice! Try again.")


# ============================================================
# DataFrame Operations
# ============================================================


def dataframe_operations(df):
    while True:
        print("\n== DataFrame Operations ==")
        print("1. Show shape (rows, columns)")
        print("2. Summary statistics")
        print("3. Sort by a column")
        print("4. Back to Main Menu")
        
        cho = int(input("\nEnter your cho: "))

        if cho == 1:
            print("\nShape:", df.shape)

        elif cho == 2:
            print("\nSummary Statistics:")
            print(df.describe())
            
        elif cho == 3:
            col = input("Enter column to sort by: ")
            if col in df.columns:
                print(df.sort_values(by=col))
            else:
                print("❌ Invalid column")
                
        elif cho == 4 :
            break

        else:
            print("Invalid option! Try again.")



# ============================================================
# HANDLE MISSING VALUES
# ============================================================

def handle_missing_values(df):

    # Convert blank strings, spaces, NA-like text → NaN
    
    df.replace(["", " ", "NA", "None", "nan"], pd.NA, inplace=True)

    while True:
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            missing_rows = df[df.isnull().any(axis=1)]
            if missing_rows.empty:
                print("\nNo missing values found in the dataset!")
            else:
                print("\nRows with missing values:")
                print(missing_rows)

        elif choice == 2:
            numeric_cols = df.select_dtypes(include='number').columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            print("\nMissing numeric values filled with MEAN.")

        elif choice == 3:
            df.dropna(inplace=True)
            print("\nRows containing missing values DROPPED.")

        elif choice == 4:
            value = input("Enter value to fill missing: ")
            df.fillna(value, inplace=True)
            print("\nMissing values replaced with:", value)

        elif choice == 5:
            break

        else:
            print("Invalid choice! Try again.")

    return df

# ============================================================
# 5. DataTool CLASS (Advanced Operations)
# ============================================================

class DataTool:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df_original = pd.read_csv(filepath)
        self.df = self.df_original.copy()

    # MAIN menu under section 5
    
    def advanced_menu(self):
        while True:
            print("\n======= ADVANCED DATA OPERATIONS =======")
            print("1. Mathematical Operations")
            print("2. Combine DataFrames")
            print("3. Split DataFrame")
            print("4. Search / Sort / Filter / Aggregate")
            print("5. Statistical Functions")
            print("6. Back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.math_operations()

            elif choice == 2:
                self.combine_data()

            elif choice == 3:
                self.split_data()

            elif choice == 4:
                self.search_sort_filter()

            elif choice == 5:
                self.stats()

            elif choice == 6:
                break

            else:
                print("❌ Invalid choice!")

    # 1 Mathematical ops
    
    def math_operations(self):
        print("\n--- Mathematical Operations ---")
        print("1. Add constant")
        print("2. Subtract constant")
        print("3. Multiply constant")
        print("4. Divide constant")

        col = input("Enter column name: ")

        if col not in self.df.columns:
            print("❌ Column not found!")
            return

        try:
            const = float(input("Enter constant: "))
        except ValueError:
            print("❌ Invalid number!")
            return

        option = int(input("Choose operation (1-4): "))

        if option == 1:
            self.df[col] = self.df[col] + const
        
        elif option == 2:
            self.df[col] = self.df[col] - const
        
        elif option == 3:
            self.df[col] = self.df[col] * const
        
        elif option == 4:
            if const == 0:
                print("❌ Cannot divide by zero!")
                return
            self.df[col] = self.df[col] / const
        
        else:
            print("❌ Invalid choice!")
            return

        print("\nUpdated DataFrame:")
        print(self.df.head())

    # 2 Combine Data
    
    def combine_data(self):
        print("\n--- Combine DataFrames ---")
        path = input("Enter path of second CSV: ")

        try:
            df2 = pd.read_csv(path)
        except:
            print("❌ Cannot load file!")
            return

        print("\n1. Concatenate")
        print("2. Merge on common column")
        print("3. Join on index")
        option = int(input("Choose: "))

        if option == 1:
            self.df = pd.concat([self.df, df2], ignore_index=True)

        elif option == 2:
            col = input("Enter common column: ")
            if col not in self.df.columns or col not in df2.columns:
                print("❌ Column not found!")
                return
            self.df = pd.merge(self.df, df2, on=col)

        elif option == 3:
            self.df = self.df.join(df2, lsuffix="_left", rsuffix="_right")

        else:
            print("❌ Invalid choice!")
            return

        print("\nCombined DataFrame:")
        print(self.df.head())

    # 3 Split data
    
    def split_data(self):
        col = input("Enter column to split by: ")

        if col not in self.df.columns:
            print("❌ Column not found!")
            return

        for value, group in self.df.groupby(col):
            print(f"\n=== Group: {value} ===")
            print(group)

    # 4 Search / Sort / Filter
    
    def search_sort_filter(self):
        print("\n--- Search / Sort / Filter / Aggregate ---")
        print("1. Search value")
        print("2. Sort")
        print("3. Filter by condition")
        print("4. Aggregate functions")

        choice = int(input("Choose: "))

        if choice == 1:
            col = input("Column: ")
            val = input("Value: ")
            print(self.df[self.df[col].astype(str) == val])

        elif choice == 2:
            col = input("Column: ")
            asc = input("Ascending (y/n): ").lower() == "y"
            print(self.df.sort_values(by=col, ascending=asc))

        elif choice == 3:
            col = input("Column: ")
            cond = input("Condition (>, <, ==): ")
            v = input("Value: ")
            print(self.df.query(f"{col} {cond} {v}"))

        elif choice == 4:
            col = input("Column: ")
            print("\nSum:", self.df[col].sum())
            print("Mean:", self.df[col].mean())
            print("Max:", self.df[col].max())
            print("Min:", self.df[col].min())
            print("Count:", self.df[col].count())

        else:
            print("❌ Invalid choice!")

    # 5 Stats
    
    def stats(self):
        print("\n--- Statistical Functions ---")
        print(self.df.describe())
        print("\nStandard Deviation:\n", self.df.std(numeric_only=True))
        print("\nVariance:\n", self.df.var(numeric_only=True))
        print("\nQuantiles:\n", self.df.quantile([0.25, 0.5, 0.75]))
        print("\nCorrelation Matrix:\n", self.df.corr(numeric_only=True))

# ============================================================
# Data vasuaizationl
# ============================================================

def visualization_menu(df):

    while True:
        print("\n=== Visualization Menu ===")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Back to Main Menu")

        ch = int(input("Enter your choice: "))
        
        # 1. BAR CHART
        
        if ch == 1:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            print("\nMatplotlib Bar Chart...")
            plt.figure()
            plt.bar(df[x], df[y])
            plt.title("Bar Chart (Matplotlib)")
            plt.show()
            
        # 2. LINE CHART
        
        elif ch == 2:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            print("\nMatplotlib Line Plot...")
            plt.figure()
            plt.plot(df[x], df[y])
            plt.title("Line Plot (Matplotlib)")
            plt.show()
        
        # 3. SCATTER PLOT

        elif ch == 3:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            print("\nMatplotlib Scatter Plot...")
            plt.figure()
            plt.scatter(df[x], df[y])
            plt.title("Scatter Plot (Matplotlib)")
            plt.show()
            
        # 4. PIE CHART (Seaborn doesn’t have pie)
 
        elif ch == 4:
            col = input("Enter column for Pie chart: ")
            pie_data = df[col].value_counts()

            print("\nMatplotlib Pie Chart...")
            plt.figure()
            plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
            plt.title("Pie Chart")
            plt.show()
    
        # 5. HISTOGRAM

        elif ch == 5:
            col = input("Enter column for Histogram: ")

            print("\nMatplotlib Histogram...")
            plt.figure()
            plt.hist(df[col], bins=10)
            plt.title("Histogram (Matplotlib)")
            plt.show()
            
        # 6. STACK PLOT        

        elif ch == 6:
            c1 = input("Enter 1st column: ")
            c2 = input("Enter 2nd column: ")

            print("\nMatplotlib Stack Plot...")
            plt.figure()
            plt.stackplot(df.index, df[c1], df[c2], labels=[c1, c2])
            plt.legend()
            plt.title("Stack Plot")
            plt.show()
    
        elif ch == 7:
            break
        
        else:
            print("Invalid choice!")

# ============================================================
# Data vasuaizationl
# ============================================================
   
def save_plot(df):

    print("\n== Save Visualization ==")
    filename = input("Enter file name to save the plot (e.g., plot.png): ")

    try:
        plt.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")
    except Exception as e:
        print("Error saving file:", e)



# -------------------------------------------------------------------------
# Main Menu
# -------------------------------------------------------------------------


def main():
    dataset = None

    while True:
        print("\n=== MENU ===")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame operation")
        print("4. Handle Missing data ")
        print("5. Generate Descriptive Statistics")
        print("6. Data vasuaizationl")
        print("7. Save vasuaizationl")
        print("8. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1 :
            dataset = load_dataset()


        elif choice == 2 :
            if dataset is not None:
                explore_data(dataset)
            else:
                print(" Please load a dataset first!")
        
               
        elif choice == 3 :
            if dataset is not None:
                dataframe_operations(dataset)
            else:
                print(" Please load a dataset first!")
        
        
        elif choice == 4:
            if dataset is not None:
                handle_missing_values(dataset)
            else:
                print(" Please load a dataset first!")
             
                
        elif choice == 5:
            file = input("Enter CSV path again for DataTool: ")
            tool = DataTool(file)

            while True:
                print("\n======== DataTool MENU ========")
                print("1. Show DataFrame")
                print("2. Reset Data")
                print("3. Advanced Data Operations")
                print("4. Back")

                ch = int(input("Enter choice: "))

                if ch == 1:
                    print(tool.df)

                elif ch == 2:
                    tool.df = tool.df_original.copy()
                    print("Data Reset Done!")

                elif ch == 3:
                    tool.advanced_menu()

                elif ch == 4:
                    break

                else:
                    print("❌ Invalid choice!")


        elif choice == 6:
            if dataset is not None:
                visualization_menu(dataset)
            else:
                print("Please load a dataset first!")
                

        elif choice == 7:
            if dataset is not None:
                save_plot(dataset)
            else:
                print("Please load a dataset first!")


        elif choice == 8:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

     
if __name__ == "__main__":
    main()