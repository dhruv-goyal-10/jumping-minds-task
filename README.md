# jumping_minds_task
Submission to Backend Developer Internship Task of Jumping Minds

## Initialization
You can create multiple elevator systems specifying the name, number of elevators & floors.
<img width="1302" alt="1" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/ee62b59a-1c3b-45ce-9a12-84a607d90ef4">

## List of elevators in elevator system
Get the list of all the elevator systems.
<img width="1300" alt="2" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/d01631fa-3408-4b88-8064-504f11c9613e">

## Create Elevator Request
You can create an elevator request specifying the elevator system and the from_floor & to_floor fields.
<img width="1307" alt="3" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/10b1f901-7b6e-4f9e-981d-70494cd180e5">

An error is thrown if user tries to requests the elevator which is not in range of floors.
<img width="1307" alt="4" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/09e1b2cb-cfa0-41a1-aa3e-319d8b3a4a22">

An error is thrown if user tries to enter the same value of from_floor & to_floor.
<img width="1301" alt="5" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/5274d164-8546-4bdb-be38-27217f20b60c">

The elevator request can be directly processed (in earlier case) or queued, depending upon the availability of elevator. 
<img width="1304" alt="6" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/79025a00-b41b-447d-8b8a-eecf2ab95868">

## List of requests in elevator system
Get all the requests which are either queued, processed or finished by an elevator system.
<img width="1296" alt="7" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/1a7bc948-9ffa-4ca5-8af4-dc59f42d70a5">

## Status of elevator in elevator system.
Get all the details related to elevator using elevator_id such as moving direction, door status, elevator status etc.
You can also update the status of elevator to maintenance as shown below using PATCH request.
<img width="1295" alt="8" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/7a72cfde-72b3-4789-b098-78967cd51a51">

## Concept of Time Increment API
I have added a concept of time factor in the elevator system. Because, without it there would be no concept of busy state, given the elevators don't take any time to go up and down. So, I have made time_increment API, that increments the world by 1 unit (or 1 second).

## Snapshot of the database before calling Time Increment API
Some requests are queued & some are in processing stage.
<img width="1129" alt="9" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/7248cc8e-3ea3-43d6-8492-d67209c68800">

## Calling Time Increment API
<img width="1300" alt="10" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/40023282-8198-4392-9edc-dacac02a9545">

## Snapshot of the database before calling Time Increment API
The requests which were processing earlier have been finished & queued requests are now in processing stage.
<img width="1116" alt="11" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/97c0c746-c024-48b5-9a5e-1bf2d09f6a7c">

## Snapshot of the database before calling Time Increment API again
All the requests have been finished now.
<img width="1121" alt="12" src="https://github.com/dhruv-goyal-10/jumping-minds-task/assets/91484101/fd7816d3-f472-447d-b6c9-a06de156ab3d">

