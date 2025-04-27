
-- Üyeler (Members) Tablosu
CREATE TABLE Members (
    member_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Eğitimler (Courses) Tablosu
CREATE TABLE Courses (
    course_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    instructor VARCHAR(100) NOT NULL,
    category_id SMALLINT NOT NULL
);

-- Kategoriler (Categories) Tablosu
CREATE TABLE Categories (
    category_id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category_name VARCHAR(100) NOT NULL
);

-- Eğitimler Tablosuna FK eklenmesi
ALTER TABLE Courses ADD CONSTRAINT fk_courses_category
FOREIGN KEY (category_id) REFERENCES Categories(category_id);

-- Katılımlar (Enrollments) Tablosu
CREATE TABLE Enrollments (
    enrollment_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    member_id BIGINT NOT NULL,
    course_id BIGINT NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_enrollments_member FOREIGN KEY (member_id) REFERENCES Members(member_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Sertifikalar (Certificates) Tablosu
CREATE TABLE Certificates (
    certificate_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    certificate_code VARCHAR(100) UNIQUE NOT NULL,
    issue_date DATE NOT NULL
);

-- Sertifika Atamaları (CertificateAssignments) Tablosu
CREATE TABLE CertificateAssignments (
    assignment_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    member_id BIGINT NOT NULL,
    certificate_id BIGINT NOT NULL,
    assignment_date DATE NOT NULL,
    CONSTRAINT fk_assignments_member FOREIGN KEY (member_id) REFERENCES Members(member_id),
    CONSTRAINT fk_assignments_certificate FOREIGN KEY (certificate_id) REFERENCES Certificates(certificate_id)
);

-- Blog Gönderileri (BlogPosts) Tablosu
CREATE TABLE BlogPosts (
    post_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    published_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id BIGINT NOT NULL,
    CONSTRAINT fk_blogposts_author FOREIGN KEY (author_id) REFERENCES Members(member_id)
);
