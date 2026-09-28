# JavaBean配置-arap_beandefinition

## JavaBean配置-主表 t_arap_beandefinition

- **表名称：** JavaBean配置-主表
- **表名：** t_arap_beandefinition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbeanclass | 接口 | varchar | 150 |  | √ | ' ' | 接口 |
| 3 | fbeanname | bean名称 | varchar | 150 |  | √ | ' ' | bean名称 |
| 4 | finstanceclass | 实例 | varchar | 150 |  | √ | ' ' | 实例 |
| 5 | fbeantype | 实例类型 | varchar | 30 |  | √ | ' ' | 实例类型,枚举: java :java ks :ks |
| 6 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 7 | fscope | 实例作用域 | varchar | 30 |  | √ | ' ' | 实例作用域,枚举: Singleton :单例 Prototype :原型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_arap_beandefinition_pkey |  | fid |
| 2 | idx_arap_beanname |  | fbeanname |
