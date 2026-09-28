# 模拟银行-ebg_simulator

## 模拟银行-主表 t_ebg_simulator

- **表名称：** 模拟银行-主表
- **表名：** t_ebg_simulator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fext | 备用 | varchar | 1024 |  | √ | ' ' | 备用 |
| 3 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 4 | fkey | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 5 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ebg_simulator |  | fid |
| 2 | idx_ebg_simulator_key |  | fkey |
