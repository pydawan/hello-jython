import org.python.core.*;
import org.python.util.PythonInterpreter;

public class JythonTest {

    public static void main(String[] args) {
        PythonInterpreter python = new PythonInterpreter();
        python.set("i", new PyInteger(42));
        System.out.println(python.get("i"));
        python.exec("square = i * i");
        System.out.println(python.get("square"));
        python.exec("import django");
        python.exec("version = django.VERSION");
        System.out.println(python.get("version"));
        python.execfile("src/models/Pessoa.py");
        python.close();
    }

}
