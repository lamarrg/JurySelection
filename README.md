# JurySelection
Data aggregation for potential jurors

This was a project that started off being a potential side job that never came to fruition. 

The theoretical client has a business where they keep data on potential jurors. It was previously created using excel and would print out to 3x5 cards. She stated that it was no longer working and I assumed the failure came with all the software updates over time.

I wanted to build something that would be less likely to suffer the same fate, so I decided to do it in Python using Flask.

Here are some of the parameters I was able to get, and some decisions I made...
  * locally used (no login required as it was used by a single person from their laptop)
  * made it a web app so it is is easy to navigate and enter data
  * used sqlite3 as I did not want them to have to worry about installing and maintaining any external software
  * create 3x5 pdfs to print the data, and to be able to look at it locally 

For as simple as it is, there is still a laundry list of things I want to do to it to make it more user friendly. (laundry list coming soon)

Starting the laundry list...
    * delete functionality - deleting a trial will also delete a the folder and cards in it.
    * create proper testing