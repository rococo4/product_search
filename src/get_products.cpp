#include "get_products.hpp"

#include <vector>

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
      : HttpHandlerBase(config, component_context){}

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
    return {"apple", "banana", "orange"};
}

void AppendGetProducts(userver::components::ComponentList& component_list) {
    component_list.Append<Products>();
    component_list.Append<userver::clients::dns::Component>();
}

}  // namespace product_search
