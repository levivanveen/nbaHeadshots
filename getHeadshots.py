import os
import requests
from playerMapping import player_images

def download_headshots():
    # Create headshots directory if it doesn't exist
    output_dir = "headshots"
    os.makedirs(output_dir, exist_ok=True)
    
    for player, url in player_images.items():
        if player == "default":  # Skip the default placeholder
            continue
        
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Define file path
            file_name = f"{player.replace(' ', '_')}.png"
            file_path = os.path.join(output_dir, file_name)
            
            # Save image
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            
            print(f"Downloaded: {player}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {player}: {e}")

if __name__ == "__main__":
    download_headshots()
