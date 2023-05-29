def english_miles_to_roman(miles):
    return round(miles * 1000 * 5280 / 4854)
    
def main():
    miles = float(input())
    print(english_miles_to_roman(miles=miles))
    
    
if __name__ == "__main__":
    main()