---
crate: trendy_terminal
layout: gnatdoc
gnatdoc: {
name: "Trendy_Terminal.Lines",
qualified_name: "Trendy_Terminal.Lines",
signature: "trendy_terminal.lines",
enclosing: "trendy_terminal",
is_private: false,
documentation: " Unless required by applicable law or agreed to in writing, software\n distributed under the License is distributed on an \"AS IS\" BASIS,\n WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n See the License for the specific language governing permissions and\n limitations under the License.\n-----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor_Direction",
       qualified_name: "Trendy_Terminal.Lines.Cursor_Direction",
       signature: "trendy_terminal.lines.cursor_direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor_Direction is (Left, Right);",
       }   ,
       {
       name: "Line",
       qualified_name: "Trendy_Terminal.Lines.Line",
       signature: "trendy_terminal.lines.line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line is private\n    with Type_Invariant => Get_Cursor_Index (Line) in 1 .. Length (Line) + 1;",
       }   ,
   ]
,}
---
