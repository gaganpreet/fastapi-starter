import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  SimpleForm,
  TextField,
  TextInput,
} from "react-admin";

export const ItemList = (props: any) => (
  <List {...props} filters={[]}>
    <Datagrid>
      <TextField source="value" />
      <TextField source="id" />
      <EditButton />
    </Datagrid>
  </List>
);

export const ItemEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="value" />
    </SimpleForm>
  </Edit>
);

export const ItemCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="value" />
    </SimpleForm>
  </Create>
);
