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
    cy.get("button").last().contains("Register").click();

    cy.get("input").first().type(username);
    cy.get("input").last().type(defaultPassword);
    cy.get("button").first().click();
    cy.contains("Successfully registered");
  });

  it("Logs in", () => {
    cy.get("input").first().type(username);
    cy.get("input").last().type(defaultPassword);
    cy.get("button").first().click();
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
    cy.get('button[title^="Profile"]').click();
    cy.contains("My Profile").click();
    const newUsername = `abc${new Date().getTime()}@example.com`;
    cy.get(`input[value='${username}']`).clear().type(newUsername);
    cy.contains("Save").click();
    cy.contains("Your profile has been updated");
  });
});
