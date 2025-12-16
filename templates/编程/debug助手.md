# Debug调试助手模板

## 模板名称
智能调试助手

## 适用场景
- 排查代码bug
- 分析错误日志
- 调试程序问题
- 性能问题诊断

## 提示词模板

```
你是一位经验丰富的调试专家。我遇到了一个编程问题，需要你的帮助。

问题信息：
- 编程语言/框架：[语言/框架]
- 问题描述：[详细描述遇到的问题]
- 错误信息：[如有错误信息，请粘贴]
- 预期行为：[描述期望的正确行为]
- 实际行为：[描述实际发生的情况]

相关代码：
```[代码语言]
[粘贴相关代码]
```

环境信息：
- 操作系统：[OS]
- 版本信息：[相关软件/库版本]

请帮我：
1. 分析问题的根本原因
2. 提供解决方案
3. 解释为什么会出现这个问题
4. 给出预防类似问题的建议
```

## 使用示例

```
你是一位经验丰富的调试专家。我遇到了一个编程问题，需要你的帮助。

问题信息：
- 编程语言/框架：JavaScript/React
- 问题描述：组件重新渲染时数据丢失
- 错误信息：无报错，但state重置为初始值
- 预期行为：state应该保持更新后的值
- 实际行为：每次父组件更新，子组件的state都会重置

相关代码：
```javascript
function ChildComponent() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

function ParentComponent() {
  const [refresh, setRefresh] = useState(0);
  return (
    <div>
      <ChildComponent />
      <button onClick={() => setRefresh(refresh + 1)}>刷新</button>
    </div>
  );
}
```

环境信息：
- 操作系统：Windows 10
- 版本信息：React 18.2.0

请帮我：
1. 分析问题的根本原因
2. 提供解决方案
3. 解释为什么会出现这个问题
4. 给出预防类似问题的建议
```

## 标签
#编程 #调试 #debug #问题解决
