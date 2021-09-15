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
  useSaveContext,
} from "react-admin";
import { userApi } from "../providers/env";

const ProfileContext = createContext({
  profileVersion: 0,
  refreshProfile: () => {},
});

export const ProfileProvider = ({ children }: { children: any }) => {
  const [profileVersion, setProfileVersion] = useState(0);
  const context = useMemo(
    () => ({
      profileVersion,
      refreshProfile: () => {
        setProfileVersion((currentVersion) => currentVersion + 1);
      },
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
  const { refreshProfile, profileVersion } = useProfile();
  const { loaded, identity } = useGetIdentity();

  const handleSave = useCallback(
    (values) => {
      setSaving(true);
      userApi
        .updateMe({ userUpdate: values })
        .then(() => {
          setSaving(false);
          notify("Your profile has been updated", "info");
          refreshProfile();
        })
        .catch((e) => {
          setSaving(false);
          notify(
            e.response?.data?.detail || "Unknown error, please try again later",
            "error"
          );
        });
    },
    [notify, refreshProfile]
  );

  const saveContext = useSaveContext({ save: handleSave, saving });

  if (!loaded) {
    return null;
  }

  // TODO: The save button is not disabled after save
  return (
    <SaveContextProvider value={saveContext} key={profileVersion}>
      <SimpleForm save={handleSave} record={identity ? identity : {}}>
        <TextInput source="id" disabled />
        <TextInput source="email" validate={required()} />
      </SimpleForm>
    </SaveContextProvider>
  );
};
