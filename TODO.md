# Integration Plan: Frontend with Backend

## Tasks
- [x] Update frontend/src/api.js to include /api in baseURL
- [x] Fix frontend/src/stores/auth.js for correct token and user handling
- [x] Update frontend/src/components/Hospitals/DoctorList.vue endpoint and book API call
- [x] Update backend/routes/tickets.py to include doctor_id in get_my_tickets response
- [x] Update frontend/src/components/Dashboard/PatientDashboard.vue to use doctor_id for queue link
- [x] Update frontend/src/components/Hospitals/DoctorList.vue to use timings instead of consultation_time_minutes
- [x] Test integration by running backend and frontend servers
- [x] Verify login, registration, hospital/doctor fetching, ticket booking, and queue viewing

## Followup Steps
- Run backend server: cd backend && python app.py
- Run frontend server: cd frontend && npm run dev
- Test all functionalities
- Handle any errors or missing features
