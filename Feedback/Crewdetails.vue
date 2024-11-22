<template>
  <div class="app">
    <!-- Header Section -->
    <header class="header">
      <div class="logo">
        <span class="logo-text">add dtc logo</span>
      </div>
      <div class="header-right">
        <span class="right-symbol">add the symbol which was decided</span>
        <div class="employee-info">
          <span class="employee-id">ID: {{ id }}</span>
          <br />
          <span class="employee-name">Name: {{ name }}</span>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Taskbar Below Navbar -->
      <div class="taskbar">
        <router-link to="/schedular.vue" class="task-item">Home</router-link>
        <router-link to="/crewManager.vue" class="task-item">Crew Manager</router-link>
        <router-link to="/busManager.vue" class="task-item">Bus Manager</router-link>
        <router-link to="/timetable.vue" class="task-item">Timetable</router-link>
      </div>

      <!-- Page Content -->
      <div class="page-body">
        <div class="content-box">
          <!-- Welcome Section -->
          <h2>Welcome, {{ name }}!</h2>
        </div>

        <!-- Crew Details Table -->
        <div class="crew-table">
          <h3>Crew Details</h3>
          <table>
            <thead>
              <tr>
                <th>Employee Name</th>
                <th>Employee ID</th>
                <th>Bus Route No.</th>
                <th>Vehicle No. Assigned</th>
                <th>Sign In</th>
                <th>Sign Off</th>
                <th>Source</th>
                <th>Destination</th>
                <th>Hours Worked</th>
                <th>Status</th>
                <th>Crew Type</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(crew, index) in crewDetails" :key="index">
                <td>{{ crew.name }}</td>
                <td>{{ crew.id }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.routeNo }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.vehicleNo }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.signIn }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.signOff }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.source }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.destination }}</td>
                <td>{{ crew.status === 'Not Assigned' ? '---' : crew.hoursWorked }}</td>
                <td>
                  <span :class="{'assigned': crew.status === 'Assigned', 'not-assigned': crew.status === 'Not Assigned'}">
                    {{ crew.status }}
                  </span>
                </td>
                <!-- Show Crew Type for all rows, even if 'Not Assigned' -->
                <td>{{ crew.status === 'Not Assigned' ? crew.crewType : crew.crewType }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Footer Section -->
    <footer class="footer">
      <div class="footer-links">
        <router-link to="/help.vue" class="footer-link">Help & Support</router-link>
        <p>&copy; 2024 Byte Knightz</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Crewdetails",
  data() {
    return {
      // Example of logged-in employee data (this should be fetched dynamically after login)
      id: "12345",
      name: "Sumit",
      // Example of crew details
      crewDetails: [
        {
          name: "Sumit",
          id: "12345",
          routeNo: "101",
          vehicleNo: "XYZ1234",
          signIn: "08:00 AM",
          signOff: "05:00 PM",
          source: "YOUR SPACE",
          destination: "NST ",
          status: "Assigned", // Assigned or Not Assigned
          crewType: "Driver", // Crew type (Driver/Conductor)
          hoursWorked: "9 hours", // Example worked hours
        },
        {
          name: "Oats",
          id: "12346",
          routeNo: "B202",
          vehicleNo: "ABC5678",
          signIn: "09:00 AM",
          signOff: "06:00 PM",
          source: "ULC",
          destination: "NST ",
          status: "Not Assigned", // Not assigned
          crewType: "Conductor",
          hoursWorked: "---", // No hours worked
        },
        // More crew members can be added dynamically
      ],
    };
  },
};
</script>

<style scoped>
/* Global Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  padding: 15px 25px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.logo-text {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.header-right {
  display: flex;
  align-items: center;
}

.right-symbol {
  font-size: 1.5rem;
  margin-right: 15px;
}

.employee-info {
  text-align: right;
}

.employee-id {
  font-size: 0.9rem;
}

.employee-name {
  font-size: 1rem;
  font-weight: bold;
}

/* Main Content */
.main-content {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 20px;
}

/* Taskbar Below Navbar */
.taskbar {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 100px;
  left: 20px;
  width: 200px;
  background-color: #f8d0d6;
  padding: 20px 15px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.task-item {
  color: #333;
  text-decoration: none;
  padding: 40px 20px;
  text-align: center;
  font-size: 1.3rem;
  margin-bottom: 15px;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s ease;
}

.task-item:hover {
  background-color: #d0596d;
  color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Page Content */
.page-body {
  padding-left: 240px;
  padding-top: 20px;
}

/* Crew Table */
.crew-table {
  background-color: #fff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.crew-table table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.crew-table th,
.crew-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.crew-table th {
  background-color: #f1b6c0;
  color: #333;
  font-weight: bold;
}

.crew-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.crew-table td {
  font-size: 0.95rem;
  color: #555;
}

.crew-table td span.assigned {
  color: green;
}

.crew-table td span.not-assigned {
  color: red;
}

.crew-table td:last-child {
  font-weight: bold;
}

/* Footer */
.footer {
  background-color: #f1b6c0;
  color: #333;
  padding: 15px;
  text-align: center;
  position: end;
  bottom: 0;
  width: 100%;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.footer-link {
  color: #333;
  text-decoration: none;
  font-size: 1rem;
  transition: text-decoration 0.3s;
}

.footer-link:hover {
  text-decoration: underline;
}
</style>
