export default function createReportObject(employeesList) {
  const repoObj = {
    allemployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return repoObj;
}
