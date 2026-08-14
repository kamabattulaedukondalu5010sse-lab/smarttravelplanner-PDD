const mongoose = require('mongoose');

let isConnected = false;

const connectDB = async () => {
  try {
    const mongoURI = process.env.MONGO_URI || 'mongodb://localhost:27017/smart-travel-planner';
    const dbName = process.env.MONGO_DB_NAME;
    console.log(`Connecting to MongoDB at: ${mongoURI}${dbName ? ` (dbName override: ${dbName})` : ''}`);
    
    const connectOptions = {
      serverSelectionTimeoutMS: 5000
    };
    if (dbName) {
      connectOptions.dbName = dbName;
    }

    // Set a short timeout for connection testing
    await mongoose.connect(mongoURI, connectOptions);
    
    isConnected = true;
    console.log('MongoDB Connected Successfully!');
  } catch (error) {
    console.error('MongoDB Connection Failed:', error.message);
    console.log('--- WARNING: RUNNING SERVER WITH IN-MEMORY MOCK FALLBACK DB ---');
    isConnected = false;
  }
};

const getIsConnected = () => isConnected;

module.exports = { connectDB, getIsConnected };
