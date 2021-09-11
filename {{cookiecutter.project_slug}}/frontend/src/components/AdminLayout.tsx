import { UserMenu, MenuItemLink, AppBar, Layout } from "react-admin";
import SettingsIcon from "@material-ui/icons/Settings";

const MyUserMenu = (props: any) => {
  // Forcing MenuItemLink to any because of some weird type mismatch, not sure what's going on
  const ItemLink = MenuItemLink as any;
  return (
    <UserMenu {...props}>
      <ItemLink
        to="/my-profile"
        primaryText="My Profile"
        leftIcon={<SettingsIcon />}
      />
    </UserMenu>
  );
};

const MyAppBar = (props: any) => (
  <AppBar {...props} userMenu={<MyUserMenu />} />
);

const MyLayout = (props: any) => <Layout {...props} appBar={MyAppBar} />;

export default MyLayout;
