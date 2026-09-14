@RestController
@RequestMapping("/products")
public class ProductController {

    @GetMapping("/{id}")
    public String getProduct(
            @PathVariable String id
    ) {

        return "Product";
    }
}
