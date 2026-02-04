import datetime
from typing import List, Dict, Any
from collections import defaultdict
import unittest

def parse_date(date_str: str) -> datetime.date:
    """Parse a date string in YYYY-MM-DD format to a date object."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

def get_month_range(target_month: str) -> (datetime.date, datetime.date):
    """Get the first and last day of the target month."""
    year, month = map(int, target_month.split('-'))
    first_day = datetime.date(year, month, 1)
    
    if month == 12:
        last_day = datetime.date(year, month, 31)
    else:
        last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    return first_day, last_day

def calculate_active_days(item_start: str, item_end: str, month_start: datetime.date, month_end: datetime.date) -> int:
    """Calculate how many days in the month the item was active."""
    start_date = parse_date(item_start)
    end_date = parse_date(item_end)
    
    # Adjust dates to be within the month range
    active_start = max(start_date, month_start)
    active_end = min(end_date, month_end)
    
    if active_start > active_end:
        return 0
    
    return (active_end - active_start).days + 1

def calculate_monthly_amount(rate: float, qty: int, active_days: int, month_days: int) -> float:
    """Calculate the prorated amount for the active days in the month."""
    daily_rate = (rate * qty) / month_days
    return round(daily_rate * active_days, 2)

def process_item(item: Dict[str, Any], month_start: datetime.date, month_end: datetime.date) -> Dict[str, Any]:
    """Process an individual item to calculate its active days and amount."""
    # Convert fields to appropriate types
    rate = float(item['rate']) if isinstance(item['rate'], str) else item['rate']
    qty = int(item['qty']) if isinstance(item['qty'], str) else item['qty']
    
    # Calculate active days in the target month
    active_days = calculate_active_days(item['start_date'], item['stop_date'], month_start, month_end)
    
    if active_days == 0:
        return None
    
    # Calculate the amount for the active period
    month_days = (month_end - month_start).days + 1
    amount = calculate_monthly_amount(rate, qty, active_days, month_days)
    
    # Determine the billing period
    active_start = max(parse_date(item['start_date']), month_start)
    active_end = min(parse_date(item['stop_date']), month_end)
    billing_period = f"{active_start.strftime('%Y-%m-%d')} to {active_end.strftime('%Y-%m-%d')}"
    
    return {
        'item_code': item['item_code'],
        'rate': rate,
        'qty': qty,
        'amount': amount,
        'billing_period': billing_period,
        'active_days': active_days,
        'month_days': month_days
    }

def generate_monthly_bill(item_list: List[Dict[str, Any]], target_month: str) -> Dict[str, Any]:
    """
    Generates a bill for the given month based on the item list.
    
    Parameters:
        item_list (list): List of dictionaries with item details.
        target_month (str): Month in "YYYY-MM" format (e.g., "2024-11").
    
    Returns:
        dict: A dictionary with grouped line items and total revenue.
    """
    # Get the month range
    month_start, month_end = get_month_range(target_month)
    month_days = (month_end - month_start).days + 1
    
    # Process all items to find active ones in the target month
    processed_items = []
    for item in item_list:
        processed_item = process_item(item, month_start, month_end)
        if processed_item:
            processed_items.append(processed_item)
    
    # Group items by item_code, rate, and billing_period
    groups = defaultdict(list)
    for item in processed_items:
        key = (item['item_code'], item['rate'], item['billing_period'])
        groups[key].append(item)
    
    # Create line items by summing quantities in each group
    line_items = []
    for key, items in groups.items():
        total_qty = sum(item['qty'] for item in items)
        # All items in group have same rate, billing_period, and amount per qty
        representative = items[0]
        line_item = {
            'item_code': representative['item_code'],
            'rate': representative['rate'],
            'qty': total_qty,
            'amount': round(representative['amount'] / representative['qty'] * total_qty, 2),
            'billing_period': representative['billing_period']
        }
        line_items.append(line_item)
    
    # Calculate total revenue
    total_revenue = round(sum(item['amount'] for item in line_items), 2)
    
    return {
        'line_items': line_items,
        'total_revenue': total_revenue
    }

class TestMonthlyBillGenerator(unittest.TestCase):
    def setUp(self):
        self.item_list = [
            {
                "idx": 1,
                "item_code": "Executive Desk (4*2)",
                "sales_description": "Dedicated Executive Desk",
                "qty": 10,
                "rate": "1000",
                "amount": "10000",
                "start_date": "2023-11-01",
                "stop_date": "2024-10-17",
            },
            {
                "idx": 2,
                "item_code": "Executive Desk (4*2)",
                "qty": "10",
                "rate": "1080",
                "amount": "10800",
                "start_date": "2024-10-18",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 3,
                "item_code": "Executive Desk (4*2)",
                "qty": 15,
                "rate": "1080",
                "amount": "16200",
                "start_date": "2024-11-01",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 4,
                "item_code": "Executive Desk (4*2)",
                "qty": 5,
                "rate": "1000",
                "amount": "5000",
                "start_date": "2024-11-01",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 5,
                "item_code": "Manager Cabin",
                "qty": 5,
                "rate": 5000,
                "amount": 25000,
                "start_date": "2024-11-01",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 6,
                "item_code": "Manager Cabin",
                "qty": 7,
                "rate": "5000",
                "amount": 35000,
                "start_date": "2024-12-15",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 7,
                "item_code": "Manager Cabin",
                "qty": 10,
                "rate": 4600,
                "amount": 46000,
                "start_date": "2023-11-01",
                "stop_date": "2024-10-17",
            },
            {
                "idx": 8,
                "item_code": "Parking (2S)",
                "qty": 10,
                "rate": 1000,
                "amount": 10000,
                "start_date": "2024-11-01",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 9,
                "item_code": "Parking (2S)",
                "qty": 10,
                "rate": 0,
                "amount": 0,
                "start_date": "2024-11-01",
                "stop_date": "2025-10-31",
            },
            {
                "idx": 10,
                "item_code": "Executive Desk (4*2)",
                "qty": "8",
                "rate": "1100",
                "amount": "8800",
                "start_date": "2024-11-15",
                "stop_date": "2025-01-31",
            },
            {
                "idx": 11,
                "item_code": "Manager Cabin",
                "qty": "3",
                "rate": "5200",
                "amount": "15600",
                "start_date": "2024-10-10",
                "stop_date": "2024-11-10",
            },
            {
                "idx": 12,
                "item_code": "Conference Table",
                "qty": 1,
                "rate": "20000",
                "amount": "20000",
                "start_date": "2024-11-05",
                "stop_date": "2024-11-20",
            },
            {
                "idx": 13,
                "item_code": "Parking (2S)",
                "qty": 5,
                "rate": "1000",
                "amount": "5000",
                "start_date": "2024-11-15",
                "stop_date": "2025-02-28",
            },
            {
                "idx": 14,
                "item_code": "Reception Desk",
                "qty": 2,
                "rate": "7000",
                "amount": "14000",
                "start_date": "2024-11-01",
                "stop_date": "2025-03-31",
            },
            {
                "idx": 15,
                "item_code": "Reception Desk",
                "qty": 1,
                "rate": "7000",
                "amount": "7000",
                "start_date": "2024-11-10",
                "stop_date": "2024-11-25",
            },
            {
                "idx": 16,
                "item_code": "Breakout Area",
                "qty": 3,
                "rate": "3000",
                "amount": "9000",
                "start_date": "2024-01-01",
                "stop_date": "2024-01-31",
            }
        ]

    def test_generate_monthly_bill_november_2024(self):
        """Test the main functionality with November 2024 data"""
        result = generate_monthly_bill(self.item_list, "2024-11")
        
        # Verify the structure of the response
        self.assertIn("line_items", result)
        self.assertIn("total_revenue", result)
        self.assertIsInstance(result["line_items"], list)
        self.assertIsInstance(result["total_revenue"], float)
        
        # Verify some specific line items
        executive_desk_items = [item for item in result["line_items"] 
                               if item["item_code"] == "Executive Desk (4*2)"]
        self.assertEqual(len(executive_desk_items), 3)  # Should have 3 groups
        
        # Check one specific item
        parking_items = [item for item in result["line_items"] 
                        if item["item_code"] == "Parking (2S)" and item["rate"] == 1000]
        self.assertEqual(len(parking_items), 2)  # Two groups (full month and partial month)
        
        # Check the zero-rate item is included but with zero amount
        zero_rate_items = [item for item in result["line_items"] 
                         if item["rate"] == 0]
        self.assertEqual(len(zero_rate_items), 1)
        self.assertEqual(zero_rate_items[0]["amount"], 0)
        
        # Check total revenue is reasonable
        self.assertGreater(result["total_revenue"], 0)

    def test_active_days_calculation(self):
        """Test the active days calculation for different scenarios"""
        month_start, month_end = get_month_range("2024-11")
        
        # Item active the entire month
        days = calculate_active_days("2024-11-01", "2024-11-30", month_start, month_end)
        self.assertEqual(days, 30)
        
        # Item active for first half of month
        days = calculate_active_days("2024-11-01", "2024-11-15", month_start, month_end)
        self.assertEqual(days, 15)
        
        # Item active for last half of month
        days = calculate_active_days("2024-11-16", "2024-12-15", month_start, month_end)
        self.assertEqual(days, 15)
        
        # Item active for middle of month
        days = calculate_active_days("2024-11-10", "2024-11-20", month_start, month_end)
        self.assertEqual(days, 11)
        
        # Item not active in month
        days = calculate_active_days("2024-10-01", "2024-10-31", month_start, month_end)
        self.assertEqual(days, 0)
        
        # Item spanning multiple months
        days = calculate_active_days("2024-10-15", "2025-01-15", month_start, month_end)
        self.assertEqual(days, 30)

    def test_month_range_calculation(self):
        """Test the month range calculation"""
        # Regular month
        start, end = get_month_range("2024-11")
        self.assertEqual(start, datetime.date(2024, 11, 1))
        self.assertEqual(end, datetime.date(2024, 11, 30))
        
        # February in leap year
        start, end = get_month_range("2024-02")
        self.assertEqual(start, datetime.date(2024, 2, 1))
        self.assertEqual(end, datetime.date(2024, 2, 29))
        
        # December
        start, end = get_month_range("2024-12")
        self.assertEqual(start, datetime.date(2024, 12, 1))
        self.assertEqual(end, datetime.date(2024, 12, 31))

    def test_empty_month(self):
        """Test with a month where no items are active"""
        result = generate_monthly_bill(self.item_list, "2023-01")
        self.assertEqual(len(result["line_items"]), 0)
        self.assertEqual(result["total_revenue"], 0)

    def test_type_conversion(self):
        """Test that string and numeric values are handled correctly"""
        item = {
            "idx": 99,
            "item_code": "Test Item",
            "qty": "5",  # String quantity
            "rate": "100.50",  # String rate
            "amount": "502.50",  # String amount (should be recalculated)
            "start_date": "2024-11-01",
            "stop_date": "2024-11-30"
        }
        month_start, month_end = get_month_range("2024-11")
        processed = process_item(item, month_start, month_end)
        
        self.assertEqual(processed["qty"], 5)
        self.assertEqual(processed["rate"], 100.50)
        self.assertEqual(processed["amount"], 502.5)  # 5 * 100.50 * 30 / 30

if __name__ == "__main__":
    # Run the tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Example usage with the provided data
    print("\nExample Bill Generation for November 2024:")
    test_case = TestMonthlyBillGenerator()
    test_case.setUp()  # This initializes the item_list
    bill = generate_monthly_bill(test_case.item_list, "2024-11")
    print(bill)