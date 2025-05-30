# END2END AWS. Development of a product for an aerodrome

Jacinto is the son of the owner of an aerodrome. His father has been running the business for more than 40 years in a traditional way, writing down all the information in different notebooks. 

Each fligth that lands has a notebook where the pilot writes down the plate number of the aircraft, time of arrival, the list of passengers, the fuel consumption, and the time of departure.

The same happens with the hangars, each airplane is register in a notebook with the plate number the type of airplane, the last maintenance date, next maintenance date and the id of the owner. 

The passengers are registered in another notebook with the name, age, national id, date of birth.

Jacinto's father is about to retire and Jacinto wants to modernize the aerodrome. He wants to develop a software that allows him to manage the aerodrome in a more efficient way. He wants to have an application where he wants to be able to do the following:

1. See the list of airplanes that are in the hangars.
2. See the list of flights that have landed.
3. See the list of passengers that have arrived at the aerodrome.

4. Register each airplane (new or not) that is in a hangar.
5. Register each flight that lands.
6. Register each passenger that arrives at the aerodrome.

7. Check number of days until next maintenance of an airplane.
8. Check the number of empty seats of each flight.
9. Check the boarding status of passengers.

10. Show an alert if the number of empty seats is higher than 10% of the total seats.
11. Show an alert if the number of days until next maintenance is less than 100 days.
12. Show an alert if the fuel consumption of a flight is higher than 10% of the total fuel capacity of the airplane.


Jacinto has hired you to develop this product. You will follow an agile methodology to develop it. You must always think on how to add value to the product and you should always be ready to show the product to Jacinto. You will work in small sprints and at the end of each sprint you will show the product to Jacinto. Jacinto will give you feedback and you will continue working on the product.

The product has to be deployed in AWS, as Jacinto wants to be able to access it from anywhere. He doesn't mind if the product doesn't have a UI, he can handle a terminal for the MVP.

From the MVP, the sky is the limit. You can Dockerize it, create an API, a UI to interact with the prouduct. You could even try to deploy it using microk8s in a virtual machine.

Initial user stories have been created for you. You can find them in the [following link](https://trello.com/invite/b/6829f2faf4b11236386a42dc/ATTIb892baeadcfa70247901fbb24b5d9349063D636B/basic-board), after creating a Trello Account