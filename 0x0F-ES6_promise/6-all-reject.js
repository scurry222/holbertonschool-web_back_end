const { signUpUser } = require('./4-all-reject');
const { uploadPhoto } = require('./5-all-reject');

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const profile = [];
  try {
    const success = await signUpUser(firstName, lastName);
    profile.push({
      status: 'fulfilled',
      value: success,
    });
    await uploadPhoto(fileName);
  } catch (err) {
    profile.push({
      status: 'rejected',
      value: `Error: ${fileName} cannot be processed`,
    });
  }
  return profile;
}
