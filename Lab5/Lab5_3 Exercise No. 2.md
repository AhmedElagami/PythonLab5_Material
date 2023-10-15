### Project: Media Inventory Management System

- Create a comprehensive **media management system** for a **library**. 
- This system, known as "**Library**," will handle various types of **media**—including **books**, **magazines**, and **newspapers**. 
- All **media** have common properties: title, author, and copies available.
- Books have an additional property: year published.
- Magazines might have an additional property like category, and newspapers might have properties like frequency of publication.
#### Tasks
##### Error Handling:
- The system should not crash on unexpected input.
- It should inform the user of things like "Media Not Found" or "Invalid Media Type."
- Custom exceptions like MediaNotFound and InvalidMediaType should be defined and raised appropriately.
##### Modular Code:
- Code should be split into various modules and organized in a package.
##### Modules and Packages:
- Each class should be defined in its own module, and all related modules should be contained within a MediaInventory package.
##### User Interaction:
- The script should allow interaction from the console for tasks like adding new media and searching the inventory.

### Solution

#### Entities & Relationships (Collections)

> The **design** is the **class**
> The **instances** are the **objects**
##### **(A) Book**  Child/Sub/Derived class
**Each** book is media +
##### AND:
it has :
**- Year Published**
			Example: 1949
			*This is a number so it should be an **integer***

> So each book is a type of media but it also have a field called year_published
##### **(A) Magazine** 
**Each** magazine is media:
##### AND:

**- Category**
			Example: "Fashion"
			*This is text so it should be an **String***

> So each magazine is a type of media but it also have a field called category
##### **(A) newspapar** 
**Each** newspaper is media
##### AND:

**- Publishing Frequency**
			Example: "Daily"
			*This is text so it should be an **String***

> So each newspaper is a type of media but it also have a field called publishingFrequency
##### Base/Parent/Super **Media Class**
**Each** media instance has the following data:
**- Title**
			Example: "To Kill a Mockingbird"
			*This is a text so it should be a **String***

**- Author**
			Example: "Harper Lee"
			*This is a text so it should be a **String***

**- Copies Available**
			Example: 30
			*This is a number so it should be an **integer***
##### **(A) Library**
All media belong the library => **A library has a lot of media**

**Functions:**
- Add new media to the inventory.
- Search for media by different criteria (e.g., year published for books).
- Display available inventory.

