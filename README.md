# Find unused files in web-development projects
A simple resource I created to find unused files in a larger web-development project I was working on. I made this open source to show part of my development process and as a resource to give to beginner web-developers.

## Running the code
Place main.py inside the directory that you want to search. Then run:

    python3 main.py

Thats all! The output should look something like this:

<img width="456" alt="Screenshot 2023-07-17 at 3 58 10 PM" src="https://github.com/zroe1/findUnusedFilesHTML/assets/114773939/7e86abbd-87c9-4f6c-89b1-98c9f04f3068">

## How it works
The code searchs recursively through the directories main.py is placed in. If you are currently in a folder with a folder, that also contains several folders, the code will search all of them.

The code only looks for files ending in '.jpg', '.jpeg', '.png', '.html', '.css', '.js', '.pdf', or 'ico'. It only reads and searchs for references to other files if the file ends in '.html', '.css', or '.js'. It also ignores git directories. This is because I designed this program for simple web-development (using only HTML, CSS, and JavaScript), but the code can be manually changed for other purposes.
