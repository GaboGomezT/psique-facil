CREATE TABLE IF NOT EXISTS therapist (
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


CREATE TABLE IF NOT EXISTS patient (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
    schedule VARCHAR(100) NOT NULL,
	email VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
    therapist_id INTEGER NOT NULL REFERENCES therapist (id),
	created_date TIMESTAMPTZ NOT NULL
);


CREATE TABLE IF NOT EXISTS event (
	id serial PRIMARY KEY,
	description VARCHAR(50),
	start_date TIMESTAMPTZ NOT NULL,
	end_date TIMESTAMPTZ NOT NULL,
	frequency INTEGER NOT NULL,
    price_per_session INTEGER NOT NULL,
    therapist_id INTEGER NOT NULL REFERENCES therapist (id),
    patient_id INTEGER NOT NULL REFERENCES patient (id),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_date TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS event_history (
	id serial PRIMARY KEY,
	event_id INTEGER NOT NULL REFERENCES event (id),
	description VARCHAR(50),
	date TIMESTAMPTZ NOT NULL,
    status VARCHAR(50) NOT NULL,
	paid BOOLEAN NOT NULL DEFAULT FALSE
);