/**
 * predict number from API
 */
const predictDigit=(image)=>{
  return new Promise(resolve => {
    axios.post(`${domain}/mnist`, {
      image
    })
      .then((response) => {
        var dataObject = response.data;
        // POST success
        // console.log(dataObject);
        resolve(dataObject);
      },
        (error) => {
          resolve('dataObject');
        }
      );
  });
}