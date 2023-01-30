# YelpQueryMaster Description

**Catalog**
- [Abstract](#Abstract)
- [Core Feactures](#Core-Feactures)
- [Technologies Used](#Technologies-Used)
- [Software Architecture](#Software-Architecture)
- [Setup Instructions](#Setup-Instructions)
- [Demo](#Demo)

**Developers:** `Xinyu Liu, Boxiang Lin, Xinru Li, Tianhao Huang`

**Date Revised:** `01/30/2022`

**Revised By:** `Boxiang Lin`

---

### Abstract
YelpQueryMaster is a comprehensive desktop solution that empowers users to effortlessly discover and evaluate dining establishments. With its advanced filtering options, including location, price range, and meal category, users can find the perfect restaurant to suit their needs. In addition, it provides insightful feedback issued by customers and straightforward histograms that shows the historical check-ins.


### Core Feactures
Below are the list of core features of YelpQueryMaster
- User login to the portal.
- Edit user profile information
- Visualize a list of user’s friends
- Visualize the latest tips (comments) made friends
- Search for restaurants by filters, filters including search by location, business category, attributes, and price range
- Show restaurant information, such as name, rating, operating hours, address, numbers of check in, and comments of the restaurant
- Visualize the historical checkins by histograms
- Check In to the restaurant
- Add tips to the restaurant.

### Technologies Used
The YelpQueryMaster application comprised two major components - the user interface and database. The followings are the technologies used during the development of YelpQueryMaster application:
- **C# WPF**: a programming framework used to implement user interfaces
- **PostgresQL**: a database management system used to maintain database
- **SQL**: Structured Query Language (SQL) used to retrieve and post data to the database
- **Npgsql**: middleware that enable C# to access the database.


### Software Architecture

Components for the entire YelpQueryMaster system can be describe as 4 modules
- C# WPF User Interface
- PostgreSQL database 
- SQL trigger
- SQL function

*Figure 1. Software Architecture*

<img width="539" alt="image" src="https://user-images.githubusercontent.com/57877290/215619504-757d0b35-bbb5-4ba4-af23-341cdc702358.png">

#### C# WPF User Interface
The C# WPF user interface is a crucial component of the YelpQueryMaster application, as it presents the data retrieved from the database in a graphical format for the user's convenience. The user interface leverages the capabilities of the WPF framework to provide an intuitive and visually appealing display of the data. The interface acts as the bridge between the database and the end-user, presenting the information in a way that is easy to understand and interact with.

#### PostgresSQL Database
The PostgresSQL component of the YelpQueryMaster application plays a vital role in ensuring the integrity and reliability of the data stored within the database. This component is responsible for maintaining the data, ensuring its availability and consistency. The use of PostgresQL as the database management system provides robust and scalable data storage capabilities, allowing the YelpQueryMaster application to efficiently manage large amounts of data. The PostgresSQL component acts as the backbone of the YelpQueryMaster, providing a secure and stable foundation for data storage and management.

#### SQL Trigger
The SQL Trigger component of the YelpQueryMaster application plays a crucial role in ensuring the integrity of the data during user interactions. This component trigger certain actions in response to specific events, such as check in to the restaurant and add tip to the restaurant. The SQL Trigger component serves as an automated safety mechanism, verifying the validity of data before it is processed and stored in the database. This helps to prevent potential errors or inconsistencies, and ensures that the data stored in the database remains accurate and consistent. The SQL Trigger component is an integral part of the YelpQueryMaster, working behind the scenes to maintain data integrity and provide a seamless user experience.

#### SQL Function
The SQL Function component of the YelpQueryMaster application is a critical component that plays a crucial role in the calculation of distances between a logged-in user and millions of restaurants. This component leverages the power of SQL to perform complex calculations with high performance and efficiency. The use of SQL Functions providing users with accurate and relevant information in real-time. The decision to use SQL Functions was made to ensure fast and reliable performance, ensuring a seamless and efficient user experience.

### Setup Instructions
**Options**

- [Setup Database Option 1](#Setup-Database-From-Scratch)
- [Setup Database Option 2 (Recommanded)](#Setup-Database-by-Backup-File)
- [Run the C# Application](#Setup-Database-by-Backup-File)

#### Setup Database From Scratch

**Step 1**

Download the Json file and put them into `data/`, download link = `https://eecs.wsu.edu/~blin1/files.html` click the `YelpQueryMaster yelpJsonData.zip`

Install all of python modules required for parsing and inserting
```bash
pip install -r requirements.txt
```
or for Mac users
```bash
pip3 install -r requirements.txt
```

**Step 2**

Modify `.env` file in root directory depending on your database setup.

**Step 3**

Import the `./DBSchema/mysql_supremacy_RELATIONS_v2.sql` file into your database to create tables.

**Step 4**

To load data into DB, first make sure data files are saved in `./data/`, then running the following commands.
```bash
cd DBPopulate
python mysql_supremacy_parseAndInsert.py
```
or for Mac users

```bash
cd DBPopulate
python3 mysql_supremacy_parseAndInsert.py
```

**Step 5**

Load triggers, functions, updates into database, they are located in `SQLScripts/`



#### Setup Database by Backup File

**Step 1**

Download the backup file at `https://eecs.wsu.edu/~blin1/files.html` click `YelpQueryMaster Backup File`;

**Step 2**

Create your database and load the backup file using `\i` 



#### Run The Application

1. VS installed
2. `cd/YelpSrc/`, execute the `YelpSrc.sln`
3. Install the ScottPlot see `https://www.nuget.org/packages/ScottPlot.WPF/`
4. Install the NpgSQL see `https://www.npgsql.org/doc/installation.html`




### Demo
![image](https://user-images.githubusercontent.com/57877290/215622853-45bc1586-c09a-4398-b78a-4ba69c9f2e31.png)
![image](https://user-images.githubusercontent.com/57877290/215622876-07156764-e823-4aa3-8334-e428c21a555a.png)


