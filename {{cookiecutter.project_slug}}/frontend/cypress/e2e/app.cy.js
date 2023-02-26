const username = `abc${new Date().getTime()}@example.com`;
const defaultPassword = "password";

describe("Test register, login and item", () => {
  beforeEach(() => {
    // Cypress starts out with a blank slate for each test
    // so we must tell it to visit our website with the `cy.visit()` command.
    // Since we want to visit the same URL at the start of all our tests,
    // we include it in our beforeEach function so that it runs before each test
    cy.restoreLocalStorage();
    cy.visit("http://localhost:{{ cookiecutter.frontend_port }}/");
  });

  it("Displays login page", () => {
    cy.contains("Sign in");
    cy.contains("Register");
  });

  it("Creates a new account", () => {
    cy.get("a").last().contains("Register").click();

    cy.get("input").first().type(username);
    cy.get("input").last().type(defaultPassword);
    cy.get("button").first().click();
    cy.contains("Successfully registered");
  });

  it("Logs in", () => {
    cy.get("input").first().type(username);
    cy.get("input").last().type(defaultPassword);
    cy.get("button").first().click();
    cy.get("button")
      .first()
      .click()
      .should(
        () => {
          // eslint-disable-next-line no-unused-expressions
          expect(localStorage.getItem("token")).to.be.not.null;
        },
        { timeout: 2000 }
      );
    cy.contains("Welcome to admin");
    cy.saveLocalStorage();
  });

  it("Creates an item", () => {
    cy.contains("Items").click();
    cy.contains("No Items yet", { timeout: 1000 });
    cy.contains("Create").click();
    cy.get("input").type("value");
    cy.contains("Save").click();
    cy.contains("Element created");
  });

  it("Edits an item", () => {
    cy.contains("Items").click();
    cy.contains("Edit").click();
    cy.get("input").type("value 2");
    cy.contains("Save").click();
    cy.contains("Element updated");
  });

  it("Edits profile", () => {
    cy.get('button[aria-label^="Profile"]').click();
    cy.contains("My Profile").click();
    const newUsername = `abc${new Date().getTime()}@example.com`;
    // Need to use {force: true} for following operations because
    // the custom app bar doesn't hide itself when the Profile button is clicked
    // Possible solution, but useUserMenu() returns undefined:
    // https://github.com/marmelab/react-admin/blob/master/packages/ra-ui-materialui/src/layout/useUserMenu.ts
    cy.get('input[id="email"]', { timeout: 1000 })
      .should("have.value", username)
      .click({ force: true });
    cy.get(`input[id="email"]`)
      .clear({ force: true })
      .type(newUsername, { force: true });
    cy.contains("Save").click({ force: true });
    cy.contains("Your profile has been updated");
  });

  it("Sucessfully logs out", () => {
    cy.get('button[aria-label^="Profile"]').click();
    cy.contains("Logout").click();
    cy.contains("Sign in");
    cy.contains("Register");
  });
});
