# psique-facil
Web app that lets clinical psychologists manage their patients.

## Features
- [x] Lets therapists and patients input their availability schedule.
- [ ] Lets therapists schedule for weekly and 2-weekly sesssions.
- [ ] Lets patients and therapists schedule one off sessions
- [ ] Lets therapists share "homework" with their patients
- [ ] Lets patients reschedule without too much back and forth.
- [ ] Notifies patients one hour/the day before or the morning before their session.
- [ ] Helps therapists keep a digital record of their patient.

## Marketing Feature
* Calculate how many sessions our product would need to save to breakeven.

## Future Features
* Payment as a service for Psychologists so they don't have to manage payments.
* Transcribe audio to text for session notes


# Next tasks

### Timezone feature

- [x] Make api that returns list of valid timezones
- [x] Create ajax call in frontend to create select input for these layouts
- [x] Set default timezone to "local"
- [x] Add dynamic change to calendar when select input changes
  - This will help https://fullcalendar.io/docs/timeZone

### Scheduling feature

- [x] Create CRUD command that saves available hours to database
- [ ] When user changes timezone, automatically change hours. Or even trigger this change if saved timezone is different from browser detected timezone. This may not be super critical so it can probably be pushed until after MVP
- [x] Create api that gets events -- For available hours, that the user can schedule
- [x] Create frontend to select available hour and save choice to DB
- [ ] Create calendar so therapist can check out their agenda
- [ ] Create calendar so patient can check out their agenda


### Reschedule Feature
### Notifications Feature
### Homework Feature
### Digital Record Feature