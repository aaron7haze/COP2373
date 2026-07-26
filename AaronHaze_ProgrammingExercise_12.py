import numpy as np

# Load only numeric columns (Exam 1–3)
def load_csv(filename):
    # usecols selects columns 2, 3, 4 (0-based index)
    return np.loadtxt(filename, delimiter=",", skiprows=1, usecols=(2, 3, 4), dtype=int)

# Show first 5 rows
def preview_data(data):
    print("First 5 rows:")
    print(data[:5])
    print()

# Stats for each exam
def exam_statistics(data):
    num_exams = data.shape[1]
    for exam in range(num_exams):
        col = data[:, exam]
        print(f"Exam {exam + 1} Stats:")
        print(f"  Mean: {np.mean(col):.2f}")
        print(f"  Median: {np.median(col):.2f}")
        print(f"  Std Dev: {np.std(col):.2f}")
        print(f"  Min: {np.min(col)}")
        print(f"  Max: {np.max(col)}")
        print()

# Stats across all exams
def overall_statistics(data):
    flat = data.flatten()
    print("Overall Stats:")
    print(f"  Mean: {np.mean(flat):.2f}")
    print(f"  Median: {np.median(flat):.2f}")
    print(f"  Std Dev: {np.std(flat):.2f}")
    print(f"  Min: {np.min(flat)}")
    print(f"  Max: {np.max(flat)}")
    print()

# Pass/fail counts per exam
def pass_fail_counts(data):
    num_exams = data.shape[1]
    for exam in range(num_exams):
        col = data[:, exam]
        passes = np.sum(col >= 60)
        fails = np.sum(col < 60)
        print(f"Exam {exam + 1} Pass/Fail:")
        print(f"  Passed: {passes}")
        print(f"  Failed: {fails}")
        print()

# Overall pass percentage
def overall_pass_percentage(data):
    flat = data.flatten()
    passes = np.sum(flat >= 60)
    pct = (passes / len(flat)) * 100
    print("Overall Pass Percentage:")
    print(f"  {pct:.2f}%")
    print()

# Main program
def main():
    data = load_csv("grades.csv")

    print("Number of students:", data.shape[0])
    print()

    preview_data(data)
    exam_statistics(data)
    overall_statistics(data)
    pass_fail_counts(data)
    overall_pass_percentage(data)

# Run program
if __name__ == "__main__":
    main()
