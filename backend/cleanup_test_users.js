const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

const MONGO_URI = process.env.MONGO_URI || 'mongodb+srv://kamabattulaedukondalu5010sse_db_user:lZ9O0YgiZvNMBceA@cluster0.pfdffws.mongodb.net/smart-travel-planner?appName=Cluster0';

async function deleteTestUsers() {
  console.log('Connecting to MongoDB database...');
  await mongoose.connect(MONGO_URI);
  console.log('Connected!');

  const User = mongoose.model('User', new mongoose.Schema({}, { strict: false }));

  // Query matching test-generated users
  const filter = {
    $or: [
      { name: /^LoadTestUser_\d+$/ },
      { email: /^loaduser_\d+@example\.com$/ },
      { email: 'testuser@example.com' },
      { email: /^user_\d+_\d+@travel\.com$/ },
      { name: 'QA Tester' }
    ]
  };

  const countBefore = await User.countDocuments(filter);
  console.log(`\nFound ${countBefore} test-generated user document(s) matching criteria.`);

  if (countBefore > 0) {
    const result = await User.deleteMany(filter);
    console.log(`Successfully deleted ${result.deletedCount} test-generated user document(s).`);
  } else {
    console.log('No matching test-generated users found to delete.');
  }

  const remainingUsers = await User.find({});
  console.log(`\nRemaining users count in collection: ${remainingUsers.length}`);
  remainingUsers.forEach((u, i) => {
    console.log(`${i + 1}. ID: ${u._id} | Name: "${u.name}" | Email: "${u.email}"`);
  });

  await mongoose.disconnect();
}

deleteTestUsers().catch(console.error);
