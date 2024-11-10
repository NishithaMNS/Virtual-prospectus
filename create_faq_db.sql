-- Create the database
CREATE DATABASE IF NOT EXISTS college_responses;

-- Switch to the database
USE college_responses;

-- Create the FAQ table
CREATE TABLE IF NOT EXISTS faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    keywords TEXT NOT NULL,
    answer TEXT NOT NULL
);

-- Insert some sample data into the FAQ table
INSERT INTO faq (question, keywords, answer) VALUES
('Who is the principal?', 'principal,name of principal,who is principal', 'Dr. A. Sai Hanuman'),
('What courses are offered?', 'courses,offered,departments', 'CSE and IT'),
('What is the vision of the college?', 'vision,college vision,what is the vision', 'To be a globally recognized institution providing quality education'),
('What is the mission of the college?', 'mission,college mission,what is the mission', 'To impart knowledge and skills that foster holistic development'),
('What are the admission requirements?', 'admission,requirements,eligibility,how to apply', 'Visit the admissions section of the website for detailed information'),
('What is the college\'s address?', 'address,college location,where is the college', 'GLWEC is located at 123 College Road, City Name'),
('What are the contact details for the administration?', 'contact,administration,phone,email', 'You can reach us at admin@glwec.edu or call 123-456-7890'),
('What departments are available at GLWEC?', 'departments,programs,offered departments', 'CSE, IT, ECE, Civil, Mechanical'),
('What is the fee structure?', 'fees,fee structure,tuition fees', 'Visit the fees section of the website for detailed information'),
('Is hostel accommodation available?', 'hostel,accommodation,available,stay', 'Yes, we have hostel facilities for both male and female students');
