This document acts as a diary to log progress on the project as it is being completed.

Wed 29 July 13:45 
* Initial Project scope is confirmed and repository is created

* The Project scope being:
    * Visualised race track with entities that track each drivers position in sync with drivers
    * Selecting an entity pulls up their respective telemetry; braking, speed, DRS etc.
    * Capacity to select two or more drivers to compare telemetry for analysis
    * 

* Long term goals with the project:
    * Derive meaningful conclusions from the analysis
    * deepen python knowledge

* Today's goals:
    * Familiarise myself with github & set out python foundations

* Achieved:
    * Created Repository and cloned locally onto device
    * Getting Familiar myself with the fastf1 package
    ![alt text](image-1.png)

Sat 1 Aug 12:12
* Continuation of tinkering with fast f1 package
* Since I last approached this project I've been thinking more about what I could possibly apply this application to and I concluded that it would be interesting to investigate two aspects of the sport:
    * Investigate how the changes to the distribution of how the car receives power (ICE vs battery) impacts the nature of the sport and how 
    * Investigate George Russell's claims that Merc is providing the younger, newer driver Kimi Antonelli a better performing car this season to explain what people believe to be a lackluster performance following Hamiltons departure
* These goals I believe give my work a clear direction and give me a clear direction in what I need to learn in order to find conclusions to these investigatiosn

* Today's goals:
    * Read up on fastf1 documentation regarding telemery 
    * Figure out how to plot telemtry data

* Notes:
    * Telemetry data is included in the session data, make sure that is loaded first 
    * Telemetry data is treated the same as all the other data types
    * Relearned alot of coding fundamentals. Remember to use library shortcuts if using their commands (OBVIOUS)
    * Telemetry data doesnt include braking as a float but as a bool
    * Look into discussion RUS vs ANT
    * Look into how to regulation changes have impacted lap times

* Achieved:
    * Created F1 Speed Trace graph comparision of Antonelli & Russell to compare drivers on the same team
    * Created F1 Throttle Trace graph of Hamilton
    * Familiarising myself with matplotlib again
    ![alt text](ANTvsRUS_tr.png)
    ![alt text](HAM_Throttle.png)