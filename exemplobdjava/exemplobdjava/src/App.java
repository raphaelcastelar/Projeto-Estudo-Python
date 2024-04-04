import DAO.usuarioDAO;
import entity.Usuario;

public class App {
    public static void main(String[] args) throws Exception {
        
        Usuario u = new Usuario();
        u.setNome("Raphael");
        u.setLogin("raphael");
        u.setSenha("12345");
        u.setEmail("raphael@gmail.com");
        
        new usuarioDAO().cadastrarUsuario(u);

    }
}
