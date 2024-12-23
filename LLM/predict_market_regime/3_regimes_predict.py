import json
import os
from datetime import datetime, timedelta
import openai

# Initialize the OpenAI client
client = openai.OpenAI(api_key='your key')

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_market_regimes(file_path):
    regimes = {}
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                date, regime = line.split(', ')
                regimes[date] = regime
            except ValueError as e:
                print(f"Error on line {line_number}: {line}")
                print(f"Error message: {str(e)}")
                print("Skipping this line and continuing...")
    return regimes

def write_market_regime(file_path, date, regime):
    with open(file_path, 'a') as file:
        file.write(f"{date}, {regime}\n")

def format_news_input(news_data):
    formatted_news = []
    date = news_data['Date']
    for item in news_data['News']:
        formatted_news.append(f"Title: {item['news_title']}, Keyword: {item['keyword']}")
    return "\n".join(formatted_news)

def get_market_regime_prediction(news_input):
    prompt = f"""
    ### Role ###
    You are a highly knowledgeable and helpful finance economist specializing in the US equity market. You have access to relevant news for the day.

    ### Task ###
    Based on the provided news for the day, please label the market regime. The 3 market regimes are represented as "Negative", "Neutral", or "Positive".
    ### Input ###
    {news_input}

    ### Output ###
    Please provide your prediction as A SINGLE INTEGER: 0 (Negative), 1 (Neutral), 2 (Positive). NO EXPLANATION NEEDED.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model="gpt-4o-mini",
        temperature=0.1,
    )

    response = chat_completion.choices[0].message.content
    return response.strip()

# Main script/execution
start_date = datetime(2012, 1, 3)
end_date = datetime(2024, 7, 30)
current_date = start_date
folder_path = "/Users/elinazhuang/Desktop/wsj_2012to2024"
market_regimes_file = "/Users/elinazhuang/Desktop/3_market_regimes_daily.txt"

market_regimes = read_market_regimes(market_regimes_file)

while current_date <= end_date:
    file_name = f"reorg_wsj_{current_date.strftime('%Y-%m-%d')}.json"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        news_data = read_json_file(file_path)
        news_input = format_news_input(news_data)
        
        prediction = get_market_regime_prediction(news_input)
        write_market_regime(market_regimes_file, current_date.strftime('%Y-%m-%d'), prediction)
        market_regimes[current_date.strftime('%Y-%m-%d')] = prediction

        print(f"Date: {current_date.strftime('%Y-%m-%d')}")
        print(f"Predicted market regime: {prediction}")
        print("---")
    else:
        print(f"No news data found for {current_date.strftime('%Y-%m-%d')}. Skipping.")

    current_date += timedelta(days=1)

print("Market regime predictions completed.")
