import { Admin, Resource } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import authProvider from "./providers/authProvider";

const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com");

const App = () => {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource name="users" />
    </Admin>
  );
};

export default App;
