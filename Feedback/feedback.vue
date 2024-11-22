<template>
    <div class="container">
      <div class="header">
        <div class="logo-placeholder">
          <!-- DTC LOGO WOULD BE ADDED HERE  -->
          <h2>LOGO PLACEHOLDER</h2>
        </div>
        <h1>HELP US GET BETTER</h1>
        <p class="intro">Have some suggestions? Share with us your thoughts!</p>
        <p class="subtext">Fill in the details so that we can serve you better.</p>
      </div>
  
      <!-- hello greeting is added  -->

    <h2 v-if="name">HELLO, {{ name }}!</h2>
  
      <form @submit.prevent="submitForm">
        <div>
          <label for="name_input">Name <span class="required">*</span></label>
          <input
            type="text"
            id="name_input"
            v-model.lazy.trim="name"
            placeholder="Enter your name"
            required
          />
        </div>
  
        <div>
          <label for="email_input">Email <span class="required">*</span></label>
          <input
            type="email"
            id="email_input"
            v-model="email"
            placeholder="Enter your email"
            required
          />
        </div>
  
        <div>
          <label for="phone_input">Phone Number <span class="required">*</span></label>
          <input
            type="number" maxlength="10" minlength="10"
            id="phone_input"
            v-model="phone"
            placeholder="Enter your phone number"
            pattern="^\+?[1-9]\d{1,14}$"
            required
          />
        </div>
  
        <div>
          <label for="suggestion_input">Suggestion <span class="required">*</span></label>
          <textarea
            id="suggestion_input"
            v-model="suggestion"
            placeholder="Write your suggestion here"
            required
          ></textarea>
        </div>
  
        <!-- Complaint checkbox -->
        <div>
          <label for="complaint">Got a complaint?</label>
          <input
            type="checkbox"
            id="complaint"
            v-model="complaint"
          />
        </div>
  
        <!-- Conditional complaint details form -->
        <div v-if="complaint">
          <div>
            <label for="bus_no_input">Bus Route Number </label>
            <input
              type="text"
              id="bus_no_input"
              v-model="busNo"
              placeholder="Enter the bus route number"
              
            />
          </div>
  
          <div>
            <label for="journey_time_input">Time of Journey </label>
            <input
              type="time"
              id="journey_time_input"
              v-model="journeyTime"
            />
          </div>
  
          <div>
            <label for="complaint_details">Complaint Details <span class="required">*</span></label>
            <textarea
              id="complaint_details"
              v-model="complaintDetails"
              placeholder="Describe your complaint here"
              required
            ></textarea>
          </div>
  
          <!-- added the complaint numbers from dtc website  -->
          <div>
            <label>For customer care helpline, call at :</label>
            <br/>
            <a href="tel:+9191123370373" class="phone-link">+91-11-23370373</a> <br />
            <a href="tel:+9191123370374" class="phone-link">+91-11-23370374</a> <br />
            <a href="tel:+918744073248" class="phone-link">+91-8744073248</a>
          </div>
        </div>
  
        <button type="submit">Submit</button>
      </form>
    </div>
  
    <!-- Footer Section -->
    <footer class="footer">
      <p>
        <!-- as of now i added the href for google but will add the help and support page link -->
        <a href="https://www.google.com" class="help-link">Help and Support</a>
      </p>
      <p>&copy; Byte Knightz 2024</p>
    </footer>
  
    <h2>HOPE YOU HAVE A NICE DAY!</h2>
  </template>
  
  <script>
  export default {
    name: "Home",
    data() {
      return {
        email: "",
        name: "",
        suggestion: "",
        phone: "",
        complaint: false,
        busNo: "",
        journeyTime: "",
        complaintDetails: "",
      };
    },
    methods: {
      submitForm() {
        console.log("Form submitted with the following details:");
        console.log("Email:", this.email);
        console.log("Name:", this.name);
        console.log("Suggestion:", this.suggestion);
        console.log("Phone:", this.phone);
        console.log("Complaint:", this.complaint);
        if (this.complaint) {
          console.log("Bus Number:", this.busNo);
          console.log("Journey Time:", this.journeyTime);
          console.log("Complaint Details:", this.complaintDetails);
        }
  
        // form data handling so that we can fetch the data to a backend server(table supabse)
        // After submission, clear the form fields.
        this.email = "";
        this.name = "";
        this.suggestion = "";
        this.phone = "";
        this.complaint = false;
        this.busNo = "";
        this.journeyTime = "";
        this.complaintDetails = "";
      }
    }
  };
  </script>
  
  <style scoped>
  /* Container for the entire page */
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Arial', sans-serif;
  }
  
  /* Header Styling */
  .header {
    text-align: center;
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 2px solid #ddd;
  }
  
  .logo-placeholder {
    margin-bottom: 20px;
    font-size: 1.5rem;
    color: #555;
    font-weight: bold;
  }
  
  h1 {
    color: rgb(160, 88, 214);
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 10px;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.1);
    transition: color 0.3s ease-in-out;
  }
  
  h1:hover {
    color: #ef325e;
  }
  
  .intro {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 5px;
  }
  
  .subtext {
    font-size: 1.1rem;
    color: #777;
  }
  
  /* Form Styling */
  form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    background-color: #f8f8f8;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  div {
    margin-bottom: 20px;
  }
  
  label {
    font-weight: bold;
    color: #333;
  }
  
  /* Red asterisk for required fields */
  .required {
    color: red;
    font-size: 1.2rem;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
  }
  
  textarea {
    height: 120px;
    resize: none;
  }
  
  button {
    padding: 14px;
    background-color: rgb(160, 88, 214);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: rgb(130, 68, 174);
  }
  
  /* Complaint section */
  div[v-if="complaint"] {
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  /* Phone link styling */
  .phone-link {
    color: rgb(110, 126, 224);
    font-weight: bold;
    font-size: 1.2rem;
    text-decoration: none;
  }
  
  .phone-link:hover {
    text-decoration: underline;
  }
  
  /* Footer Section */
  .footer {
    text-align: center;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 2px solid #ddd;
  }
  
  .help-link {
    color: rgb(160, 88, 214);
    text-decoration: none;
    font-size: 1.2rem;
  }
  
  .help-link:hover {
    text-decoration: underline;
  }
  
  h2 {
    color: rgb(70, 70, 70);
    text-align: center;
    margin-top: 30px;
  }
  </style>
  