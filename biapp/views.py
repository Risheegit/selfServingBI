from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_spark_session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def index(request):
    return render(request, 'index.html')

def display_results(request):
    # Retrieve data from session
    form_data = request.session.get('form_data', {})
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    channel = request.GET.get('channel')
    transaction_type = request.GET.get('transaction_type')
    customer_code = request.GET.get('customer_code')
    scheme_type = request.GET.get('scheme_type')

    data = [
            ('2023-01-01', '2023-01-02', 'merchant_payment', '123', 'scheme1', 'upi'),
            ('2023-01-03', '2023-01-04', 'ft_credit', '456', 'scheme2', 'ecs'),
            ('2023-01-05', '2023-01-06', 'td_creation', '789', 'scheme3', 'aeps'),
            ('2023-01-07', '2023-01-08', 'mf_investment', '012', 'scheme4', 'atm'),
            ('2023-01-09', '2023-01-10', 'insurance_payment', '234', 'scheme5', 'bna'),
            ('2023-01-11', '2023-01-12', 'cash_deposit', '567', 'scheme6', 'auto'),
            ('2023-01-13', '2023-01-14', 'cheque_debit', '890', 'scheme7', 'dig'),
            ('2023-01-15', '2023-01-16', 'surcharge_reversal', '135', 'scheme8', 'not_identified'),
            ('2023-01-17', '2023-01-18', 'ft_debit', '246', 'scheme9', 'brn'),
            ('2023-01-19', '2023-01-20', 'td_interest', '579', 'scheme10', 'ni'),
            ('2023-01-21', '2023-01-22', 'credit_adjustment', '802', 'scheme11', 'pos'),
            ('2023-01-23', '2023-01-24', 'cash_withdrawal_reversal', '135', 'scheme12', 'upi'),
            ('2023-01-25', '2023-01-26', 'auto_debit', '468', 'scheme13', 'ecs'),
            ('2023-01-27', '2023-01-28', 'surcharge', '791', 'scheme14', 'aeps'),
            ('2023-01-29', '2023-01-30', 'salary_credit', '024', 'scheme15', 'atm')
        ]

    data_dicts = [
        {'start_date': row[0], 'end_date': row[1], 'transaction_type': row[2], 'customer_code': row[3], 'scheme_type': row[4], 'channel': row[5]}
        for row in data
    ]

    # Apply filters only if values are not None and not empty
    if start_date:
        data_dicts = [item for item in data_dicts if item['start_date'] == start_date]
    if end_date:
        data_dicts = [item for item in data_dicts if item['end_date'] == end_date]
    if channel:
        data_dicts = [item for item in data_dicts if item['channel'].lower() == channel.lower()]
    if transaction_type:
        data_dicts = [item for item in data_dicts if item['transaction_type'].lower() == transaction_type.lower()]
    if customer_code:
        data_dicts = [item for item in data_dicts if item['customer_code'] == customer_code]
    if scheme_type:
        data_dicts = [item for item in data_dicts if item['scheme_type'].lower() == scheme_type.lower()]

    # Calculate percentages for different categories
    # category_counts = {}
    # total_count = len(data_dicts)
    # for item in data_dicts:
    #     category = item['channel']
    #     category_counts[category] = category_counts.get(category, 0) + 1

    # # Calculate percentages
    # percentages = {category: (count / total_count) * 100 for category, count in category_counts.items()}

    # # Create a pie chart
    # plt.figure(figsize=(8, 8))
    # plt.pie(percentages.values(), labels=percentages.keys(), autopct='%1.1f%%', startangle=140)
    # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    # plt.title('Distribution of Categories')

    # # Save the plot to a buffer
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # plot_data = base64.b64encode(buffer.read()).decode('utf-8')

    # Add the plot data to the context
    context = {
        'data': data_dicts,
        # 'plot_data': plot_data
    }

    # Continue with your view logic
    return render(request, 'results.html', context)
