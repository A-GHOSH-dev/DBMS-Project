--CREATE DATABASE MyDatabasedbms  

use MyDatabasedbms  


create table adduser(
addemp_id int primary key, --Employee ID
addemail varchar(100) not null, --Email address
addname varchar(50) not null, --Name
adddepartment varchar(100) not null, --Department
addsection varchar(100) not null, --Section
addrole varchar(100) not null, --Role of User
addtraining varchar(25) not null, --Training Recieved or not for the Role (Yes/No)
addphone numeric(15) not null, --Phone
addpassword varchar(25) not null); --Password

create table incidentreporting(
datereport date not null, --Date of Reporting
timereport time not null, --Time of Reporting
reportedby varchar(50) not null, --Incident Reported By
dateincident date not null, --Date of Incident
timeincident time not null, --Time of Incident
locationincident varchar(50) not null, --Location of Incident
incidentdesc varchar(1000) not null, --Incient Description
incidentaction varchar(1000) not null, --Immediate actions taken & Current Status
victimname varchar(50) not null, --Name of Victim (if Any)
victimrole varchar(100) not null, --Role of Victim (Employee/Contractor/Visitor/Others)
victimemp_id int primary key not null, --Employee ID (if employee)
victimcon_id varchar(100) not null, --Name of Contractor agency (if contractor)
assign_inv_email varchar(100) not null); --Email address

create table assigninvestigator(
incident_id int primary key, --Incident ID
nameassignedinvestigator varchar(50) not null, --Name of Investigator Assigned
emailassignedinvestigator varchar(100) not null); --Email address of Investigator assigned

create table whywhyanalyzing(
whyinc_id int primary key, --Incident ID
ps varchar(100) not null, --Incident ID
why1 varchar(100) not null, --Why1
why2 varchar(100) not null, -- Why2
why3 varchar(100) not null, --Why3
why4 varchar(100) not null, --Why4
why5 varchar(100) not null, --Why5
rc varchar(100) not null, --Root causes
constraint fk_why foreign key(whyinc_id) references AssignInvestigator(Incident_id));

create table specialanalyzing(
spe_inc_id int primary key, --Incident ID
imm_cause_unsafe_ac varchar(100) not null, --Immediate Causes (Unsafe Actions)
imm_cause_unsafe_con varchar(100) not null, --Immediate Causes (Unsafe Conditions)
root_cause_human_fac varchar(100) not null, --Root Causes (Human Factors)
root_cause_org_fac varchar(100) not null, --Root Causes (Organizational Factors)
constraint fk_sp_analysis foreign key(spe_inc_id) references AssignInvestigator(Incident_id));

create table finalreport(
reinc_id int primary key, --Incident ID
inc_type varchar(200) not null,
summary varchar(100) not null, --Summary of Incident
img image not null, --Image Upload
rca varchar(50) not null, --RCA Tool used
imc varchar(100) not null, --Immediate Causes
rtc varchar(100) not null, --Root Causes
ca varchar(100) not null, --Corrective action
cap varchar(100) not null, --Corrective action responsible person
cad varchar(100) not null, --Corrective action target date
pa varchar(200) not null, --Preventive action 
pap varchar(200) not null,--Preventive action responsible person
pat varchar(200) not null, --Preventive action target date
intensity int not null, --Intensity/Level of Incident using Risk Matrix
constraint fk_report foreign key(reinc_id) references AssignInvestigator(Incident_id));

create table actionclosure(
actionclose_inc_id int primary key, --Incident ID
actiondonebyname varchar(100) not null, --action done by the person name
actiontaken varchar(1000) not null, --what are the actions taken
completiondate date not null, --action completion date
constraint fk_action foreign key(actionclose_inc_id) references AssignInvestigator(Incident_id));

create table verifyactionclose(
ver_action_close_inc_id int primary key, --Incident ID
inc_closeoropen varchar(10) not null, --Incident Status (Close/ Open)
remarks varchar(500) not null, --Any Remarks
constraint fk_verify foreign key(ver_action_close_inc_id) references AssignInvestigator(Incident_id));

--drop table adduser
--drop table incidentreporting

--drop table verifyactionclose
--drop table actionclosure
--drop table finalreport
--drop table specialanalyzing
--drop table whywhyanalyzing

--drop table assigninvestigator

select * from adduser
select * from incidentreporting
select * from assigninvestigator