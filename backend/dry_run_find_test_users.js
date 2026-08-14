const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

const MONGO_URI = process.env.MONGO_URI || 'mongodb+srv://kamabattulaedukondalu5010sse_db_user:lZ9O0YgiZvNMBceA@cluster0.pfdffws.mongodb.net/smart-travel-planner?appName=Cluster0';

async function dryRun() {
  console.log(`Connecting to MongoDB...`);
  await mongoose.connect(MONGO_URI);
  console.log('Connected to MongoDB successfully.');

  const User = mongoose.model('User', new mongoose.Schema({}, { strict: false }));

  const allUsers = await User.find({});
  console.log(`\nTotal users in 'users' collection: ${allUsers.length}`);

  const testUserQuery = {
    $or: [
      { name: /^LoadTestUser_\d+$/ },
      { email: /^loaduser_\d+@example\.com$/ },
      { email: 'invalid_user@example.com' },
      { email: 'john@example.com' },
      { email: 'admin@company.com' },
      { email: 'john.doe@company.com' }
    ]
  };

  const matchedTestUsers = await User.find(testUserQuery);

  console.log(`\n=== MATCHED TEST-GENERATED USERS (${matchedTestUsers.length}) ===`);
  matchedTestUsers.forEach((u, i) => {
    console.log(`${i + 1}. ID: ${u._id} | Name: "${u.name}" | Email: "${u.email}" | CreatedAt: ${u.createdAt}`);
  });

  const matchedIds = new Set(matchedTestUsers.map(u => u._id.toString()));
  const realUsers = allUsers.filter(u => !matchedIds.has(u._id.toString()));

  console.log(`\n=== REAL USERS / UNMATCHED USERS (${realUsers.length}) ===`);
  realUsers.forEach((u, i) => {
    console.log(`${i + 1}. ID: ${u._id} | Name: "${u.name}" | Email: "${u.email}" | CreatedAt: ${u.createdAt}`);
  });

  await mongoose.disconnect();
}

dryRun().catch(console.error);
