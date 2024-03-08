#include "get_products.hpp"
#include <string>
#include <vector>
#include "/home/rococo4/pg_service_template/src/models/Product.hpp"
#include "userver/logging/log.hpp"
#include "/home/rococo4/pg_service_template/src/models/ParseToProduct.hpp"
#include <fmt/format.h>
#include <userver/clients/dns/component.hpp>
#include <userver/components/component.hpp>
#include <userver/server/handlers/http_handler_base.hpp>
#include <userver/storages/postgres/cluster.hpp>
#include <userver/storages/postgres/component.hpp>
#include <userver/utils/assert.hpp>

namespace product_search {

namespace {

class Products final : public userver::server::handlers::HttpHandlerBase {
   public:
    static constexpr std::string_view kName = "handler-get-products";

    Products(const userver::components::ComponentConfig& config,
             const userver::components::ComponentContext& component_context)
        : HttpHandlerBase(config, component_context) {}

    std::string HandleRequestThrow(
        const userver::server::http::HttpRequest& request,
        userver::server::request::RequestContext&) const override {

        std::string s = "";
        for (auto i : GetProducts()) {
            s += " " + i;
        }
        return s;
    }
};

}  // namespace

std::vector<std::string> GetProducts() {
    Product laptop(12345, "Lenovo ThinkPad X1 Carbon",
                  // product_search::ProductType::MilkProducts,
                     1500.00,
                   "http://example.com/images/lenovo_thinkpad_x1_carbon.jpg",
                   "http://example.com/products/12345",
                   "14-дюймовый ноутбук, Intel Core i7, 16 ГБ RAM, 512 ГБ SSD");
    auto a = product_search::Serialize(
        laptop,
        userver::formats::serialize::To<userver::formats::json::Value>());
    LOG_ERROR() <<"asd"<< a;
    auto t = product_search::Parse(a, userver::formats::parse::To<Product>());
    LOG_ERROR()<< "asd123" << t.getProductName();
    return {""};

}

void AppendGetProducts(userver::components::ComponentList& component_list) {
    component_list.Append<Products>();
    component_list.Append<userver::clients::dns::Component>();
}

}  // namespace product_search
