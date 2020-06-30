const { signUpUser } = require('./4-all-reject');
const { uploadPhoto } = require('./5-all-reject');

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((resolve) => resolve.map((result) => ({
    status: result,
    value: resolve,
  })));
}
