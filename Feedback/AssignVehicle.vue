<template>
    <div class="app">
      <!-- Header Section -->
      <header class="header">
        <div class="logo">
          <span class="logo-text">DTC Bus Management</span>
        </div>
        <div class="header-right">
          <span class="right-symbol">Symbol</span>
          <div class="employee-info">
            <span class="employee-id">ID: {{ employeeId }}</span><br />
            <span class="employee-name">Name: {{ employeeName }}</span>
          </div>
        </div>
      </header>
  
      <!-- Taskbar Below Navbar -->
      <div class="taskbar">
        <router-link to="/" class="task-item">Home</router-link>
        <router-link to="/crewManager.vue" class="task-item">Crew Manager</router-link>
        <router-link to="/busManager.vue" class="task-item">Bus Manager</router-link>
        <router-link to="/timetable.vue" class="task-item">Timetable</router-link>
      </div>
  
      <!-- Main Content -->
      <div class="main-content">
        <!-- Welcome Section -->
        <div class="welcome-box">
          <h2>Welcome, {{ employeeName }}!</h2>
          <p>Manage buses and assignments for optimal route scheduling.</p>
        </div>
  
        <!-- Bus Table -->
        <div class="bus-table">
          <h3>Available Vehicles</h3>
          <table>
            <thead>
              <tr>
                <th>Vehicle No</th>
                <th>Bus Name</th>
                <th>Route No Assigned</th>
                <th>Source</th>
                <th>Destination</th>
                <th>Date/Time</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(bus, index) in buses" :key="index">
                <td>{{ bus.id }}</td>
                <td>{{ bus.name }}</td>
                <td>{{ bus.routeNo || 'None' }}</td>
                <td>{{ bus.source || 'N/A' }}</td>
                <td>{{ bus.destination || 'N/A' }}</td>
                <td>{{ bus.date || 'N/A' }}</td>
                <td :class="{'available': bus.available, 'assigned': !bus.available}">
                  {{ bus.available ? 'Available' : 'Assigned' }}
                </td>
                <td>
                  <button v-if="bus.available" @click="openAssignRoute(bus)">Assign Route</button>
                  <button v-else @click="openEditRoute(bus)">Edit</button>
                </td>
              </tr>
            </tbody>
          </table>
  
          <!-- Modal for Route Assignment -->
          <div v-if="showModal" class="modal-overlay">
            <div class="modal">
              <h3>{{ isEditMode ? 'Edit Route Assignment' : 'Assign Route to ' + selectedBus.name }}</h3>
              <label for="route">Select Route:</label>
              <select v-model="selectedRoute" @change="updateRouteDetails">
                <option value="NST">NST</option>
                <option value="YOUR_SPACE">YOUR SPACE</option>
                <option value="PHOENIX">PHOENIX</option>
                <option value="PUNE_CITY">PUNE CITY</option>
              </select>
  
              <label for="source">Source:</label>
              <input type="text" v-model="source" />
  
              <label for="destination">Destination:</label>
              <input type="text" v-model="destination" />
  
              <label for="date">Date/Time:</label>
              <select v-model="selectedTime" :disabled="!availableTimes.length">
                <option v-for="(time, index) in availableTimes" :key="index" :value="time">{{ time }}</option>
              </select>
              <p v-if="!availableTimes.length">No available time slots</p>
  
              <div class="actions">
                <button @click="assignRoute">{{ isEditMode ? 'Update Assignment' : 'Assign Route' }}</button>
                <button @click="closeModal">Cancel</button>
              </div>
            </div>
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
    name: "BusTable",
    data() {
      return {
        buses: [
          { id: "V101", name: "Bus 1", available: true },
          { id: "V102", name: "Bus 2", available: true },
          { id: "V103", name: "Bus 3", available: false, routeNo: "PUNE_CITY", source: "B", destination: "C", date: "2024-11-25", time: "10:00 AM" }
        ],
        showModal: false,
        selectedBus: null,
        selectedRoute: "",
        source: "",
        destination: "",
        selectedTime: "",
        availableTimes: ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM"],
        isEditMode: false,
        employeeId: "12345",
        employeeName: "Sumit"
      };
    },
    methods: {
      openAssignRoute(bus) {
        this.selectedBus = bus;
        this.showModal = true;
        this.isEditMode = false;
        this.selectedRoute = "";
        this.source = "";
        this.destination = "";
        this.selectedTime = "";
        this.updateRouteDetails();
      },
      openEditRoute(bus) {
        this.selectedBus = bus;
        this.showModal = true;
        this.isEditMode = true;
        this.selectedRoute = bus.routeNo;
        this.source = bus.source;
        this.destination = bus.destination;
        this.selectedTime = bus.time;
        this.updateRouteDetails();
      },
      closeModal() {
        this.showModal = false;
      },
      assignRoute() {
        if (this.selectedBus && this.selectedRoute && this.selectedTime) {
          this.selectedBus.routeNo = this.selectedRoute;
          this.selectedBus.source = this.source;
          this.selectedBus.destination = this.destination;
          this.selectedBus.date = new Date().toLocaleDateString();
          this.selectedBus.time = this.selectedTime;
          this.selectedBus.available = false;
          this.availableTimes = this.availableTimes.filter(time => time !== this.selectedTime);
        }
        this.closeModal();
      },
      updateRouteDetails() {
        if (this.selectedRoute === "NST") {
          this.source = "A";
          this.destination = "B";
        } else if (this.selectedRoute === "YOUR_SPACE") {
          this.source = "B";
          this.destination = "C";
        } else if (this.selectedRoute === "PHOENIX") {
          this.source = "C";
          this.destination = "D";
        } else if (this.selectedRoute === "PUNE_CITY") {
          this.source = "D";
          this.destination = "E";
        }
        if (this.selectedBus && this.selectedBus.time) {
          this.availableTimes = this.availableTimes.filter(time => time !== this.selectedBus.time);
        }
      }
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
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  header {
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
  }
  
  .header-right {
    display: flex;
    align-items: center;
  }
  
  .employee-info {
    text-align: right;
  }
  
  .employee-id,
  .employee-name {
    font-size: 1rem;
  }
  
  /* Taskbar */
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
    text-decoration: none;
    color: #333;
    padding: 10px;
    margin-bottom: 10px;
    display: block;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
  }
  
  .task-item:hover {
    background-color: #f1a7b1;
  }
  
  .main-content {
    flex-grow: 1;
    padding: 20px;
  }
  
  .welcome-box {
    text-align: center;
    margin-bottom: 30px;
    background-color: #ffb6c1;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .welcome-box h2 {
    font-size: 2rem;
    font-weight: bold;
  }
  
  .welcome-box p {
    font-size: 1.2rem;
  }
  
  .bus-table {
    margin-top: 20px;
  }
  
  .bus-table h3 {
    font-size: 1.8rem;
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    background-color: white;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  th,
  td {
    padding: 10px;
    text-align: center;
    border: 1px solid #ddd;
  }
  
  th {
    background-color: #f1a7b1;
  }
  
  td {
    background-color: #f9f9f9;
  }
  
  td.available {
    color: green;
  }
  
  td.assigned {
    color: blue;
  }
  
  button {
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    background-color: #ff6b81;
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #ff3b5c;
  }
  
  /* Modal Styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 400px;
  }
  
  .modal h3 {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin: 10px 0 5px;
  }
  
  input,
  select {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  button {
    margin-right: 10px;
  }
  
  /* Footer Section */
  footer {
    background-color: #ff6b81;
    color: white;
    padding: 15px 0;
    text-align: center;
    margin-top: auto;
  }
  
  .footer-links {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  .footer-link {
    text-decoration: none;
    color: white;
    font-size: 16px;
  }
  
  .footer-link:hover {
    text-decoration: underline;
  }
  </style>
  