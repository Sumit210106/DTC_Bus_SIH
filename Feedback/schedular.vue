<template>
    <div class="app">
      <!-- Header Section -->
      <header class="header" >
        <div class="logo">

          <!-- left the space for logo -->
          <span class="logo-text">add dtc logo </span>
        </div>
        <div class="header-right">

          <!-- Right-sided symbol symbol which was decided -->
          <span class="right-symbol"> add the symbol which was decided</span>

          <!-- Employee Info (name and employee ID) -->
          <div class="employee-info">
            <span class="employee-id">ID: {{ employeeId }}</span>
            <br/>
            <span class="employee-name">Name: {{ employeeName }}</span>
          </div>
        </div>
      </header>
  
      <!-- Main Content code i have written below  -->
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
          
        </div>
      </div>
  
      <!-- Footer Section --> 
       <!-- add more footer details i have currently left the space -->
      <footer class="footer">
        <div class="footer-links">
          <router-link to="/help.vue" class="footer-link">Help & Support</router-link>
          <p>&copy; &copy;2024 Byte Knightz</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script>

  export default {
    name: "Schedular",
    components:{
        // home,
        // CrewManager,
        // BusManager,
        // TimeTable
    },
    data() {
      return {
        // added my details ---- change it and make it dynamic and fetch the details from tables after login
        employeeId: "12345",
        employeeName: "sumit",
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
    position:absolute;
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
    transition: box-shadow 0.3s ease, transform 0.3s ease;
  }
  
  .content-box:hover {
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
    transform: translateY(-5px);
  }
  
  .content-box h2, .content-box h3 {
    color: #333;
  }
  
  .content-box p {
    font-size: 1rem;
    color: #666;
  }
  
  .content-box ul {
    list-style: none;
    padding: 0;
  }
  
  .content-box ul li {
    margin-bottom: 10px;
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