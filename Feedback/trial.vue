<template>
    <div class="home">
      <header class="header">
        <h1>Bus Portal</h1>
        <nav>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#routes">Routes</a></li>
            <li><a href="#bookings">Bookings</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </header>
      <main class="main-content">
        <section class="hero">
          <h2>Find Your Bus</h2>
          <form @submit.prevent="searchBuses">
            <input type="text" v-model="searchTerm" placeholder="Enter destination" />
            <button type="submit">Search</button>
          </form>
        </section>
        <section class="bus-list">
          <h3>Available Buses</h3>
          <div v-if="buses.length === 0" class="no-buses">No buses available.</div>
          <div v-for="bus in buses" :key="bus.id" class="bus-item">
            <h4>{{ bus.name }}</h4>
            <p>Departure: {{ bus.departure }}</p>
            <p>Arrival: {{ bus.arrival }}</p>
            <button @click="bookBus(bus.id)">Book Now</button>
          </div>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; 2024 BYTE KNIGHTZ. All rights reserved.</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchTerm: '',
        buses: [
          { id: 1, name: 'Mehrauli', departure: '10:00 AM', arrival: '12:00 PM' },
          { id: 2, name: 'Railway station', departure: '1:00 PM', arrival: '3:00 PM' },
          { id: 3, name: 'India gate', departure: '8:00 PM', arrival: '10:00 PM' }
        ]
      };
    },
    methods: {
      searchBuses() {
        
        this.buses = this.buses.filter(bus => bus.name.toLowerCase().includes(this.searchTerm.toLowerCase()));
      },
      bookBus(busId) {
        alert(`Bus ${busId} booked!`);
      }
    }
  };
  </script>
  
  <style>
  .home {
    font-family: Arial, sans-serif;
    text-align: center;
  }
  .header {
    background-color: #4CAF50;
    color: white;
    padding: 10px 0;
  }
  .header nav ul {
    list-style: none;
    padding: 0;
  }
  .header nav ul li {
    display: inline;
    margin: 0 15px;
  }
  .header nav ul li a {
    color: white;
    text-decoration: none;
  }
  .main-content {
    padding: 20px;
  }
  .hero {
    background-color: #f2f2f2;
    padding: 20px;
  }
  .bus-list {
    margin-top: 20px;
  }
  .bus-item {
    border: 1px solid #ccc;
    margin: 10px 0;
    padding: 10px;
  }
  .footer {
    background-color: #4CAF50;
    color: white;
    padding: 10px 0;
    position: absolute;
    bottom: 0;
    width: 100%;
  }
  .no-buses {
    color: red;
  }
  </style>