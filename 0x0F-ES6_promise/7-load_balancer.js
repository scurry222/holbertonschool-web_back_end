export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([
    chinaDownload,
    USDownload,
  ]).then((msg) => {
    console.log(msg);
  });
}
