from reactpy import component, html, run, use_state # Import the component, html, run, and use_state functions
from reactpy_router import route, simple, link # Import the route and link components
from reactpy_router.core import use_params # Import the use_params hook

@component
def root():
    return simple.router(
        route("/home", Home()),
        route("/login", LoginScreen()),
        route("/student", Students()),
        route("/teacher", Teachers()),
    )


@component
def Home():
    return html.div(
        html.h1("Home Page 🏠"),
        link("Home", to="/home"),
    )


@component
def Students():
    return html.div(
        html.h1("Students 📚"),
        link("Student Page", to="/student"),
    )


@component
def Teachers():
    return html.div(
        html.h1("Teachers 📞"),
        link("Teacher Page", to="/teacher"),
    )



@component
def LoginScreen():
    # Return the login screen HTML
    html.div(
        html.h1("Login Screen 🔑"),
        link("Login Screen", to="/login"),
    )  


        # Define state variables for the input fields
    username, set_username = use_state("")
    password, set_password = use_state("")

    # Define event handlers for the input fields
    def handle_username_change(event):
        set_username(event.target.value)

    def handle_password_change(event):
        set_password(event.target.value)

    # Define event handler for the form submission
    def handle_submit(event):
        event.preventDefault()
        print("Username:", username)
        print("Password:", password)

    # Render the login screen HTML
    return html.form(
        {"onSubmit": handle_submit, "style": {"margin": "auto", "display": "flex", "flexDirection": "column", "alignItems": "center", "justifyContent": "center", "height": "100vh"}},
        html.label({"style": {"fontWeight": "bold"}}, "Username:"),
        html.input({"type": "text", "value": username, "onChange": handle_username_change}),
        html.br(),
        html.label({"style": {"fontWeight": "bold"}}, "Password:"),
        html.input({"type": "password", "value": password, "onChange": handle_password_change}),
        html.br(),
        html.button({"type": "submit"}, "Login")
    )

     

# Run the app
run(root)