#pragma once
#include <userver/formats/json.hpp>
#include "Product.hpp"
namespace product_search {
Product Parse(const userver::formats::json::Value& json,
                       userver::formats::parse::To<Product>);
}