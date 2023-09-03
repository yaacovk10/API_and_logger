import http.client

def search_linkedin():
    conn = http.client.HTTPSConnection("linkedin-profiles1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "50b7198a71msha0f963578a476d3p143814jsn9c7d6298f6b8",
        'X-RapidAPI-Host': "linkedin-profiles1.p.rapidapi.com"
    }

    while True:
        # Ask the user if they want to search for a person or a company
        search_type = input("Enter 'person' to search for a person or 'company' to search for a company, or 'exit' to quit: ").lower()

        if search_type == 'exit':
            return
        elif search_type == 'person':
            # If the user wants to search for a person, ask for first name and last name
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            query = f"{first_name}%20{last_name}"
        elif search_type == 'company':
            # If the user wants to search for a company, ask for the company name
            company_name = input("Enter the company name: ")
            query = company_name
        else:
            print("Invalid search type. Please enter 'person', 'company', or 'exit'.")
            continue

        # Make the API request with the appropriate query and search type
        conn.request("GET", f"/search?query={query}&type={search_type}", headers=headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # Parse the JSON response
        try:
            import json
            result = json.loads(data)
            profiles = result.get("data", [])

            if len(profiles) == 0:
                print("No matching profiles found.")
                continue

            profile = profiles[0]  # Assume the first result is the one we want

            while True:
                # Ask the user what they want to view or exit
                choice = input("Enter 'description' to see the description, 'url' to see the LinkedIn profile URL, or 'exit' to go back: ").lower()

                if choice == 'exit':
                    return
                elif choice == 'description':
                    description = profile.get("snippet", "")
                    print(description)
                elif choice == 'url':
                    url = profile.get("url", "")
                    print(f'<a href="{url}">{url}</a>')
                else:
                    print("Invalid choice. Please enter 'description', 'url', or 'exit'.")

        except json.JSONDecodeError:
            print("Error parsing JSON response.")
            continue

if __name__ == "__main__":
    search_linkedin()
