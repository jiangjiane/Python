#工厂函数
print('工厂函数举例：')
def maker(N):
    def action(X):
        return X**N
    return action
