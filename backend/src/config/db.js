const mongoose = require('mongoose');
const path = require('path');
const dotenv = require('dotenv');

// Load the backend .env file if available
dotenv.config({
  path: path.resolve(__dirname, '../../.env')
});
dotenv.config({
  path: path.resolve(__dirname, '../.env')
});

let isConnected = false;

const connectDB = async () => {
  const mongoURI = process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/smart-travel-planner';
  const dbName = process.env.MONGO_DB_NAME;

  try {
    console.log(`Connecting to MongoDB at: ${mongoURI.split('@').pop()}${dbName ? ` (dbName: ${dbName})` : ''}`);

    await mongoose.connect(mongoURI, {
      serverSelectionTimeoutMS: 3000,
      connectTimeoutMS: 3000,
      ...(dbName ? { dbName } : {})
    });

    isConnected = true;
    console.log('MongoDB Connected Successfully!');
    console.log(`Database Name: ${mongoose.connection.name}`);

    return true;
  } catch (error) {
    console.warn('MongoDB Connection Failed:', error.message);
    console.log('--- RUNNING WITH IN-MEMORY MOCK FALLBACK DB ---');
    isConnected = false;
    return false;
  }
};

const getIsConnected = () => {
  return isConnected && mongoose.connection.readyState === 1;
};

module.exports = {
  connectDB,
  getIsConnected
};
