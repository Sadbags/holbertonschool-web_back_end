export default function getStudentsByLocation() {
	return getListStudents.filter((students) => students.location === city);
}
