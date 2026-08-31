/* Write the queries to do the following:
 - JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table.
 - RIGHT JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table. */
 
 
 
 SELECT * FROM student s JOIN course c on s.Course_id=c.Course_id;
 
 SELECT * FROM student s RIGHT JOIN course c on s.Course_id=c.Course_id;