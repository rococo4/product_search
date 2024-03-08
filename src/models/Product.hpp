#pragma once
#include <string>
#include <userver/formats/json.hpp>
#include "ProductType.hpp"
namespace product_search {
class Product {
   private:
    int id;
    std::string product_name;
  //  product_search::ProductType type_of_product;
    double price;
    std::string link_to_picture;
    std::string link_to_product;
    std::string other_information;

   public:
    Product();

    Product(int id, const std::string product_name,
           // ProductType type_of_product, 
            double price,
            const std::string link_to_picture,
            const std::string link_to_product,
            const std::string other_information);

    int getId() const;
    std::string getProductName() const;
   // product_search::ProductType getTypeOfProduct() const;
    double getPrice() const;
    std::string getLinkToPicture() const;
    std::string getLinkToProduct() const;
    std::string getOtherInformation() const;

};
userver::formats::json::Value Serialize(
        const Product data,
        userver::formats::serialize::To<userver::formats::json::Value>);

}  // namespace product_search