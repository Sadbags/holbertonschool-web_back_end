export default function getListStudentIds() {
	try {
		return getListStudentIds.map((l) => l.id);
	} catch (error) {
		return [];
	}
}
