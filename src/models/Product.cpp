#include "Product.hpp"
namespace product_search {
Product::Product(int id, const std::string product_name,
                 //ProductType type_of_product, 
                 double price,
                 const std::string link_to_picture,
                 const std::string link_to_product,
                 const std::string other_information)
    : id(id),
      product_name(product_name),
     // type_of_product(type_of_product),
      price(price),
      link_to_picture(link_to_picture),
      link_to_product(link_to_product),
      other_information(other_information) {}

int Product::getId() const {
    return id;
}

std::string Product::getProductName() const {
    return product_name;
}

//product_search::ProductType Product::getTypeOfProduct() const {
  //  return type_of_product;
//}

double Product::getPrice() const {
    return price;
}
std::string Product::getLinkToPicture() const {
    return link_to_picture;
}

std::string Product::getLinkToProduct() const {
    return link_to_product;
}

std::string Product::getOtherInformation() const {
    return other_information;
}

userver::formats::json::Value Serialize(
    const Product data,
    userver::formats::serialize::To<userver::formats::json::Value>) {
    userver::formats::json::ValueBuilder builder;
    builder["id"] = data.getId();
    builder["product_name"] = data.getProductName();
    //builder["type_of_product"] = data.getTypeOfProduct();
    builder["price"] = data.getPrice();
    builder["link_to_picture"] = data.getLinkToPicture();
    builder["link_to_product"] = data.getLinkToProduct();
    builder["other_information"] = data.getOtherInformation();
    return builder.ExtractValue();
}
}  // namespace product_search
