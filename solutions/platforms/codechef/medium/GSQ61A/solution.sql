/* Write a query to join the table 'student' and 'course' using 'Course_id' to match both the tables and output the joined table. */

SELECT * FROM student JOIN course on  student.course_ID = course.course_id;