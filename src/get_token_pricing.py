import requests
from bs4 import BeautifulSoup
import datetime

def get_aws_price():
    # URL of the AWS Bedrock pricing page
    url = 'https://aws.amazon.com/bedrock/pricing/'

    # Send a request to fetch the HTML content of the page
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize HTML table with headers
    html_table = """
    <h1>AWS Bedrock Pricing</h1>

    <table>
        <thead>
            <tr>
                <th>Model</th>
                <th>Resolution</th>
                <th>Standard Price</th>
                <th>Premium Price</th>
            </tr>
        </thead>
        <tbody>
    """

    # Locate the table rows containing the pricing information
    # This might need adjustment based on the actual structure of the page
    # Replace 'table' and 'tr' selectors with the appropriate ones for the AWS Bedrock pricing page
    pricing_rows = soup.select('table tbody tr')

    for row in pricing_rows:
        cells = row.find_all('td')
        if len(cells) >= 4:  # Assuming each row has at least four cells: Model, Resolution, Standard Price, Premium Price
            model = cells[0].get_text(strip=True)
            resolution = cells[1].get_text(strip=True)
            standard_price = cells[2].get_text(strip=True)
            premium_price = cells[3].get_text(strip=True)
            
            # Append the data to the HTML table
            html_table += f"""
            <tr>
                <td>{model}</td>
                <td>{resolution}</td>
                <td>{standard_price}</td>
                <td>{premium_price}</td>
            </tr>
            """

    html_table += """
        </tbody>
    </table>
    """

    # Output to an HTML file
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"index.html"

    with open(filename, 'w') as file:
        file.write(html_table)

    print(f"HTML table saved to {filename}")

get_aws_price()