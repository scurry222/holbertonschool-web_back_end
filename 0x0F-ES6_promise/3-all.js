const { uploadPhoto, createUser } = require('./utils');

export default function handleProfileSignup() {
  return uploadPhoto()
    .then(({ body }) => {
      createUser()
        .then(({ firstName, lastName }) => {
          console.log(
            body,
            firstName,
            lastName,
          );
        })
        .catch(() => {
          console.log('Signup system offline');
        });
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
