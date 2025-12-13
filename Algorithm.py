# Algorithm.py
# Max Profit Optimization Problem

def max_profit(n):
    theatres = n // 5
    remaining = n % 5
    pubs = 1 if remaining >= 4 else 0

    earnings = theatres * 1500 + pubs * 1000

    return {
        "T": theatres,
        "P": pubs,
        "C": 0,
        "Earnings": earnings
    }


if __name__ == "__main__":
    n = int(input("Enter time units: "))

    result = max_profit(n)

    print(f"T: {result['T']} P: {result['P']} C: {result['C']}")
    print(f"Total Earnings: ${result['Earnings']}")
