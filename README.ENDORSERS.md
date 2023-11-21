# Updating list of endorers

1. Go to https://indico.cern.ch/event/1293733/manage/registration/95224/registrations/
2. Make sure the 'right' Affiliation is selected in the "Customise list" 
3. Select 'All' items (use the checkbox on the top) and then export > CSV
4. Clone this repository and save the CSV file (`registrations.csv`) in the checkout folder
5. Run `_python/build_endorsers.py registrations.csv`
6. Commit the changes to `Endorsers.html` and `Endorsers_insert.html`
7. Push the changes
8. The site will be deployed soon after

