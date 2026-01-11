import re

def f(dates):
    date_list = dates.split(",")
    # Regex for YYYY-MM-DD
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    
    valid_dates = []
    for d in date_list:
        d = d.strip() # Clean whitespace if any
        if re.match(pattern, d):
            valid_dates.append(d)
            
    return valid_dates

if __name__ == "__main__":
    dates = "2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"
    print(f(dates)) # Expected: ["1998-12-11", "2001-12-07"]