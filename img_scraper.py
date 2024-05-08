def img_downloader(url):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_url = soup.find(class_='mh-monster-header').img['src']

    # Check if the URL is relative and prepend with the base URL if necessary
    if not img_url.startswith('http'):
        base_url = 'https://mhrise.mhrice.info/'
        img_url = urljoin(base_url, img_url)

    # Get the image content
    img_data = requests.get(img_url).content

    # Create a folder named "imgs" if it doesn't exist
    folder = 'imgs'
    os.makedirs(folder, exist_ok=True)

    # Save the image in the "imgs" folder with the same name as in the URL
    img_filename = os.path.basename(img_url)
    img_path = os.path.join(folder, img_filename[2:])
    with open(img_path, 'wb') as img_file:
        img_file.write(img_data)

    return f"Image saved to {img_path}"


link_list= [
  "https://mhrise.mhrice.info/monster/001_00.html",
  "https://mhrise.mhrice.info/monster/001_02.html",
  "https://mhrise.mhrice.info/monster/001_07.html",
  "https://mhrise.mhrice.info/monster/002_00.html",
  "https://mhrise.mhrice.info/monster/002_02.html",
  "https://mhrise.mhrice.info/monster/002_07.html",
  "https://mhrise.mhrice.info/monster/003_00.html",
  "https://mhrise.mhrice.info/monster/004_00.html",
  "https://mhrise.mhrice.info/monster/007_00.html",
  "https://mhrise.mhrice.info/monster/007_07.html",
  "https://mhrise.mhrice.info/monster/019_00.html",
  "https://mhrise.mhrice.info/monster/020_00.html",
  "https://mhrise.mhrice.info/monster/023_00.html",
  "https://mhrise.mhrice.info/monster/023_05.html",
  "https://mhrise.mhrice.info/monster/024_00.html",
  "https://mhrise.mhrice.info/monster/024_08.html",
  "https://mhrise.mhrice.info/monster/025_00.html",
  "https://mhrise.mhrice.info/monster/025_08.html",
  "https://mhrise.mhrice.info/monster/027_00.html",
  "https://mhrise.mhrice.info/monster/027_08.html",
  "https://mhrise.mhrice.info/monster/032_00.html",
  "https://mhrise.mhrice.info/monster/037_00.html",
  "https://mhrise.mhrice.info/monster/037_02.html",
  "https://mhrise.mhrice.info/monster/042_00.html",
  "https://mhrise.mhrice.info/monster/044_00.html",
  "https://mhrise.mhrice.info/monster/047_00.html",
  "https://mhrise.mhrice.info/monster/054_00.html",
  "https://mhrise.mhrice.info/monster/057_00.html",
  "https://mhrise.mhrice.info/monster/057_07.html",
  "https://mhrise.mhrice.info/monster/058_00.html",
  "https://mhrise.mhrice.info/monster/059_00.html",
  "https://mhrise.mhrice.info/monster/060_00.html",
  "https://mhrise.mhrice.info/monster/060_07.html",
  "https://mhrise.mhrice.info/monster/061_00.html",
  "https://mhrise.mhrice.info/monster/062_00.html",
  "https://mhrise.mhrice.info/monster/071_00.html",
  "https://mhrise.mhrice.info/monster/071_05.html",
  "https://mhrise.mhrice.info/monster/072_00.html",
  "https://mhrise.mhrice.info/monster/072_08.html",
  "https://mhrise.mhrice.info/monster/077_00.html",
  "https://mhrise.mhrice.info/monster/081_00.html",
  "https://mhrise.mhrice.info/monster/082_00.html",
  "https://mhrise.mhrice.info/monster/082_02.html",
  "https://mhrise.mhrice.info/monster/082_07.html",
  "https://mhrise.mhrice.info/monster/086_05.html",
  "https://mhrise.mhrice.info/monster/086_08.html",
  "https://mhrise.mhrice.info/monster/089_00.html",
  "https://mhrise.mhrice.info/monster/089_05.html",
  "https://mhrise.mhrice.info/monster/090_00.html",
  "https://mhrise.mhrice.info/monster/090_01.html",
  "https://mhrise.mhrice.info/monster/091_00.html",
  "https://mhrise.mhrice.info/monster/092_00.html",
  "https://mhrise.mhrice.info/monster/093_00.html",
  "https://mhrise.mhrice.info/monster/093_01.html",
  "https://mhrise.mhrice.info/monster/094_00.html",
  "https://mhrise.mhrice.info/monster/094_01.html",
  "https://mhrise.mhrice.info/monster/095_00.html",
  "https://mhrise.mhrice.info/monster/095_01.html",
  "https://mhrise.mhrice.info/monster/096_00.html",
  "https://mhrise.mhrice.info/monster/097_00.html",
  "https://mhrise.mhrice.info/monster/098_00.html",
  "https://mhrise.mhrice.info/monster/099_00.html",
  "https://mhrise.mhrice.info/monster/099_05.html",
  "https://mhrise.mhrice.info/monster/100_00.html",
  "https://mhrise.mhrice.info/monster/102_00.html",
  "https://mhrise.mhrice.info/monster/107_00.html",
  "https://mhrise.mhrice.info/monster/108_00.html",
  "https://mhrise.mhrice.info/monster/109_00.html",
  "https://mhrise.mhrice.info/monster/118_00.html",
  "https://mhrise.mhrice.info/monster/118_05.html",
  "https://mhrise.mhrice.info/monster/124_00.html",
  #"https://mhrise.mhrice.info/monster/131_00.html",
  "https://mhrise.mhrice.info/monster/132_00.html",
  "https://mhrise.mhrice.info/monster/132_05.html",
  "https://mhrise.mhrice.info/monster/133_00.html",
  "https://mhrise.mhrice.info/monster/134_00.html",
  "https://mhrise.mhrice.info/monster/135_00.html",
  "https://mhrise.mhrice.info/monster/136_00.html",
  "https://mhrise.mhrice.info/monster/136_01.html"
]



import os

def img_renamer(new_names):    
    folder = 'imgs'

    # Check if the 'imgs' folder exists
    if os.path.exists(folder) and os.path.isdir(folder):
        # List all files in the 'imgs' folder
        files = os.listdir(folder)

        # Check if the number of new names matches the number of files
        if len(new_names) != len(files):
            print("Number of new names does not match the number of files.")
        else:
            # Rename each file
            for old_name, new_name in zip(files, new_names):
                old_path = os.path.join(folder, old_name)
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{old_name}' to '{new_name}'.")
    else:
        print(f"Folder '{folder}' does not exist.")


import os

def rename_files(directory):
    # Get absolute path of the directory
    directory = os.path.abspath(directory)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Iterate over each file
    for filename in files:
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Rename file by replacing spaces with underscores
            new_filename = filename.replace(' ', '_')
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            
            print(f"Renamed '{filename}' to '{new_filename}'")

# Directory containing the files to be renamed
directory = 'templates/imgs'

# Call the function to rename files
rename_files(directory)
# Example usage:
#new_names = ['Rathian.png', 'Gold Rathian.png', 'Apex Rathian.png', 'Rathalos.png', 'Silver Rathalos.png', 'Apex Rathalos.png', 'Khezu.png', 'Basarios.png', 'Diablos.png', 'Apex Diablos.png', 'Daimyo Hermitaur.png', 'Shogun Ceanataur.png', 'Rajang.png', 'Furious Rajang.png', 'Kushala Daora.png', 'Risen Kushala Daora.png', 'Chameleos.png', 'Risen Chameleos.png', 'Teostra.png', 'Risen Teostra.png', 'Tigrex.png', 'Nargacuga.png', 'Lucent Nargacuga.png', 'Barioth.png', 'Barroth.png', 'Royal Ludroth.png', 'Great Baggi.png', 'Zinogre.png', 'Apex Zinogre.png', 'Amatsu.png', 'Great Wroggi.png', 'Arzuros.png', 'Apex Arzuros.png', 'Lagombi.png', 'Volvidon.png', 'Gore Magala.png', 'Chaotic Gore Magala.png', 'Shagaru Magala.png', 'Risen Shagaru Magala.png', 'Seregios.png', 'Astalos.png', 'Mizutsune.png', 'Violet Mizutsune.png', 'Apex Mizutsune.png', 'Crimson Glow Valstrax.png', 'Risen Crimson Glow Valstrax.png', 'Magnamalo.png', 'Scorned Magnamalo.png', 'Bishaten.png', 'Blood Orange Bishaten.png', 'Aknosom.png', 'Tetranadon.png', 'Somnacanth.png', 'Aurora Somnacanth.png', 'Rakna-Kadaki.png', 'Pyre Rakna-Kadaki.png', 'Almudron.png', 'Magma Almudron.png', 'Wind Serpent Ibushi.png', 'Goss Harag.png', 'Great Izuchi.png', 'Thunder Serpent Narwa.png', 'Narwa the Allmother.png', 'Anjanath.png', 'Pukei-Pukei.png', 'Kulu-Ya-Ku.png', 'Jyuratodus.png', 'Tobi-Kadachi.png', 'Bazelgeuse.png', 'Seething Bazelgeuse.png', 'Velkhana.png', 'Malzeno.png', 'Primordial Malzeno.png', 'Lunagaron.png', 'Garangolm.png', 'Gaismagorm.png', 'Espinas.png', 'Flaming Espinas.png']  # Replace with your list of new names

