import requests

def get_university_ranking(university_name):
    # استبدل 'YOUR_API_ENDPOINT' بعنوان الـ API الفعلي
    api_endpoint = 'YOUR_API_ENDPOINT'
    params = {
        'university': university_name
    }
    
    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        # استبدل 'ranking' بالمفتاح الصحيح في البيانات
        ranking = data.get('ranking', 'No ranking found')
        return ranking
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    university_name = input("Enter the name of the university: ")
    ranking = get_university_ranking(university_name)
    print(f"The ranking of {university_name} is: {ranking}")
