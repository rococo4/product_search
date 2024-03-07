#pragma once

#include <string>
#include <string_view>

#include <userver/components/component_list.hpp>
#include <vector>

namespace product_search {

std::vector<std::string> GetProducts();

void AppendGetProducts(userver::components::ComponentList& component_list);

}  // namespace product_search
