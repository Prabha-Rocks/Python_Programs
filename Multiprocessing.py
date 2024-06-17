import concurrent.futures
import requests
import os

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    os.makedirs('files', exist_ok=True)  # Ensure the directory exists
    file_path = os.path.join('files', f'file{name}.jpg')
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")
    return f"Downloaded {name}"

url = "https://picsum.photos/2000/3000"

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for _ in range(60)]
        l2 = list(range(60))
        results = executor.map(downloadFile, l1, l2)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
