# CODE VERDICT - an Online Judge

*From the very first year, when I embarked on my journey in Competitive Programming (CP), I came across many remarkable platforms like CodeForces and Codechef. I always wondered about the internal working of those platforms. 
Although, the primary objective is not to entirely replicate all the features but to create a product that delivers value to the user through a judicious selection of essential features. It is a go-to-use product in software domain as I look from my perspective.*

So here, I present Code Verdict, an Online Judge using Django from scratch. Django being a high-level, open-source web framework in Python, is simple and easy to learn. It has a built-in admin panel and authorization system. It follows the ***Don’t Repeat Yourself (DRY)*** principle, hence reducing redundancy. 
I tried my best to follow DRY principle. It is commonly used by many famous companies such as ***Instagram, Youtube and Spotify***. 

The final product aims to allow users to submit their code in multiple programming languages, execute it and generate a verdict in real-time environment. The system will be constructed with a focus on ensuring robust security and scalability.

<img src="https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/47a48902-a934-4d71-af8f-fb20c1c60364" width="100" height="100">

**LET'S  DIG  IN  WITHOUT  FURTHER  ADO !!**
___
Now, a common misconception arises and people equate an Online Judge with an Online Compiler. In layman terms, Online Compiler is a subset of Online Judge.

Here is the basic difference between them : 
### **Online Judge**
> It is a platform where a user submits their code and receives a verdict based on the judgement system. Here, Input is provided in form of predefined test cases and compared with the corresponding predefined Output. 
> It is commonly used for competitive programming, coding contests, and practicing problems for DSA.
>> Example - CodeForces, Codechef

### **Online Compiler**
> It is a tool that allows users to write, compile, and execute code online without any local compiler in their system. It is mainly used for quick code testing, debugging, and experimentation.
> Here, no verdict is passed by the system, rather only output is generated. Also, providing Input may or may not be necessary.
>> Example - OnlineGDB, Programiz
<br>

## ✨ Key Features
- Multi-language support: `C++` `Java` `Python` `C-Programming`
- User registration and login page (Authentication)
- Permissions assigned based on roles (Authorization)
- Only ***Employee*** can perform CRUD operations after verification
- Problem statements with difficulty assigned
- Custom Input feature
- Supports TLE and Runtime Error
- Can access past submissions in profile
- Can copy submitted codes in past submissions
- View common stats in profile section
- Code-editor supports both HTML and Markdown language
- Support syntax highlighting and line numbers
- Shortcut keys support - `Tab` `Shift + Tab` `Enter`
- Leaderboard to see your global standings
- Security with custom compiler and Docker for isolation

<br>

# How to start using Code-Verdict 🤔
Well, I will be dicussing mainly 2 ways on how to use this online judge on your local machine.


## Using Docker
***Pre-requisites***
<ol>
  <li>Docker account with Docker Desktop in local machine</li>
  <li>VS Code or any code-editor</li>
</ol>

***Steps To Follow***
- Firstly, **Clone** this repository to your local machine.
  - Open a folder (recommended to create a new folder) in VS Code
  - Now, let's create a virtual environment inside this folder
      ```python
      python -m venv myenv
      ```
    Replace **'myenv'** with any desired name you want
  - Now, run this command inside your terminal:
    ```bash
    git clone https://github.com/Devankar-iitP/Code_Verdict.git
    ```
    
- Great, now let's get inside the Code_Verdict folder in your current directory
  ```bash
  cd code_Verdict
  ```
  
- Install all the requirements needed. Don't worry, it's quite simple  ^_^
  ```python
  pip install -r requirements.txt
  ```
  
- Let's create our docker container now...
  ```docker
  docker-compose up -d
  ```
  
- After the download is completed, head over to the Docker Desktop application inside your local machine
  - Press Windows key and type **"Docker Desktop"** in search bar to open
 
- You will observe something like this inside the app
  ![image](https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/6e0a4008-5b16-479b-b41d-753d5bd02aae)
  In Images section, you will observe there are 2 images created named postgres which is our database and code_verdict-web which contains whole django app.

  
  - If your container appears to be orange like below
    ![image](https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/b089a09d-d491-4808-85bc-26c3b15c8e0e)
    
    Follow the instructions mentioned below step-wise :
    - Click on "code_verdict" written near the orange icon
    - Stop both the containers using ■ icon on right. After stopping, both should look like below :
      <img src="https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/d32068c4-ccee-458a-9833-06a57ece3c59" width="300" height="200">
    - Now, start only the postgres_db using ▶ icon on right
      ![image](https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/dd61cdf7-5ee5-4e11-b460-a5d697415bc2)
    - When you see the following line in logs section : "database system is ready to accept connections", now your database is ready.
    - Start the django_container using ▶ icon on right
    - If you get same message as below, then your containers are in sync and working
      ![image](https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/049acf5f-a7e3-4dbc-b091-5cd0c6a5c0a3)
      If not, then again perform these debugging instructions from start at an interval of 10 seconds


- If your container is green then you are good to go now.
- <img src="https://github.com/Devankar-iitP/Code_Verdict/assets/118092124/23b0db91-0872-4071-98af-5fbeb39f53bb" width="300" height="200">
- Click on highlighted link
- Congratulations !! Now, you are part of Code_Verdict team.
  HAPPY CODING 😀

<br>

***Key Notes***
- Admin is already created with username = "root" & password = "admin"
  - If you want your own custom superuser
    ```python
    python manage.py create superuser
    ```
    Set the username & password accordingly
- All data is stored in data folder
- If you want to be employee, then give permission from admin for approval
- ***This system is NOT connected to main SERVER. It's like a virtual playground for your own experiments.***

<br>

## Using EC2 instance on AWS

***Pre-requisites*** - Frankly speaking, you have to only click on the below link

<a href="https://code-verdict.me/">Code-Verdict</a>

***Note - Since, I am a student and using free-tier on AWS account. This link only works if my instance is running on AWS. So, be careful !!***

<br>

## Contributions
We welcome anyone who wants to make contributions from the community to enhance this Online Judge Platform. If you have ideas for new features, improvements, or bug fixes, follow these steps to contribute :

1. Fork the Repository: Click the 'Fork' button at the top right of this repository to create your own copy.
2. Clone the Forked Repository: Clone your forked repository to your local machine using
```git
git clone https://github.com/Devankar-iitP/Code_Verdict.git
```
3. Now, create a new branch for development
```git
git checkout -b branch_name
```
4. Implement your changes in the codebase, whatever you think fits the best.
5. Stage those changes
```git
git add .
``` 
6. Commit your changes with a clear commit message
```git
git commit -m "Add feature: your feature name"
```
7. Push the changes to your forked repository
```git
git push origin feature/your-feature-name
```
8. Finally, make a pull request
   - Head on over to the repository on GitHub where your project lives `https://github.com/<your_username>/Code_Verdict`
   - You'll see a banner indicating that your branch is one commit ahead of main.
   - Click on Contribute and then Open a pull request.
   - Click Create pull request.
   - Enter the title and description of your changes.

#### Before contributing, please ensure that your changes follow the project's coding standards and guidelines.
#### Thank you for your interest in contributing to Code Verdict ! 

<br>

## LICENSE
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
