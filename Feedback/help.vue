<template>
  <div class="Help">
    <h1 id="help_heading">Help & Support</h1>
    <p>Welcome to DTC - eSupport</p>

    <div class="Recent_booking_box">
      <p>Need Help with your Recent Booking?</p>
      <button type="button" id="log_in_now">LOG IN NOW</button>
    </div>

    <div class="para">
      <p>Important Contacts and Helpline Numbers</p>
    </div>

    <div class="contact-info">
      <div class="contact-grid">
  
        <div class="contact-detail dtc-helpline">
          <h3>DTC 24X7 Contact</h3>
          <p>Phone: <span>{{ dtc_contact }}</span></p>
          <p>Email: <span>{{ email }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Delhi Police Control Room</h3>
          <p>Phone: <span>{{ delhi_police_control_room_no }}</span></p>
          <p>Email: <span>{{ dp_email }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Women Helpline</h3>
          <p>Phone: <span>{{ women_helpline }}</span></p>
          <p>Email: <span>{{ women_email }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Delhi Police Tourist Helpline</h3>
          <p>Phone: <span>{{ dp_tou_helpline }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Emergency Response Support System</h3>
          <p>Phone: <span>{{ eme_resp_sup_sys }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Senior Citizen Helpline</h3>
          <p>Phone 1: <span>{{ Snr_cit_Helpline_1 }}</span></p>
          <p>Phone 2: <span>{{ Snr_cit_Helpline_2 }}</span></p>
          <p>Email: <span>{{ snr_email }}</span></p>
        </div>
  
        <div class="contact-detail">
          <h3>Cyber Crime Portal</h3>
          <p>Phone: <span>{{ cyber_crime_portal }}</span></p>
          <p>Website: 
               <!--added the cyber crime website link (it was also there in dmrc) -->
            <a :href="'http://' + cyber_crime_web" target="_blank">{{ cyber_crime_web }}</a>  
          </p>
        </div>
  
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Help",
  data() {
    return {
      // researched and found out the data from internet and few from some public websites 
      dtc_contact: '011-23370236',
      email: 'dcgmpld@dtc.nic.in',
      delhi_police_control_room_no: '112',
      dp_email: 'delpol.service@delhipolice.gov.in',
      women_helpline: '1091',
      women_email: 'complaintcell-ncw@nic.in',
      dp_tou_helpline: '8750871111',
      eme_resp_sup_sys: '112',
      Snr_cit_Helpline_1: '1091',
      Snr_cit_Helpline_2: '1291',
      snr_email: 'delpol.service@delhipolice.gov.in',
      cyber_crime_portal: '1930',
      cyber_crime_web: 'www.cybercrime.gov.in'
    };
  }
};
</script>
<style>
.Help {
  background-color: #f0f4f7;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

#help_heading {
  font-size: 3em;
  color: #00796b;
  font-weight: 600;
  text-align: center;
  margin-bottom: 20px;
}

.Recent_booking_box {
  background-color: #ffeb3b;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
  width: 320px;
  float: right;
  text-align: center;
}

.Recent_booking_box p {
  margin-bottom: 10px;
  font-size: 1.2em;
  font-weight: bold;
}

#log_in_now {
  background-color: #d32f2f;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1.1em;
  transition: background-color 0.3s ease;
}

#log_in_now:hover {
  background-color: #c62828;
}

.para {
  clear: both;
  text-align: center;
  font-size: 1.5em;
  color: #00796b;
  margin-top: 20px;
}

.contact-info {
  margin-top: 30px;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.contact-detail {
  padding: 20px;
  background-color: #ffffff;
  border-radius: 12px; /* More rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  border: 2px solid transparent; /* Default border with thinner border */
}

.contact-detail:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
}

.dtc-helpline {
  background-color: #ffffff; /* Keep it uncolored */
  border-left: 2px solid #00796b; /* Green left border, thinner and lighter */
}

.contact-detail h3 {
  font-size: 1.3em;
  color: #0288d1;
  margin-bottom: 10px;
}

.contact-detail p {
  font-size: 1.1em;
  color: #424242;
}

.contact-detail span {
  font-weight: bold;
  color: #00796b;
}

.contact-detail:nth-child(2) {
  border: 2px solid #ff5722; /* Orange border, thinner and lighter */
}

.contact-detail:nth-child(3) {
  border: 2px solid #9c27b0; /* Purple border, thinner and lighter */
}

.contact-detail:nth-child(4) {
  border: 2px solid #00bcd4; /* Cyan border, thinner and lighter */
}

.contact-detail:nth-child(5) {
  border: 2px solid #8bc34a; /* Green border, thinner and lighter */
}

.contact-detail:nth-child(6) {
  border: 2px solid #ff9800; /* Amber border, thinner and lighter */
}

.contact-detail:nth-child(7) {
  border: 2px solid #e91e63; /* Pink border, thinner and lighter */
}

.contact-detail:nth-child(8) {
  border: 2px solid #3f51b5; /* Indigo border, thinner and lighter */
}

a {
  color: #0288d1;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>