from textual.app import App, ComposeResult, RenderResult
from textual import events
from textual.widgets import Header
from textual.widget import Widget

class Hello(Widget):
    """Display a greeting."""
    CSS_PATH = "hello.tcss"
    def render(self) -> RenderResult:
        return "Hello, [b]World[/b]!"
    
class EventApp(App):
    
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]
    def compose(self) -> ComposeResult:
        yield Header()
    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"
        
    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            self.mount(Hello(classes = "Hello"))


if __name__ == "__main__":
    app = EventApp()
    app.run()