# MerryTaskmas
=======
<p align="center">
  <img src="documentation/images/home.png">
</p>

## Introduction

**MerryTaskmas** is an educational project developed for the final Hackathon of a Code Institute Bootcamp. In the spirit of the holiday season, we created MerryTaskmas, your ultimate holiday helper that tracks everything related to Christmas. This application allows you to manage your to-do lists, create Christmas wishlists for your loved ones, and features a countdown to Christmas, among other festive functionalities.

View the live site here: [MerryTaskmas]()

For Admin access with relevant sign-in information: [MarryTaskmas Admin]()

---

## Table of Contents

## Overview

# Merry Taskmas Overview

**Merry Taskmas** is a holiday organization app designed to help individuals manage the chaos of the Christmas season. It provides tools to streamline holiday planning, allowing users to:

- Keep track of the days until Christmas with a **dynamic countdown timer**.
- Create and manage a **to-do list** for all holiday-related tasks.
- Organize gifts with a **gift list**, including sections for family, friends and budget.
- Plan and schedule holiday events with a **calendar** (optional feature).
- Prepare for holiday gatherings with a **shopping list** and **meal planner** (optional features).

Merry Taskmas is fully accessible via modern web browsers and is responsive across all screen sizes. Its goal is to simplify holiday organization, reduce seasonal stress, and add a bit of festive cheer to everyday planning.

While other task management apps exist, Merry Taskmas is uniquely tailored to the Christmas holidays, offering specialized features like the Christmas countdown, gift tracker, and holiday-themed user interface.

## Future Development Plans:
- Enhanced gift list capabilities, such as tagging gifts with recipient preferences or marking gifts as “shipped” or “wrapped.”
- Interactive meal planner with built-in recipe suggestions for traditional holiday dishes.
- Ability to sync tasks, events, and shopping lists across devices.
- A sharing feature for collaborative planning with family and friends.

**Merry Taskmas** aims to bring joy, simplicity, and organization to every user’s Christmas season, fostering a stress-free and memorable holiday.


---

## UX - User Experience

### Design Inspiration

The design of **Merry Taskmas** was inspired by the previous project work of the development team. With this being the final bootcamp hackathon and the holiday season upon us, the team decided that a Christmas theme would be the perfect fit. 

The festive design aims to create a cheerful and engaging experience for users while maintaining functionality and simplicity to help them stay organized during the holidays.


### Colour Scheme

Christmas!

### Font

Using [Google Fonts](https://fonts.google.com/), I imported Alice and Raleway. Alice for headings and a bit of interest, the curls in the font felt a bit Christmassy. Raleway was used for clarity in the rest of the text.
  
# Project Planning  
 
## Strategy Plane

**Problem Statement**:  
How do we create a website that enables users to easily organize and manage tasks, events, and plans around the Christmas holidays?

**Purpose**:  
The purpose of **Merry Taskmas** is to:
- Simplify holiday organization and planning.
- Reduce seasonal stress by offering tools to track to-do lists, gifts, and events.
- Provide an intuitive and festive platform that fosters holiday cheer while keeping users on top of their tasks.
- Help users prepare for Christmas with features like a Christmas Countdown, To Do List, and Gift Tracker.

**Target Audience**:  
The primary target audience for **Merry Taskmas** includes:
- Individuals or families who want to organize their holiday season more efficiently.
- Busy professionals juggling work and holiday preparations.
- Anyone looking for a simple, accessible tool to track gifts, meals, and events during the Christmas season.
- People who enjoy a festive, cheerful theme while managing their tasks.

The app is designed for anyone who loves Christmas and could benefit from a user-friendly and engaging way to plan their holidays.


### Site Goals

- Have fun creating something in Django using CRUD functionality.

## Agile Methodologies - Project Management

**Merry Taskmas** was built using Agile methodology. Our team used the [GitHub Project Board](https://github.com/users/TaylaJBall/projects/3) to track our tasks, organize user stories, and ensure the project stayed within Scope. 

The board served as a central hub for documenting progress and maintaining focus throughout the development process.


### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for LitRPG Library, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. 
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

### **Merry Taskmas Features**

| **ID** | **Title**                           | **User Stories**                                                                                  | **Priority**   |
|--------|-------------------------------------|--------------------------------------------------------------------------------------------------|----------------|
| **#1** | **User Login**                      | I want to log in to my account so that I can access my personal Christmas dashboard.             | **MUST HAVE**  |   
| **#2** | **Countdown to Christmas**          | I want to see a countdown to Christmas so that I can track how many days are left.               | **MUST HAVE**  |
| **#3** | **To-Do List for Preparations**     | I want to manage a to-do list so that I can organize tasks for Christmas preparations.           | **MUST HAVE**  |
| **#4** | **Wishlists for Gift Ideas**        | I want to create and manage wishlists for different people so that I can keep track of gift ideas. | **MUST HAVE**  |
| **#5** | **Festive UI**                      | I want to see a festive design on the dashboard so that I feel the Christmas spirit while using it. | **MUST HAVE**  |
| **#6** | **Registration**                    | I want to register for an account so that I can create my personalized dashboard.                | **MUST HAVE**  |
| **#7** | **Calendar for Parties/Events**     | I want to have a calendar to track Christmas parties and events so that I can stay organized.    | **SHOULD HAVE**|
| **#8** | **Meal Planner**                    | I want to plan meals for the holiday season so that I can stay organized and prepared for dinners. | **COULD HAVE** |
| **#9** | **Shopping List**                   | I want to manage a shopping list for Christmas so that I can keep track of the items I need to buy. | **COULD HAVE** |

## **Scope Plane**

The scope for this project focuses on delivering a **personalized Christmas planning dashboard** while ensuring the most essential features are implemented. While there are many possibilities for expanding the functionality, we narrowed it down to what was necessary for users to organize and enjoy their Christmas preparations effectively.

We initially considered incorporating advanced third-party APIs, such as calendar integrations or meal planning tools, but we found that simplicity was key for this first version. Features such as **user authentication**, a **countdown to Christmas**, and **task and gift management** were critical to achieving the project's goals.

This scope prioritizes delivering a functional and festive platform that enables users to plan, organize, and engage with their Christmas preparations.

---

### **Essential Features of Merry Taskmas**

- **User Authentication**
  - Registration, login, and logout functionality
  - Personalized dashboard for each user

- **Countdown to Christmas**
  - A real-time countdown feature displaying the days, hours, and minutes until Christmas
  - Festive visual representation for added excitement

- **Task Management**
  - A to-do list for organizing Christmas preparations
  - Add, edit, and delete tasks to keep track of progress

- **Giftlist Management**
  - Ability to create and manage giftlists for gift ideas
  - Separate giftlists for different people (e.g., family, friends)

- **Festive Design**
  - A visually appealing and festive user interface to create a joyful experience
  - Snowfall effects, Christmas-themed colors, and imagery

  ### **Should have Features

- **Event Management**
  - A calendar to track Christmas parties and events
  - Simplified event addition and management functionality

  ### **Could have Features

- **Meal Planning**
  - A section to plan meals for the holiday season
  - Ability to add dishes, edit menus, and organize meals for specific days

- **Shopping List**
  - A shopping list to manage items required for Christmas
  - Add, mark as purchased, and delete items as needed

---

### **Additional Considerations**
1. **User Experience**  
   - Ensuring the interface is intuitive and responsive for all devices.  
   - Keeping the design festive without compromising usability.

2. **Scalability**  
   - This first version focuses on core features but lays the groundwork for future enhancements like:  
     - Notifications for tasks and events  
     - Integration with external calendars (Google Calendar)  
     - Sharing wishlists with others.  

3. **User Control**  
   - Providing users with the ability to edit and delete their own tasks, wishlists, and events to maintain control over their data.

---

This scope ensures that **Merry Taskmas** delivers a clear, functional, and festive platform, providing essential tools for Christmas organization while leaving room for further growth in the future.

## **Structural Plane**

The structural plane focuses on the organization and architecture of the Merry Taskmas website. The goal is to create a functional, maintainable, and scalable site, adhering to Django’s **Model-View-Template (MVT)** framework. This structure ensures a clear separation of concerns and allows for future growth. We tried to adapt our previous projects to use in this project as there was very little time to complete it. 

---

### **Application Structure**

The Merry Taskmas project is divided into modular apps, each handling a distinct part of the functionality:

1. **Accounts**  
   - The **landing page** is the login page (`/accounts/login/`), ensuring that unauthenticated users are immediately prompted to sign in or sign up.  
   - Built using `django-allauth` to handle registration, login, and logout securely.  
   - Users are redirected to the dashboard (`/`) upon successful login.  

2. **Home**  
   - The **dashboard** for authenticated users, providing a central hub for accessing key features such as tasks, giftlists, and events.  
   - Redirects unauthenticated users back to the login page.

3. **Tasks**  
   - Allows users to manage a to-do list for Christmas preparations.  
   - Features include adding, editing, and deleting tasks.

4. **Giftlist**  
   - Enables users to create and manage wishlists for gift ideas.  
   - Supports multiple lists for different individuals (e.g., family, friends).

5. **Calendar**  
   - A calendar feature that helps users organize Christmas parties and events. (Should have feature)

6. **Core**  
   - Handles shared components like static files (CSS, JS), templates, and other common utilities.

# Skeleton & Surface Planes

### Wireframes

The wireframes for Merry Taskmas are fairly high fidelity and were created in [Figma](www.figma.com). We kept mostly to the general design. The circles in the footer represent each team member's picture and socials. 

**Mobile/Tablet view for:**  

- Sign In

<details open>
    <summary>Mobile/Tablet Sign In Page Wireframe</summary>  
    <img src="documentation/images/signin_wf.png">  
</details>

- Home Page

<details open>
    <summary>Mobile/Tablet Home Page Wireframe</summary>  
    <img src="documentation/images/home_wf.png">  
</details>

### Database Schema - Entity Relationship Diagram

![ERD Image](documentation/images/erd.png)  
*Database Schema (ERD) for Merry Taskmas*

The Entity Relationship Diagram (ERD) for the Merry Taskmas project visually represents the data structure and relationships between various entities in the system. This diagram reflects the key components of the website, such as user management, wishlists, to-do lists, and tasks, and how they interact with one another.

Note: We did change wishlist to giftlist as we preferred the terminology. A user is listing possible gifts to by for loved ones.

---

### **Entities and Relationships**

#### **1. User**
The **User** entity represents the core users of the Merry Taskmas platform. Each user can interact with multiple features such as creating wishlists, managing tasks, and organizing to-do lists.  

**Attributes**:  
- `UserID` (Primary Key): Unique identifier for each user.  
- `Name`: The user's name.  
- `Email`: Email address for user login.  
- `Password`: Encrypted password for authentication.  
- `CreatedAt`: Timestamp for account creation.  
- `UpdatedAt`: Timestamp for the last update to the user’s profile.  

**Relationships**:  
- A **User** can have multiple **Wishlists**.  
- A **User** can also create multiple **ToDoLists**.

---

#### **2. Wishlist**
The **Wishlist** entity allows users to create separate lists for different individuals (e.g., family members, friends) with a specific budget.  

**Attributes**:  
- `WishlistID` (Primary Key): Unique identifier for each wishlist.  
- `UserID` (Foreign Key): Links the wishlist to a specific user.  
- `PersonName`: Name of the person for whom the wishlist is created.  
- `Budget`: Total budget allocated for the wishlist.  
- `CreatedAt`: Timestamp for wishlist creation.  
- `UpdatedAt`: Timestamp for the last update to the wishlist.  

**Relationships**:  
- A **Wishlist** can have multiple **WishlistItems**.

---

#### **3. WishlistItems**
The **WishlistItems** entity contains individual gift ideas or items that belong to a wishlist.  

**Attributes**:  
- `WishlistItemID` (Primary Key): Unique identifier for each wishlist item.  
- `WishlistID` (Foreign Key): Links the item to a specific wishlist.  
- `Description`: Detailed description of the gift item.  
- `Link`: A URL or reference link for the gift (e.g., online store link).  
- `CreatedAt`: Timestamp for item creation.  
- `UpdatedAt`: Timestamp for the last update to the item.  

**Relationships**:  
- Each **WishlistItem** is linked to a specific **Wishlist**.  

---

#### **4. TodoList**
The **TodoList** entity allows users to manage lists of tasks needed for Christmas preparations.  

**Attributes**:  
- `TodoListID` (Primary Key): Unique identifier for each to-do list.  
- `UserID` (Foreign Key): Links the to-do list to a specific user.  
- `Title`: Title or name of the to-do list.  
- `CreatedAt`: Timestamp for to-do list creation.  
- `UpdatedAt`: Timestamp for the last update to the to-do list.  

**Relationships**:  
- A **TodoList** can have multiple **Tasks**.  

---

#### **5. Tasks**
The **Tasks** entity stores individual tasks that belong to a to-do list. These tasks can be marked as completed or pending.  

**Attributes**:  
- `TaskID` (Primary Key): Unique identifier for each task.  
- `TodoListID` (Foreign Key): Links the task to a specific to-do list.  
- `Description`: A detailed description of the task.  
- `IsCompleted`: Boolean field indicating if the task is completed (`True`) or not (`False`).  
- `CreatedAt`: Timestamp for task creation.  
- `UpdatedAt`: Timestamp for the last update to the task.  

**Relationships**:  
- Each **Task** is linked to a specific **TodoList**.  

---

### **Relationships Overview**

1. **User ↔ Wishlist**:  
   - A single user can create multiple wishlists.  
   - Each wishlist belongs to one user.

2. **Wishlist ↔ WishlistItems**:  
   - A single wishlist can contain multiple items (gifts).  
   - Each item belongs to one wishlist.

3. **User ↔ TodoList**:  
   - A single user can create multiple to-do lists.  
   - Each to-do list belongs to one user.

4. **TodoList ↔ Tasks**:  
   - A single to-do list can contain multiple tasks.  
   - Each task belongs to one to-do list.

---

### **Design Observations**

1. **Normalization**:  
   The database design is well-normalized with separate tables for each entity, ensuring no duplication of data.

2. **Scalability**:  
   - The structure allows for easy expansion of features. For example:
     - Adding new attributes (e.g., priority levels for tasks).  
     - Linking items or tasks to events or reminders.

3. **User Control**:  
   Users can manage their wishlists, tasks, and to-do lists independently while maintaining relationships between entities.

4. **Data Integrity**:  
   - Primary and Foreign Keys enforce referential integrity.  
   - Timestamps (`CreatedAt` and `UpdatedAt`) ensure accurate tracking of data changes.

---

### **Conclusion**
The ERD for **Merry Taskmas** outlines a clear, organized structure for managing users, wishlists, to-do lists, and tasks. The relationships between entities are well-defined, supporting essential features like user authentication, task management, and wishlist creation. This design ensures a robust, scalable foundation for the platform while allowing future enhancements.


