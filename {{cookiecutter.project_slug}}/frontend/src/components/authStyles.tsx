const authStyles = {
  main: {
    display: "flex",
    // Following "string" as "string" is ugly, but it's a Typescript thing
    flexDirection: "column" as "column",
    minHeight: "100vh",
    alignItems: "center",
    justifyContent: "flex-start",
    backgroundColor: "#fcf7e1",
  },
  card: {
    minWidth: 300,
    marginTop: "6em",
  },
  header: {
    textAlign: "center",
  },
  avatar: {
    margin: "1em",
    display: "flex",
    justifyContent: "center",
  },
  form: {
    padding: "0 1em 1em 1em",
  },
  actions: {
    padding: "0 1em 1em 1em",
  },
};

export default authStyles;
