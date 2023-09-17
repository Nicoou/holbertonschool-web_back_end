export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartaments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
}
