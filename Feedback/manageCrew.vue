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
        <div class="taskbar">
          <router-link to="/" class="task-item">Home</router-link>
          <router-link to="/crewManager.vue" class="task-item">Crew Manager</router-link>
          <router-link to="/busManager.vue" class="task-item">Bus Manager</router-link>
          <router-link to="/timetable.vue" class="task-item">Timetable</router-link>
        </div>
  
        <div class="page-body">
          <div class="content-box">
            <h2>Welcome, {{ employeeName }}!</h2>
          </div>
  
          <!-- Crew Management Table -->
          <div class="crew-management">
            <h3>Manage Crew</h3>
            <table>
                <thead>
                <tr>
                    <th>Employee ID</th>
                    <th>Name</th>
                    <th>Work Hours</th>
                    <th>Rest Hours</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="crew in crewList" :key="crew.id" @click="selectCrew(crew)">
                    <td>{{ crew.employeeId }}</td>
                    <td>{{ crew.name }}</td>
                    <td>{{ crew.workHours }}</td>
                    <td>{{ crew.restHours }}</td>
                    <td>
                    <button @click.stop="editCrew(crew)">Edit</button>
                    <button @click.stop="deleteCrew(crew.id)">Delete</button>
                    </td>
                </tr>
                </tbody>
            </table>
            </div>
  
          <!-- Edit Crew Modal (optional) -->
          <div v-if="isEditing" class="modal">
            <div class="modal-content">
              <h4>Edit Crew Details</h4>
              <form @submit.prevent="updateCrew">
                <div>
                  <label for="crewName">Name:</label>
                  <input type="text" v-model="currentCrew.name" id="crewName" />
                </div>
                <div>
                  <label for="workHours">Work Hours:</label>
                  <input type="number" v-model="currentCrew.workHours" id="workHours" />
                </div>
                <div>
                  <label for="restHours">Rest Hours:</label>
                  <input type="number" v-model="currentCrew.restHours" id="restHours" />
                </div>
                <button type="submit">Save Changes</button>
                <button @click="isEditing = false">Cancel</button>
              </form>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Footer Section -->
      <footer class="footer">
        <div class="footer-links">
          <router-link to="/help.vue" class="footer-link">Help & Support</router-link>
          <p>&copy;2024 Byte Knightz</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: "Manager",
    data() {
      return {
        employeeId: "12345", // This should be dynamically fetched after login
        employeeName: "Sumit", // This should be dynamically fetched after login
        crewList: [
          { id: 1, employeeId: "1001", name: "John Doe", workHours: 160, restHours: 40 },
          { id: 2, employeeId: "1002", name: "Jane Smith", workHours: 150, restHours: 50 },
          { id: 3, employeeId: "1003", name: "Samuel Lee", workHours: 170, restHours: 30 },
        ],
        isEditing: false,
        currentCrew: {},
      };
    },
    methods: {
      // Select a crew member to edit
      selectCrew(crew) {
        this.currentCrew = { ...crew };
        this.isEditing = true;
      },
  
      // Edit the crew details
      editCrew(crew) {
        this.selectCrew(crew);
      },
  
      // Update the crew details after edit
      updateCrew() {
        const index = this.crewList.findIndex((crew) => crew.id === this.currentCrew.id);
        if (index !== -1) {
          this.$set(this.crewList, index, { ...this.currentCrew });
          this.isEditing = false;
        }
      },
  
      // Delete a crew member
      deleteCrew(crewId) {
        const index = this.crewList.findIndex((crew) => crew.id === crewId);
        if (index !== -1) {
          this.crewList.splice(index, 1);
        }
      },
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
  
  .content-box:hover {
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
  }
  
  .crew-management table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .crew-management th, .crew-management td {
    padding: 12px;
    text-align: left;
    border: 1px solid #ddd;
  }
  
  .crew-management button {
    margin-right: 10px;
    padding: 6px 12px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .crew-management button:hover {
    background-color: #e0e0e0;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    width: 300px;
  }
  
  .modal-content input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
  }
  
  .modal-content button {
    width: 100%;
    padding: 10px;
    background-color: #f1b6c0;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .modal-content button:hover {
    background-color: #e0a0b4;
  }
  
  .footer {
    background-color: #f1b6c0;
    color: #333;
    padding: 15px;
    text-align: center;
  }
  
  .footer-links {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  .footer-link {
    color: #333;
    text-decoration: none;
  }
  
  .footer-link:hover {
    text-decoration: underline;
  }
  </style>