import openpyxl

# Load the Excel file
file_path = '../aggregated_output/LLM TEMP 0 MULTIPLE RUN SEED 791.xlsx'  # Replace with your file path
wb = openpyxl.load_workbook(file_path)
ws = wb.active  # Use the active worksheet

# Function to calculate LCS using the normalized formula
def lcs_length(s, t):
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def lcs(s, t):
    return lcs_length(s, t) / len(s) if len(s) > 0 else 0

# Optimized function to calculate LED using dynamic programming
def led(s, t):
    if len(s) < len(t):
        temp = s
        s = t
        t = temp
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n] / len(s) if len(s) > 0 else 0

# Process rows and calculate LCS and LED for each pair of strings
for row in ws.iter_rows(min_row=2):  # Adjust the row range as needed
    reference_string = row[6].value  # Column G (reference string)

    if reference_string:
        for idx, col in enumerate([7, 8, 9, 10]):  # Columns H, I, J, K
            compared_string = row[col].value
            if compared_string:
                lcs_value = lcs(reference_string, compared_string)
                led_value = led(reference_string, compared_string)
                
                # Write LCS and LED values to new columns (L, M, N, O, P, Q, R, S)
                row[11 + 2*idx].value = lcs_value  # LCS values in L, N, P, R
                row[12 + 2*idx].value = led_value  # LED values in M, O, Q, S

# Save the updated Excel file
output_file_path = 'updated_excel_with_lcs_led.xlsx'
wb.save(output_file_path)
