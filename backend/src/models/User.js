
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },

  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
    lowercase: true
  },

  password: {
    type: String,
    required: true,
    minlength: 6
  },

  avatar: {
    type: String,
    default:
      'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&h=150&q=80'
  },

  phone: {
    type: String,
    default: ''
  },

  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Hash password when it is modified.
// Do not hash it again if it is already a bcrypt hash.
UserSchema.pre('save', async function () {
  if (!this.isModified('password')) {
    return;
  }

  const password = this.password;

  const isBcryptHash =
    typeof password === 'string' &&
    /^\$2[aby]\$\d{2}\$/.test(password);

  if (isBcryptHash) {
    return;
  }

  this.password = await bcrypt.hash(password, 10);
});

// Compare entered password with stored password hash
UserSchema.methods.matchPassword = async function (enteredPassword) {
  return bcrypt.compare(
    String(enteredPassword),
    this.password
  );
};

module.exports = mongoose.model('User', UserSchema);
