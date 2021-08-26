CREATE TABLE IF NOT EXISTS therapists (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
    description VARCHAR(50),
    schedule VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	created_date TIMESTAMPTZ NOT NULL
);


CREATE TABLE IF NOT EXISTS patients (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
    schedule VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
    therapist_id INTEGER NOT NULL REFERENCES therapists (id),
	created_date TIMESTAMPTZ NOT NULL
);


CREATE TABLE IF NOT EXISTS events (
	id serial PRIMARY KEY,
	description VARCHAR(50),
	start_date TIMESTAMPTZ NOT NULL,
	end_date TIMESTAMPTZ NOT NULL,
	frequency INTEGER NOT NULL,
    price_per_session INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL REFERENCES therapists (id),
    patient_id INTEGER NOT NULL REFERENCES patients (id),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS event_history (
	id serial PRIMARY KEY,
	event_id INTEGER NOT NULL REFERENCES events (id),
	description VARCHAR(50),
	date TIMESTAMPTZ NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT "PENDING",
	paid BOOLEAN NOT NULL DEFAULT FALSE
);