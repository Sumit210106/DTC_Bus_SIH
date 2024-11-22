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
          <router-link to="/" class="task-item">Home</router-link>
          <router-link to="/crewManager.vue" class="task-item">Crew Manager</router-link>
          <router-link to="/busManager.vue" class="task-item">Bus Manager</router-link>
          <router-link to="/timetable.vue" class="task-item">Timetable</router-link>
        </div>
  
        <!-- Page Content -->
        <div class="page-body">
          <div class="content-box">
            <h2>Welcome, {{ employeeName }}!</h2>
          </div>
  
          <!-- Crew Management Table -->
          <div class="crew-management">
            <h3>Manage Crew</h3>
  
            <!-- Filter Dropdown -->
            <div class="filter-dropdown">
              <label for="availability">Filter by Availability:</label>
              <select v-model="availabilityFilter" @change="filterCrew">
                <option value="all">All</option>
                <option value="available">Available</option>
                <option value="not-available">Not Available</option>
              </select>
            </div>
  
            <!-- Crew Table -->
            <table>
              <thead>
                <tr>
                  <th>Employee ID</th>
                  <th>Name</th>
                  <th>Crew Type</th>
                  <th>Status</th>
                  <th>Remaining Working Hours</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="crew in filteredCrewList" :key="crew.id">
                  <td>{{ crew.employeeId }}</td>
                  <td>{{ crew.name }}</td>
                  <td>{{ crew.crewType }}</td>
                  <td :class="{'available': crew.status === 'Available', 'not-available': crew.status === 'Not Available'}">
                    {{ crew.status }}
                  </td>
                  <td>{{ crew.remainingHours }} hours</td>
                  <td>
                    <button @click="editCrew(crew)">Edit</button>
                    <button @click="deleteCrew(crew.id)">Delete</button>
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
    name: "Schedular",
    data() {
      return {
        employeeId: "12345",
        employeeName: "Sumit",
        availabilityFilter: "all", // filter options: all, available, not-available
        crewList: [
          { id: 1, employeeId: "001", name: "sumit", crewType: "Driver", status: "Available", remainingHours: 40 },
          { id: 2, employeeId: "002", name: "oats", crewType: "Conductor", status: "Not Available", remainingHours: 30 },
          { id: 3, employeeId: "003", name: "roni", crewType: "Driver", status: "Available", remainingHours: 35 },
          { id: 4, employeeId: "004", name: "deep", crewType: "Conductor", status: "Not Available", remainingHours: 25 },
          { id: 5, employeeId: "005", name: "yuvraj", crewType: "Conductor", status: "Available", remainingHours: 29 },
          { id: 6, employeeId: "006", name: "arohi", crewType: "driver", status: "Not Available", remainingHours: 32 },
          // Add more crew members as needed
        ],
        filteredCrewList: [] // Store the filtered crew list
      };
    },
    watch: {
      // Watch for changes to availabilityFilter and update filteredCrewList
      availabilityFilter() {
        this.filterCrew();
      }
    },
    methods: {
      // Filter crew list based on the selected filter
      filterCrew() {
        if (this.availabilityFilter === "all") {
          this.filteredCrewList = this.crewList;
        } else {
          this.filteredCrewList = this.crewList.filter(crew => crew.status.toLowerCase() === this.availabilityFilter);
        }
      },
      editCrew(crew) {
        console.log("Editing crew:", crew);
        // Add your edit logic here (e.g., show a modal to update crew details)
      },
      deleteCrew(crewId) {
        this.crewList = this.crewList.filter(crew => crew.id !== crewId);
        this.filterCrew(); // Reapply the filter after deletion
        console.log("Deleted crew with ID:", crewId);
      }
    },
    mounted() {
      this.filterCrew(); // Initialize the filtered list on mount
    }
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
  
  /* Content Area */
  .page-body {
    margin-left: 240px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .content-box {
    background-color: #fff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .content-box h2,
  .content-box h3 {
    color: #333;
  }
  
  .content-box p {
    font-size: 1rem;
    color: #666;
  }
  
  /* Crew Management Table */
  .crew-management table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .crew-management th,
  .crew-management td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd;
  }
  
  .crew-management button {
    background-color: #f1b6c0;
    border: none;
    border-radius: 5px;
    padding: 5px 10px;
    cursor: pointer;
  }
  
  .crew-management button:hover {
    background-color: #e0a0b4;
  }
  
  /* Filter Dropdown */
  .filter-dropdown {
    margin-bottom: 20px;
  }
  
  .filter-dropdown label {
    font-size: 1rem;
    margin-right: 10px;
  }
  
  .filter-dropdown select {
    padding: 8px;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .available {
    color: green;
  }
  
  .not-available {
    color: red;
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
  