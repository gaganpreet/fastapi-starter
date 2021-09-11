import {
  createContext,
  useState,
  useCallback,
  useMemo,
  useContext,
} from "react";
import {
  TextInput,
  SimpleForm,
  required,
  useNotify,
  SaveContextProvider,
  useGetIdentity,
} from "react-admin";
import { userApi } from "../providers/env";

const ProfileContext = createContext({});

export const ProfileProvider = ({ children }: { children: any }) => {
  const [profileVersion, setProfileVersion] = useState(0);
  const context = useMemo(
    () => ({
      profileVersion,
      refreshProfile: () =>
        setProfileVersion((currentVersion) => currentVersion + 1),
    }),
    [profileVersion]
  );

  return (
    <ProfileContext.Provider value={context}>
      {children}
    </ProfileContext.Provider>
  );
};

export const useProfile = () => useContext(ProfileContext);

export const ProfileEdit = ({ ...props }) => {
  const notify = useNotify();
  const [saving, setSaving] = useState(false);

  const { loaded, identity } = useGetIdentity();

  const handleSave = useCallback(
    (values) => {
      setSaving(true);
      userApi
        .updateMeUsersMePatch({ userUpdate: values })
        .then(() => {
          setSaving(false);
          notify("Your profile has been updated", "info");
        })
        .catch((e) => {
          setSaving(false);
          notify(
            e.response?.data?.detail || "Unknown error, please try again later"
          );
        });
    },
    [notify]
  );

  const saveContext = useMemo(
    () => ({
      save: handleSave,
      saving,
    }),
    [saving, handleSave]
  );

  if (!loaded) {
    return null;
  }

  return (
    <SaveContextProvider value={saveContext}>
      <SimpleForm save={handleSave} record={identity ? identity : {}}>
        <TextInput source="id" disabled />
        <TextInput source="email" required />
      </SimpleForm>
    </SaveContextProvider>
  );
};
