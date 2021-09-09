import { createBrowserHistory as createHistory } from "history";
import simpleRestProvider from "ra-data-simple-rest";
import {
  Admin,
  fetchUtils,
  Resource,
  RouteWithoutLayout,
} from "react-admin";
import LoginPage from "./pages/Login";
import Register from "./pages/Register";
import authProvider from "./providers/authProvider";
import { basePath } from "./providers/env";

const httpClient = (url: string, options: any = {}) => {
  options.user = {
    authenticated: true,
    token: localStorage.getItem("token"),
  };
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider(`${basePath}/api/v1/`, httpClient);

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
    </Admin>
  );
};

export default App;
