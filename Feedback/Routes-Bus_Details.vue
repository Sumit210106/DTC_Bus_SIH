<template>
  <div class="app">
    <!-- Header Section -->
    <header class="header">
      <div class="logo">
        <!-- left the space for logo -->
        <span class="logo-text">add dtc logo</span>
      </div>
      <div class="header-right">
        <!-- Right-sided symbol -->
        <span class="right-symbol">add the symbol which was decided</span>

        <!-- Employee Info (name and employee ID) -->
        <div class="employee-info">
          <span class="employee-id">ID: {{ employeeId }}</span>
          <br />
          <span class="employee-name">Name: {{ employeeName }}</span>
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
          <h2>Welcome, {{ employeeName }}!</h2>
        </div>

        <!-- Bus Routes Table -->
        <div class="bus-routes">
          <h3>Bus Route Details</h3>

          <!-- Table -->
          <table>
            <thead>
              <tr>
                <th>S.No</th>
                <th>Bus Route No</th>
                <th>Source</th>
                <th>Destination</th>
                <th>Stops</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(route, index) in busRoutes" :key="route.busRouteNo">
                <td>{{ index + 1 }}</td>
                <td>{{ route.busRouteNo }}</td>
                <td>{{ route.source }}</td>
                <td>{{ route.destination }}</td>
                <td>
                  <!-- Using ordered list for numbered bullets -->
                  <ol>
                    <li v-for="(stop, idx) in route.stops" :key="idx">{{ stop }}</li>
                  </ol>
                </td>
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
  name: "RoutesBus_Details",
  data() {
    return {
      // Sample employee data (to be dynamically fetched after login)
      employeeId: "12345",
      employeeName: "Sumit",
      
      // Bus routes data
      busRoutes: [
        {
          busRouteNo: "GL90",
          source: "Kendriya Terminal",
          destination: "Rohini Sector 16",
          stops: [
            "Regal", "New Delhi Railway Station", "Police Station Paharganj", "D.B. Gupta Market", 
            "Sarai Rohilla / Anand Parvat", "Zakhira", "Punjabi Bagh", "Wazirpur Depot", 
            "Pitampura K.D. Block", "Rohini Sector 7/8 X-ing", "Vidya Vihar", "Rohini Sector 15 Pocket-D2", 
            "Rohini Sector 11", "Rohini Sector 16"
          ]
        },
        {
          busRouteNo: "100",
          source: "Kendriya Terminal",
          destination: "Adarsh Nagar",
          stops: [
            "Kendriya Terminal", "Regal", "Shivaji Stadium", "Chitra Gupta Road", "Master Prithvi Nath Marg / Faiz Road", 
            "Ice Factory", "Malka Ganj", "Maurice Nagar", "G.T.B. Nagar", "Model Town II", "Adarsh Nagar"
          ]
        },
        {
          busRouteNo: "101",
          source: "Nizamuddin Railway Station",
          destination: "Swaroop Nagar JJ Colony GT Road",
          stops: [
            "Nizamuddin Railway Station", "Police Station Nizamuddin", "Golf Club / Sunder Nagar", "Supreme Court", 
            "Delhi Gate", "Red Fort", "ISBT / Kashmiri Gate", "Old Secretariat", "G.T.B. Nagar", "Model Town II", 
            "Adarsh Nagar", "Jahangir Puri", "Durga Chowk", "Shraddhanand Colony", "Swaroop Nagar JJ Colony GT Road"
          ]
        },
        {
          busRouteNo: "102",
          source: "Old Delhi Railway Station",
          destination: "Rohini Sector 22 (Lakhi Ram Park)",
          stops: [
            "Old Delhi Railway Station", "Mori Gate", "Ice Factory", "Malka Ganj", "R.P. Bagh", "Bara Bagh", 
            "Ashok Vihar X-ing", "Wazirpur Depot", "Pitampura J.D. Block", "Rohini Sector 7/8 X-ing", "Rohini Sector 6", 
            "Rohini Sector 24 Nallah / Rohini Sector 24 Gas Pla", "Rohini Sector 25 (Deep Vihar)", "Rohini Sector 23", 
            "Rohini Sector 20 JJ Colony", "Rohini Sector 22 (Lakhi Ram Park)"
          ]
        }
      ]
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
  margin-bottom: 80px; /* Allow space for footer */
}

/* Taskbar Below Navbar */
.taskbar {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 100px; /* Position the taskbar below the navbar */
  left: 20px;
  width: 200px; /* Increased width for bigger boxes */
  background-color: #f8d0d6; /* Light pink */
  padding: 20px 15px;
  border-radius: 12px; /* Rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.task-item {
  color: #333;
  text-decoration: none;
  padding: 40px 20px; /* Increased padding for bigger buttons */
  text-align: center;
  font-size: 1.3rem;
  margin-bottom: 15px;
  border-radius: 10px; /* Rounded corners */
  background-color: #fff; /* White background for each box */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for boxes */
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s ease;
}

.task-item:hover {
  background-color: #d0596d;
  color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
}

.page-body {
  flex: 1;
  padding-left: 240px; /* Space for taskbar */
}

.content-box {
  margin-bottom: 40px;
}

.content-box h2 {
  font-size: 2rem;
  font-weight: 600;
  color: #333;
}

/* Bus Routes Table */
.bus-routes table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.bus-routes th,
.bus-routes td {
  padding: 15px;
  text-align: left;
  border: 1px solid #ddd;
}

.bus-routes th {
  background-color: #f1b6c0;
}

.bus-routes tbody tr:hover {
  background-color: #f1f1f1;
}

/* Ordered List Styling */
ol {
  padding-left: 20px;
}

ol li {
  margin-bottom: 5px;
}

/* Footer */
.footer {
  background-color: #f1b6c0;
  color: #333;
  padding: 15px;
  text-align: center;
  position: relative;
  width: 100%;
  bottom: 0;
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
