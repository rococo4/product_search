#include "ParseToProduct.hpp"
#include <string>
#include <userver/formats/json.hpp>
namespace product_search {
Product Parse(const userver::formats::json::Value& json,
                       userver::formats::parse::To<Product>) {
    return Product{
        json["id"].As<int>(0),
        json["product_name"].As<std::string>("missing information"),
       // json["type_of_product"].As<ProductType>(ProductType::NotFound),
        json["price"].As<double>(0),
        json["link_to_picture"].As<std::string>("NotFound"),
        json["link_to_product"].As<std::string>("NotFound"),
        json["other_infotmation"].As<std::string>("NotFound")};
}
}  // namespace product_search