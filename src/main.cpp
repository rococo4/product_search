#include <userver/clients/http/component.hpp>
#include <userver/components/minimal_server_component_list.hpp>
#include <userver/server/handlers/ping.hpp>
#include <userver/server/handlers/tests_control.hpp>
#include <userver/testsuite/testsuite_support.hpp>
#include <userver/utils/daemon_run.hpp>

#include "get_products.hpp"
#include "hello.hpp"

int main(int argc, char* argv[]) {
  auto component_list = userver::components::MinimalServerComponentList()
                            .Append<userver::server::handlers::Ping>()
                            .Append<userver::components::TestsuiteSupport>()
                            .Append<userver::components::HttpClient>()
                            .Append<userver::server::handlers::TestsControl>();

  product_search::AppendHello(component_list);
  product_search::AppendGetProducts(component_list);
  return userver::utils::DaemonMain(argc, argv, component_list);
}
