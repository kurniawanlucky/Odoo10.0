Module Name: 
==
booking_service

Short Description: 
--
To allow users to create bookings for employees and equipments

Navigation Menu to create:
--
Name | Parent Menu | Views | Remarks
-----|-------------|-------|--------
Booking Order | Booking | List, Form, Calendar | Create a new “Booking” Parent Menu under Sales, and next to sales dropdown
Work Order | Booking | List, Form, Calendar | 
Team | Booking | List, Form

Flow to create / edit:
--
Location & View Type | Fields / Flow / Function / Triggers
---------------------|------------------------------------
* Product 
    * Add a Checklist “Is an equipment” under the general information
* Calendar Event
    * Add “Equipments” under Attendees, which is a multi select of Serial Numbers
* Employees 
    * Add a button on the top right next to Active button, called “Events” which is a calendar of their events
* Serial Number 
    * Similar to employees, add a button on the top right of the serial number form view, which will show their calendar events
* Team
    * These are the fields in the form View:
        * Team Name – Textfield – Compulsory
        * Team leader – Dropdown of employees
        * Employees (List of employees, like invoice lines)
        * Equipments (List of products that has “Is an Equipment” ticked, and select their Serial Numbers, like invoice lines) Both fields are compulsory when adding a line
        ![plot](static/description/1.png)
* Booking Order
    * Add “Is a booking” in all Quotations & Sales Orders in the Other Information Tab
    * If “Is a booking” is ticked, then add the following fields:
        * Team -> dropdown of teams (non compulsory
        * Team Leader -> Dropdown of employees (when team is selected, it will auto fill this employees field but it is still editable )
        * Employees -> Dropdown of employees (when team is selected, it will auto fill this employees field but it is still editable )
        * Equipments -> Dropdown of equipments (when team is selected, it will auto fill this employees field but it is still editable )
        * Booking Start - > Date Time - Compulsory
        * Booking End -> Date Time – Compulsory (By default, after user fill in the boo ing start, it will auto fill the booking end by booking start + 1 hour, but editable)
        ![plot](static/description/Customer.png)
        * Add a navigation called “Booking Order” which will show all the Sales Order that “is a booking”. In the Sales Order menu, it will only show all Sales Order that is not a booking. When user creates an order from the Booking Order Menu, it will auto tick the “Is a booking”
        * Add a button “Check” next to “Validate”, which will check if the team leader employees and equipments has any calendar event which overlaps for the booking start and booking end time.
            * If yes, highlight a popup saying:
                * Employee A, Employee B and Equipment C (this is dynamic) has an event on that day and time
            * If no, highlight a popup saying
                * Everyone is available for the booking
        * Upon clicking validate, it will do the “check” once again
            * If yes, highlight a popup saying:
                * Employee A, Employee B and Equipment C (this is dynamic) has an event on that day and time, are you sure you want to validate?
                    * If yes, validate
                    * If no, don’t validate
            * If no, simply validate
                * A calendar event for the employee, team leader and equipments for that booking start and time is automatically created, which will show in the Employees and Serial Number’s calendar.
        * Upon validation, create a “Work Order”, explained in the next row, the Work Order created from Booking Order will directly go to “Pending” stage
        * Note: The invoice creation still follows normal Sales Order Delivery Order flow
        * Ensure there is a function called “makebookingorder” which allows other developers to call this function to create work orders which will create calendar event (like the above flow)
        * []Is a booking needs to be ticked by default (true) if created from booking order and hide it
* Work Order
    * Add “Is a booking” in all Delivery Orders in the Other Information Tab
    * If “Is a booking” is ticked, then add the following fields:
        * Change “Delivery Order” to “Work Order”, with its own sequence
        * Add the fields (UI make it similar to the booking order)
            * Scheduled Start - compulsory (based on booking order’s booking start)
            * Scheduled End - compulsory (based on booking order’s booking end)
            * Actual Start - compulsory (based on booking order’s booking start, but editable)
            * Actual End - compulsory (based on booking order’s booking end, but edtable)
            * Team (based on booking orders’ booking, but editable)
            * Team Leader (based on booking orders’ booking, but editable)
            * Employees (based on booking orders’ booking, but editable)
            * Equipments (based on booking orders’ booking, but editable)
    * Add a navigation called “Work Order” which will show all the Delivery Order that “is a booking”. In the Work Order menu, it will only show all Work Order that is a booking. When user creates an order from the Work Order Menu, it will auto tick the “Is a booking”
    * Other functions like DO works as per normal, user can still add things in the DO line to make stock moves.
    * Add a status “Pending” before “Available”
    * Add a button “Check” next to “Mark to do”, which will check if the team leader employees and equipments has any calendar event which overlaps for the booking start and booking end time.
        * If yes, highlight a popup saying:
            * Employee A, Employee B and Equipment C (this is dynamic) has an event on that day and time
        * If no, highlight a popup saying
            * Everyone is available for the booking
    * Upon clicking “Mark to do”, it will do the “check” once again
        * If yes, highlight a popup saying:
            * Employee A, Employee B and Equipment C (this is dynamic) has an event on that day and time, are you sure you want to validate?
                * If yes, mark to do
                * If no, don’t mark to do
        * If no, simply mark to do, and the Work Order becomes “Pending”
            * A calendar event for the employee, team leader and equipments for that booking start and time is automatically created, which will show in the Employees and Serial Number’s calendar.
    * When WO is validated, there is a button called “Start”. After click start, the Actual Start will be auto filled. And then it goes to “Available”
    * Rename “Available” to “Started”
    * When user click “Validate” button in “Available” status, the booking end will be auto filled
    * Ensure there is a function called “makeworkorder” which allows other developers to call this function to create work orders which will create calendar event (like the above flow)
    * [ ]Is a booking needs to be ticked by default (true) if created from work order and hide it

Access Rights to create / edit:
---
Module | Name | Description of access
-------|------|----------------------
Booking | User | Have access to view and edit his own work order (the ones where he is a team leader or employee)
Booking | Manager | Have full access to booking order and work order and team
Warehouse | User | Able to view the serial number’s calendar event but not edit
Warehouse | Manager | Able to view and edit the serial numbers’ calendar events