-- CREATING AND SELECT DATABASE
CREATE DATABASE db_task;
\c db_task;
-- CREATING TABLES ASNF TYPES
CREATE TYPE TYPE_STATUS AS ENUM('Completed', 'In Progress', 'Pending');

DROP TABLE IF EXISTS roles;
CREATE TABLE IF NOT EXISTS roles (
	role_id SERIAL NOT NULL PRIMARY KEY,
	role_name VARCHAR(50) NOT NULL UNIQUE,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL NOT NULL PRIMARY KEY,
	user_name VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(150) NOT NULL,
	role_id INT NOT NULL,
	image VARCHAR(150),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_role_user FOREIGN KEY(role_id) REFERENCES roles(role_id)
);
DROP TABLE IF EXISTS tasks;
CREATE TABLE IF NOT EXISTS tasks (
	task_id SERIAL NOT NULL PRIMARY KEY,
	task_name VARCHAR(100) NOT NULL,
	description VARCHAR(200) NOT NULL,
	status TYPE_STATUS DEFAULT 'Pending',
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	user_id INT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_task_user FOREIGN KEY(user_id) REFERENCES users(user_id)
);
-- CREATING VIEW view_user_tasks
DROP VIEW IF EXISTS view_user_tasks;
CREATE VIEW view_user_tasks AS 
SELECT t.task_id, t.task_name,
	t.description, t.status,
	t.start_date, t.end_date,
	t.created_at, t.updated_at,
	u.user_id, u.user_name,
	r.role_name
FROM tasks t
JOIN users u ON(u.user_id = t.user_id)
JOIN roles r ON(r.role_id = u.role_id)
ORDER BY t.created_at DESC;

-- CREATING VIEW view_user_data
DROP VIEW IF EXISTS view_user_data;
CREATE VIEW view_user_data AS 
SELECT u.user_id, u.user_name,
	u.password, u.created_at, 
	u.updated_at, u.image, 
	r.role_id, r.role_name
FROM users u
JOIN roles r ON(r.role_id = u.role_id)
ORDER BY u.created_at DESC;

-- INSERTING DATA
INSERT INTO roles (role_name) VALUES ('administrator');
INSERT INTO roles (role_name) VALUES ('normal');
INSERT INTO users (user_name, password, role_id) VALUES ('admin01', 'sha256$Y6n9BV9QhGkoORIz$6200b3b9cf111f359846716ecd42122fac99808cd51cea6e135ba7fc0e7687f8', 1);
INSERT INTO users (user_name, password, role_id) VALUES ('admin02', 'sha256$Y6n9BV9QhGkoORIz$6200b3b9cf111f359846716ecd42122fac99808cd51cea6e135ba7fc0e7687f8', 1);
INSERT INTO users (user_name, password, role_id) VALUES ('user1', 'sha256$0NMAtO3uqwrB5HRz$933ecf05af2687e98348fed1dd2285ec1234e4b47b8fed8e8c575d7ea5e4644a', 2);
INSERT INTO users (user_name, password, role_id) VALUES ('user2', 'sha256$0NMAtO3uqwrB5HRz$933ecf05af2687e98348fed1dd2285ec1234e4b47b8fed8e8c575d7ea5e4644a', 2);
INSERT INTO users (user_name, password, role_id) VALUES ('user3', 'sha256$0NMAtO3uqwrB5HRz$933ecf05af2687e98348fed1dd2285ec1234e4b47b8fed8e8c575d7ea5e4644a', 2);
INSERT INTO users (user_name, password, role_id) VALUES ('user4', 'sha256$0NMAtO3uqwrB5HRz$933ecf05af2687e98348fed1dd2285ec1234e4b47b8fed8e8c575d7ea5e4644a', 2);
INSERT INTO tasks (task_name, description, start_date, end_date, user_id) VALUES ('Read a Book', 'Reading a programming book', '2022-12-18', '2023-02-04', 2);
INSERT INTO tasks (task_name, description, start_date, end_date, user_id) VALUES ('Make a Lunch', 'Reading a programming book', '2022-09-18', '2022-12-24', 3);
INSERT INTO tasks (task_name, description, start_date, end_date, user_id) VALUES ('Walk in the moon', 'Walking with my dog every day, at 6 AM', '2023-02-01', '2023-02-01', 4);
INSERT INTO tasks (task_name, description, start_date, end_date, user_id) VALUES ('Send an email', 'Send an email to recruites', '2023-01-18', '2023-01-18', 5);