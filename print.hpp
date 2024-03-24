#ifndef MY_PRINT_WRAPPER__
#define MY_PRINT_WRAPPER__

#if (__cplusplus >= 202302L)

#include <print>

template <typename... Args>
void print(std::format_string<Args...> str, Args&&... args) {
  std::print(stdout, str, std::forward<Args>(args)...);
}

template <typename... Args>
void eprint(std::format_string<Args...> str, Args&&... args) {
  std::print(stderr, str, std::forward<Args>(args)...);
}

template <typename... Args>
void println(std::format_string<Args...> str, Args&&... args) {
  std::println(stdout, str, std::forward<Args>(args)...);
}

template <typename... Args>
void eprintln(std::format_string<Args...> str, Args&&... args) {
  std::println(stderr, str, std::forward<Args>(args)...);
}

#endif  // __cplusplus
#endif  // MY_PRINT_WRAPPER__
