import { Admin, Resource } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import authProvider from "./providers/authProvider";
import { RouteWithoutLayout } from "react-admin";
import LoginPage from "./pages/Login";
import Register from "./pages/Register";
import { createBrowserHistory as createHistory } from "history";

const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com");

const customRoutes = [
  <RouteWithoutLayout exact path="/register" component={Register} noLayout />,
];

const App = () => {
  return (
    <Admin
      dataProvider={dataProvider}
      authProvider={authProvider}
      loginPage={LoginPage}
      customRoutes={customRoutes}
      history={createHistory()}
    >
      <Resource name="users" />
    </Admin>
  );
};

export default App;
