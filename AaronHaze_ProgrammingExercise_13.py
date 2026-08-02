import sqlite3
import random
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# FUNCTION 1: Create database + table + insert 2023 data
# ---------------------------------------------------------

def create_database():
    conn = sqlite3.connect("population_AH.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # 10 Florida cities + estimated 2023 populations
    cities_2023 = {
        "Sarasota": 57900,
        "Venice": 27000,
        "Tampa": 403000,
        "Orlando": 316000,
        "Miami": 449000,
        "Jacksonville": 971000,
        "St. Petersburg": 263000,
        "Fort Myers": 96000,
        "Clearwater": 117000,
        "Lakeland": 115000
    }

    # Insert baseline 2023 data
    for city, pop in cities_2023.items():
        cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()


# ---------------------------------------------------------
# FUNCTION 2: Simulate 20 years of growth/decline
# ---------------------------------------------------------

def simulate_population():
    conn = sqlite3.connect("population_AH.db")
    cursor = conn.cursor()

    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cursor.fetchall()

    for city, base_pop in rows:
        population = base_pop

        for year in range(2024, 2044):  # 20 years
            rate = random.uniform(-0.03, 0.05)  # -3% decline to +5% growth
            population = int(population * (1 + rate))

            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, population))

    conn.commit()
    conn.close()


# ---------------------------------------------------------
# FUNCTION 3: Plot population growth for selected city
# ---------------------------------------------------------

def show_population_growth():
    conn = sqlite3.connect("population_AH.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    print("\nChoose a city to display population growth:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    choice = int(input("\nEnter the number of the city: "))
    selected_city = cities[choice - 1]

    cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (selected_city,))
    data = cursor.fetchall()

    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, pops, marker="o")
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    conn.close()


# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

def main():
    create_database()
    simulate_population()
    show_population_growth()

if __name__ == "__main__":
    main()
