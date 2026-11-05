const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const path = require('path');

// Load environment variables from backend/.env
dotenv.config({
  path: path.resolve(__dirname, '../.env')
});

// Import MongoDB connection
const { connectDB, getIsConnected } = require('./config/db');

// Import destination and user seeding functions
const { seedDestinations } = require('./controllers/destinationController');
const { seedUsers } = require('./controllers/authController');

// Initialize Express
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// API Routes
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/trips', require('./routes/tripRoutes'));
app.use('/api/bookings', require('./routes/bookingRoutes'));
app.use('/api/expenses', require('./routes/expenseRoutes'));
app.use('/api/destinations', require('./routes/destinationRoutes'));

// Welcome route
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to the Smart Travel Planner API!',
    status: 'Server is running',
    dbConnected: getIsConnected()
  });
});

// Port configuration
const PORT = process.env.PORT || 5000;

// Start listening immediately on 0.0.0.0 so health checks pass without delay
const server = app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
  console.log(`API URL: http://localhost:${PORT}`);
});

// Attempt DB connection in background without blocking server availability
connectDB()
  .then(async () => {
    if (getIsConnected()) {
      console.log('MongoDB connection successful.');
      await seedDestinations().catch(err => console.warn('Destination seed error:', err.message));
      await seedUsers().catch(err => console.warn('User seed error:', err.message));
    } else {
      console.log('Operating in mock database fallback mode.');
    }
  })
  .catch(error => {
    console.warn('Background database initialization warning:', error.message);
  });

module.exports = app;
