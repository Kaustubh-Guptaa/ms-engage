# ms-engage
Microsoft Engage


----------------
MS_Final.ipynb
----------------

The Dataset is analyzed, model is generated and connected to Anvil's Web Application using Google Colaboratory.
Upload the MS_Final.ipynb notebook to the Google Colaboratory. Upload the Dataset to the notebook's directory and run the code.
Each code is documented under a text for better understanding on what's done.
Under 'Server Connection' there's a commented code - # pip install anvil-uplink, uncomment it if the code doesn't run further. After the installation:
  1. Restart Runtime
  2. Comment pip install anvil-uplink again.
  3. Re-run entire code again.
 
----------------
Dashboardwalkthrough
----------------

Application Link: https://P57AXF6NWFMKFXL4.anvil.app/2QNNDNL2Z2V5JWTGV7BNON7P
Anvil Link: https://anvil.works/login
      (Credential's provided in acehacker's submission)

Web Application source code is downloaded as a git repository. All the files are inside the Dashboardwalkthrough folder.

If there's an error in connecting to server:
  1. Log in to Anvil's website
  2. Go to 'My Apps' and select 'MS FINAL'
  3. Select 'App Browser' on Top Left
  4. Click on the ⚙ (Gear icon) below
  5. Select 'Uplink' 
  6. Click on 'Reset Uplink Key' and copy above code
  7. Open MS_Final.ipynb 
  8. Navigate down to 'Server Connection'
  9. Paste the copied code inside - anvil.server.connect(" ")  

----------------
cars_engage_2022_edited.csv
----------------

It is the edited dataset (originally: cars_engage_2022.csv) provided on the acehacker's website. NULL values are completed in the 'Make' column of the dataset.
If dataset is not accessible via GitHub, download from below link:

Drive: https://drive.google.com/file/d/1YOa7Ue5agZPHP695j4IkfvZwTdt5cB__/view?usp=sharing
