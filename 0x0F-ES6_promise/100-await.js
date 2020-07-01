const { uploadPhoto, createUser } = require('./utils');

export default async function asyncUploadUser() {
  try {
    const resFromUploadPhoto = await uploadPhoto();
    const resFromCreateUser = await createUser();
    return Promise.resolve({
      photo: resFromUploadPhoto,
      user: resFromCreateUser,
    });
  } catch (err) {
    return Promise.resolve({
      photo: null,
      user: null,
    });
  }
}
