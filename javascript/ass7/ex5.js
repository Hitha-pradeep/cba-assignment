// Fetch users from API
fetch("https://jsonplaceholder.typicode.com/users")
  .then((response) => response.json()) // convert to JSON
  .then((users) => {
    users.forEach((user) => {
      console.log(`Name : ${user.name}`);
      console.log(`Email : ${user.email}`);
      console.log(`City : ${user.address.city}\n`);
    });
  })
  .catch((error) => {
    console.log("Error fetching data:", error);
  });
