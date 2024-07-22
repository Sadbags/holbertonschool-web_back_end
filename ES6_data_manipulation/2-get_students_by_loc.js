export default function getStudentsByLocation() {
	return ListStudents.filter((students) => students.location === city);
}
