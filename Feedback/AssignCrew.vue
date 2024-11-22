<template>
    <div class="assign-crew">
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
          <router-link to="/schedular.vue" class="task-item">Home</router-link>
          <router-link to="/crewManager.vue" class="task-item">Crew Manager</router-link>
          <router-link to="/busManager.vue" class="task-item">Bus Manager</router-link>
          <router-link to="/timetable.vue" class="task-item">Timetable</router-link>
        </div>
  
        <!-- Page Content -->
        <div class="page-body">
          <h1 class="page-body-head">Assign Crew</h1>
  
          <!-- Crew Assignment Form -->
          <div class="assignment-form">
            <h3>Select Driver</h3>
            <select v-model="selectedDriver" class="select-input">
              <option v-for="driver in drivers" :key="driver.id" :value="driver.id">
                {{ driver.name }} (ID: {{ driver.id }})
              </option>
            </select>
  
            <h3>Select Conductor</h3>
            <select v-model="selectedConductor" class="select-input">
              <option v-for="conductor in conductors" :key="conductor.id" :value="conductor.id">
                {{ conductor.name }} (ID: {{ conductor.id }})
              </option>
            </select>
  
            <h3>Select Bus</h3>
            <select v-model="selectedBus" class="select-input">
              <option v-for="bus in buses" :key="bus.id" :value="bus.id">
                {{ bus.busNumber }} (ID: {{ bus.id }})
              </option>
            </select>
  
            <h3>Select Schedule</h3>
            <input type="datetime-local" v-model="selectedSchedule" class="select-input" />
  
            <button @click="assignCrew" class="btn-assign">Assign Crew</button>
          </div>
  
          <!-- Current Assignments Table -->
          <div class="assignments-table">
            <h3>Current Crew Assignments</h3>
            <table>
              <thead>
                <tr>
                  <th>Driver Name</th>
                  <th>Conductor Name</th>
                  <th>Bus Number</th>
                  <th>Schedule</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="assignment in assignments" :key="assignment.id">
                  <td>{{ assignment.driverName }}</td>
                  <td>{{ assignment.conductorName }}</td>
                  <td>{{ assignment.busNumber }}</td>
                  <td>{{ assignment.schedule }}</td>
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
    name: "AssignCrew",
    data() {
      return {
        employeeId: "12345",
        employeeName: "Sumit",
        drivers: [
          { id: 1, name: "Roni" },
          { id: 2, name: "Sumit" },
          { id: 3, name: "Mandal" },
        ],
        conductors: [
          { id: 1, name: "Deep" },
          { id: 2, name: "Oats" },
          { id: 3, name: "Arohi" },
        ],
        buses: [
          { id: 1, busNumber: "Bus 101" },
          { id: 2, busNumber: "Bus 102" },
          { id: 3, busNumber: "Bus 103" },
        ],
        assignments: [
          { id: 1, driverName: "Sumit", conductorName: "Deep", busNumber: "Bus 101", schedule: "2024-11-22 10:00" },
          { id: 2, driverName: "Oats", conductorName: "", busNumber: "Bus 102", schedule: "2024-11-22 12:00" },
        ],
        selectedDriver: null,
        selectedConductor: null,
        selectedBus: null,
        selectedSchedule: null,
      };
    },
    methods: {
      assignCrew() {
        if (this.selectedDriver && this.selectedConductor && this.selectedBus && this.selectedSchedule) {
          const newAssignment = {
            id: this.assignments.length + 1,
            driverName: this.drivers.find(driver => driver.id === this.selectedDriver).name,
            conductorName: this.conductors.find(conductor => conductor.id === this.selectedConductor).name,
            busNumber: this.buses.find(bus => bus.id === this.selectedBus).busNumber,
            schedule: this.selectedSchedule,
          };
          this.assignments.push(newAssignment);
          this.selectedDriver = null;
          this.selectedConductor = null;
          this.selectedBus = null;
          this.selectedSchedule = null;
        } else {
          alert("Please select all fields before assigning.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .page-body-head {
    text-align: center;
    padding: 20px;
  }
  
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
  
  /* Crew Assignment Form */
  .assignment-form {
    margin-left: 240px;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 60%;
  }
  
  h3 {
    margin-bottom: 10px;
  }
  
  .select-input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 8px;
    border: 1px solid #ddd;
  }
  
  .btn-assign {
    padding: 10px 20px;
    background-color: #d0596d;
    color: #fff;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.2rem;
  }
  
  .btn-assign:hover {
    background-color: #c04e59;
  }
  
  /* Current Assignments Table */
  .assignments-table {
    margin-left: 240px;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  table th, table td {
    padding: 12px;
    text-align: left;
    border: 1px solid #ddd;
  }
  
  table th {
    background-color: #f1f1f1;
  }
  
  table tr:nth-child(even) {
    background-color: #f9f9f9;
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