# Murders RPC

<br/>

Murder RPC is an app made in college using RPC in Python

<br/>

# Work Context

<br/>

This work aimed to develop students' skills in
use of data representation methods (through the use of annotation languages)
to help the integration of different systems and thus allow their interoperability.

<br/>

# Work rules

<br/>

+ For the development of the proposed works, the languages of
Python programming (XMLRPC) or Javascript (Node.js / gRPC).
+ The implementation details that are due to the interpretation of the statements by the
groups of students should be described in the report with details and justification of the options
sockets.
+ The implementation of extra functionalities not present in the statement will be valued, provided that
these features do not modify the mandatory requirements and do not reduce the difficulty of the
job. The extra functionalities implemented must be documented in the report.

<br/>

# Work fullfiled goals description

<br/>

 - [x]  Each group must choose a dataset at https://www.kaggle.com/datasets. The dataset chosen must be unique for each group, cannot be in XML and must have at least 1 MB. Students must communicate with teachers through Moodle, the chosen dataset. If 2 groups choose the same dataset, the assignment will be on a first-come, first-served basis.
 - [x] The group must define an XML format to store the data of the chosen dataset. THE definition of the XML format must be accompanied by the respective XML Schema, in order it to be possible to validate documents of the new format.
 - [x] The group must build a service to import the data from the old dataset to XML in the new format.
 - [x] All imported documents must be previously validated with the Schema and persist in the database. A Postgree database can be used with a table unique with the following fields: The. ID (self-generated unique) B. Imported file name (VARCHAR) ç. Content of the imported XML file (XML type) d. Import date (datetime)
 - [x] It should be possible to remove or add new files via RPC. In the case of removal, a “soft-delete” must be done.
 - [x] At least 5 RPC routines must be implemented for data queries in XML columns  of the constructed database (example: if the database is a library, a routine example would be consulting all books published by a given author in 1987). The. Queries should use XPATH/XQuery whenever possible to optimize the search results B. Queries will be performed on all imported files. It must be indicated in the call to the RPC function if the results should be grouped by file or accumulated in a single result. ç. Routines should return only essential data (instead of returning complete objects) d. Routines with some level of complexity should be chosen: i. Include text search; ii. Inclusion of filters; iii. Grouping of results; iv. Sorting results; v. Exchange of information between different levels of the document.

<br/>

# Architecture

<br/>

![murdersDiagram-Server drawio](https://user-images.githubusercontent.com/76015450/178151536-333c58ea-7469-44a7-aa86-078eaa848ce3.png)

<br/>
