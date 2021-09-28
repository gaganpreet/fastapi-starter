import { createBrowserHistory as createHistory } from "history";
import simpleRestProvider from "ra-data-simple-rest";
import { Admin, fetchUtils, Resource, RouteWithoutLayout } from "react-admin";
import { Route } from "react-router";
import MyLayout from "./components/AdminLayout";
import Dashboard from "./pages/Dashboard";
import { ItemCreate, ItemEdit, ItemList } from "./pages/Items";
import LoginPage from "./pages/Login";
import { ProfileEdit } from "./pages/ProfileEdit";
import Register from "./pages/Register";
import { UserEdit, UserList } from "./pages/Users";
import authProvider from "./providers/authProvider";
import { basePath } from "./providers/env";

const httpClient = (url: string, options: any = {}) => {
  options.user = {
    authenticated: true,
    token: `Bearer ${localStorage.getItem("token")}`,
  };
  if (url.includes("/users/") && options.method === "PUT") {
    // We use PATCH for update on the backend for users, since PATCH is selective PUT, this change should be fine
    options.method = "PATCH";
  }
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
      layout={MyLayout}
      dashboard={Dashboard}
    >
      <Resource name="users" list={UserList} edit={UserEdit} />
      <Resource
        name="items"
        list={ItemList}
        edit={ItemEdit}
        create={ItemCreate}
      />
    </Admin>
  );
};

export default App;
