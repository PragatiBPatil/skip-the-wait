-- Supabase Database Schema for Hospital Queue Management System

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    role VARCHAR(20) DEFAULT 'patient' CHECK (role IN ('patient', 'doctor', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Hospitals table
CREATE TABLE hospitals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    address VARCHAR(200),
    specialization VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Doctors table
CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100),
    hospital_id INTEGER REFERENCES hospitals(id) ON DELETE CASCADE,
    timings VARCHAR(100),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tickets table
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    doctor_id INTEGER REFERENCES doctors(id) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'waiting' CHECK (status IN ('waiting', 'served', 'missed', 'cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for better performance
CREATE INDEX idx_tickets_patient_id ON tickets(patient_id);
CREATE INDEX idx_tickets_doctor_id ON tickets(doctor_id);
CREATE INDEX idx_tickets_status ON tickets(status);
CREATE INDEX idx_doctors_hospital_id ON doctors(hospital_id);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

-- Note: Since we're using SQLAlchemy with custom JWT authentication,
-- Row Level Security policies are provided for reference but may not be
-- automatically enforced when connecting directly to Postgres.
-- Security is handled at the application level in Flask routes.

-- If you want to use Supabase Auth instead of Flask-JWT-Extended,
-- uncomment and modify the policies below:

-- Row Level Security (RLS) Policies for Supabase Auth
-- (Uncomment if using Supabase Auth)

-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE hospitals ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE doctors ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE tickets ENABLE ROW LEVEL SECURITY;

-- Users policies
-- CREATE POLICY "Users can view own profile" ON users
--     FOR SELECT USING (auth.uid()::text = id::text OR auth.jwt() ->> 'role' = 'admin');

-- CREATE POLICY "Users can update own profile" ON users
--     FOR UPDATE USING (auth.uid()::text = id::text);

-- CREATE POLICY "Admins have full access to users" ON users
--     FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Hospitals policies
-- CREATE POLICY "Public read access to hospitals" ON hospitals
--     FOR SELECT USING (true);

-- CREATE POLICY "Admins manage hospitals" ON hospitals
--     FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Doctors policies
-- CREATE POLICY "Public read access to doctors" ON doctors
--     FOR SELECT USING (true);

-- CREATE POLICY "Doctors can update own profile" ON doctors
--     FOR UPDATE USING (auth.uid()::text = user_id::text);

-- CREATE POLICY "Admins manage doctors" ON doctors
--     FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Tickets policies
-- CREATE POLICY "Patients can view own tickets" ON tickets
--     FOR SELECT USING (auth.uid()::text = patient_id::text);

-- CREATE POLICY "Patients can create tickets" ON tickets
--     FOR INSERT WITH CHECK (auth.uid()::text = patient_id::text);

-- CREATE POLICY "Patients can update own tickets" ON tickets
--     FOR UPDATE USING (auth.uid()::text = patient_id::text AND status IN ('cancelled'));

-- CREATE POLICY "Doctors can view their patients tickets" ON tickets
--     FOR SELECT USING (
--         doctor_id IN (
--             SELECT id FROM doctors WHERE user_id::text = auth.uid()::text
--         )
--     );

-- CREATE POLICY "Doctors can update ticket status" ON tickets
--     FOR UPDATE USING (
--         doctor_id IN (
--             SELECT id FROM doctors WHERE user_id::text = auth.uid()::text
--         )
--     );

-- CREATE POLICY "Admins have full access to tickets" ON tickets
--     FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger to automatically update updated_at
CREATE TRIGGER update_tickets_updated_at
    BEFORE UPDATE ON tickets
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
