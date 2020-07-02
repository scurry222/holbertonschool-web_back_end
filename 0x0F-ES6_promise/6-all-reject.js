import signUpUser from './4-all-reject';
import uploadPhoto from './5-all-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signIn = await signUpUser(firstName, lastName)
    .then((res) => ({
      status: 'fulfilled',
      value: res,
    }))
    .catch((err) => ({
      status: 'rejected',
      value: err.toString(),
    }));
  const upload = await uploadPhoto(fileName)
    .catch((err) => ({
      status: 'rejected',
      value: err.toString(),
    }));
  return Promise.resolve([
    signIn,
    upload,
  ]);
}
