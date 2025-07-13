import streamlit as st
from nova_core import run_nova

# Set page config
st.set_page_config(
    page_title="NOVA Language",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
st.markdown("""
<style>
/* Combined CSS from both style.css and style1.css */
body {
  font-family: 'Segoe UI', sans-serif;
  margin: 0;
  background: #f9f9fb;
  color: #333;
}

.container {
  max-width: 960px;
  margin: auto;
  padding: 20px;
}

.hero {
  text-align: center;
  padding: 60px 20px;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: white;
  border-radius: 8px;
}

.hero h1 {
  font-size: 2.5em;
  margin-bottom: 0.4em;
}

.cta-button {
  background: white;
  color: #2575fc;
  padding: 12px 24px;
  font-size: 1em;
  border: none;
  border-radius: 4px;
  text-decoration: none;
  font-weight: bold;
  display: inline-block;
  margin-top: 20px;
}

.docs {
  margin-top: 50px;
}

.docs h2 {
  font-size: 2em;
  color: #2575fc;
  margin-top: 40px;
}

.docs h3 {
  color: #444;
  margin-top: 20px;
}

pre {
  background: #272822;
  color: #f8f8f2;
  padding: 12px;
  border-radius: 5px;
  overflow-x: auto;
}

code {
  font-family: 'Fira Code', monospace;
  font-size: 0.95em;
}

nav {
  background: #1a1a2e;
  color: white;
  padding: 20px;
  text-align: center;
  margin-bottom: 30px;
}

nav a {
  color: white;
  margin: 0 15px;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1em;
}

h1, h2 {
  color: #1a1a2e;
}

textarea {
  width: 100%;
  padding: 15px;
  font-family: monospace;
  font-size: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #fff;
  resize: vertical;
  min-height: 300px;
}

button {
  padding: 12px 24px;
  background: #1a1a2e;
  color: white;
  border: none;
  margin-top: 15px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  font-weight: bold;
}

pre.output, pre.error {
  background: #f4f4f4;
  padding: 15px;
  border-radius: 8px;
  margin-top: 15px;
  white-space: pre-wrap;
  font-family: monospace;
}

pre.error {
  border-left: 5px solid red;
  background: #ffecec;
}

/* Streamlit specific overrides */
.stButton>button {
  background: #1a1a2e;
  color: white;
  border-radius: 5px;
  padding: 12px 24px;
  font-weight: bold;
}

.stTextArea textarea {
  min-height: 300px;
}

/* Custom tab styling */
.tab-container {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.tab {
  padding: 12px 30px;
  background: #f0f0f0;
  color: #333;
  cursor: pointer;
  margin: 0 5px;
  border-radius: 5px;
  font-weight: bold;
  transition: all 0.3s ease;
}

.tab:hover {
  background: #e0e0e0;
}

.tab.active {
  background: #1a1a2e;
  color: white;
}

/* Responsive design */
@media (max-width: 768px) {
  .container {
    padding: 10px;
  }
  
  .hero {
    padding: 30px 15px;
  }
  
  .hero h1 {
    font-size: 2em;
  }
  
  .tab {
    padding: 10px 20px;
    font-size: 0.9em;
  }
}
</style>
""", unsafe_allow_html=True)

def home_tab():
    st.markdown("""
    <div class="hero">
        <h1>Welcome to the NOVA Language</h1>
        <p>NOVA is a lightweight, beginner-friendly, interpreted programming language designed to be easy to read, powerful, and extendable. It is built for education, rapid prototyping, and hobbyist development.</p>
        <a href="#try" class="cta-button">Try It Now →</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="docs">
        <h2>Features</h2>
        <ul>
            <li>Simple syntax inspired by Python and BASIC</li>
            <li>Variables, numbers, strings, booleans</li>
            <li>Arithmetic and logical expressions</li>
            <li>Control structures: <code>IF</code>, <code>WHILE</code>, <code>FOR</code></li>
            <li>Functions with arguments and return values</li>
            <li>Built-in error handling and clear error messages</li>
            <li>Custom syntax highlighting</li>
            <li>Comment support using <code>#</code></li>
        </ul>

        <h2>Syntax Guide</h2>

        <h3>1. Variables</h3>
        <pre><code>NOVA x = 10
x + 5  # returns 15</code></pre>

        <h3>2. Arithmetic</h3>
        <pre><code>2 + 3 * 4 - 1 / 2</code></pre>

        <h3>3. Booleans & Logical Operators</h3>
        <pre><code>TRUE AND FALSE  # FALSE
NOT TRUE        # FALSE
5 > 2           # TRUE</code></pre>

        <h3>4. Conditionals</h3>
        <pre><code>IF x > 10 THEN
    x + 1
ELSE
    x - 1</code></pre>

        <h3>5. Loops</h3>
        <h4>WHILE Loop</h4>
        <pre><code>NOVA i = 0
WHILE i < 5 DO
    i = i + 1</code></pre>

        <h4>FOR Loop</h4>
        <pre><code>FOR i = 1 TO 5 DO
    i * 2</code></pre>

        <h3>6. Functions</h3>
        <pre><code>FUNC add(a, b) -> RETURN a + b

add(4, 5)  # returns 9</code></pre>

        <h3>7. Comments</h3>
        <pre><code># This is a comment
NOVA y = 7</code></pre>

        <h3>8. Errors</h3>
        <p>If there's an error in your code, NOVA provides syntax or runtime error messages with highlighted locations, like:</p>
        <pre><code>SyntaxError: Expected identifier after NOVA</code></pre>
    </div>
    """, unsafe_allow_html=True)

def try_tab():
    st.markdown("<h1>Try NOVA</h1>", unsafe_allow_html=True)
    
    code = st.text_area("", height=400, placeholder="Write NOVA code here...", key="code_input")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        run_clicked = st.button("Run Code", key="run_button")
    with col2:
        clear_clicked = st.button("Clear Output", key="clear_button")
    
    # Initialize session state variables
    if 'output' not in st.session_state:
        st.session_state.output = ""
    if 'error' not in st.session_state:
        st.session_state.error = ""
    
    if run_clicked:
        if code.strip():
            processed_code = code.replace('\r\n', '\n').strip()
            processed_code = "\n".join([line.strip() for line in processed_code.splitlines() if line.strip() != ""])
            
            output, err = run_nova("<stdin>", processed_code)
            
            st.session_state.output = str(output) if output else ''
            st.session_state.error = str(err) if err else ''
        else:
            st.warning("Please enter some code to run")
    
    if clear_clicked:
        st.session_state.output = ""
        st.session_state.error = ""
    
    if st.session_state.output:
        st.markdown("<h2>Output</h2>", unsafe_allow_html=True)
        st.markdown(f'<pre class="output">{st.session_state.output}</pre>', unsafe_allow_html=True)
    
    if st.session_state.error:
        st.markdown("<h2>Error</h2>", unsafe_allow_html=True)
        st.markdown(f'<pre class="error">{st.session_state.error}</pre>', unsafe_allow_html=True)

def main():
    # Create custom navigation
    st.markdown("""
    <nav>
        <a href="#home">Documentation</a>
        <a href="#try">Try NOVA</a>
    </nav>
    """, unsafe_allow_html=True)
    
    # Create custom tabs
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    
    # Initialize session state for active tab
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Home"
    
    # Home tab button
    home_active = "active" if st.session_state.active_tab == "Home" else ""
    st.markdown(f'<div class="tab {home_active}" onclick="window.parent.document.querySelector(\'[data-testid="stMarkdownContainer"]\').scrollIntoView(); setTimeout(function(){{window.parent.document.dispatchEvent(new Event(\'HOME_TAB\'));}}, 100)">Home</div>', unsafe_allow_html=True)
    
    # Try tab button
    try_active = "active" if st.session_state.active_tab == "Try" else ""
    st.markdown(f'<div class="tab {try_active}" onclick="window.parent.document.querySelector(\'[data-testid="stMarkdownContainer"]\').scrollIntoView(); setTimeout(function(){{window.parent.document.dispatchEvent(new Event(\'TRY_TAB\'));}}, 100)">Try NOVA</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # JavaScript for tab switching
    st.components.v1.html("""
    <script>
    document.addEventListener('HOME_TAB', function() {
        window.parent.document.querySelectorAll('[data-testid="stMarkdownContainer"]')[1].innerHTML = '<div style="display:none">HOME_TAB</div>';
    });
    
    document.addEventListener('TRY_TAB', function() {
        window.parent.document.querySelectorAll('[data-testid="stMarkdownContainer"]')[1].innerHTML = '<div style="display:none">TRY_TAB</div>';
    });
    </script>
    """, height=0)
    
    # Handle tab switching
    if 'trigger' in st.session_state:
        if st.session_state.trigger == "HOME_TAB":
            st.session_state.active_tab = "Home"
        elif st.session_state.trigger == "TRY_TAB":
            st.session_state.active_tab = "Try"
    
    # Check for tab trigger
    if st.session_state.active_tab == "Home":
        home_tab()
    elif st.session_state.active_tab == "Try":
        try_tab()

if __name__ == '__main__':
    # Initialize trigger state
    if 'trigger' not in st.session_state:
        st.session_state.trigger = None
    
    # Check for hidden trigger
    if st.session_state.get('trigger'):
        st.session_state.trigger = None
        st.experimental_rerun()
    
    main()