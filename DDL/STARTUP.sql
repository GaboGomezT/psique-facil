CREATE TABLE IF NOT EXISTS events (
	id serial PRIMARY KEY,
	description VARCHAR(50),
	start_date TIMESTAMPTZ NOT NULL,
	end_date TIMESTAMPTZ NOT NULL,
	frequency INTEGER NOT NULL,
	organization_id INTEGER,
    therapist_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);