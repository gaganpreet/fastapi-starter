import { createBrowserHistory as createHistory } from "history";
import simpleRestProvider from "ra-data-simple-rest";
import {
  Admin,
  fetchUtils,
  ListGuesser,
  Resource,
  RouteWithoutLayout,
} from "react-admin";
import { Route } from "react-router";
import MyLayout from "./components/AdminLayout";
import { ProfileEdit } from "./pages/ProfileEdit";
import LoginPage from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import authProvider from "./providers/authProvider";
import { basePath } from "./providers/env";

const httpClient = (url: string, options: any = {}) => {
  options.user = {
    authenticated: true,
    token: `Bearer ${localStorage.getItem("token")}`,
  };
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider(`${basePath}/api/v1`, httpClient);

const customRoutes = [
  <RouteWithoutLayout exact path="/register" component={Register} noLayout />,
  <Route key="my-profile" path="/my-profile" render={() => <ProfileEdit />} />,
];

const App = () => {
  return (
    <Admin
      dataProvider={dataProvider}
      authProvider={authProvider}
      loginPage={LoginPage}
      customRoutes={customRoutes}
      history={createHistory()}
      appLayout={MyLayout}
      dashboard={Dashboard}
    >
      <Resource name="users" list={ListGuesser} />
    </Admin>
  );
};

export default App;
