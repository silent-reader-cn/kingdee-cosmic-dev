# 经营核算维度文本-xkoac_assist_txt

## 经营核算维度文本-主表 t_xkoac_assist_txt

- **表名称：** 经营核算维度文本-主表
- **表名：** t_xkoac_assist_txt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 横表 | int8 | 64 |  | √ | 0 | 经营核算维度文本 xkoac_assist_txt |
| 2 | fvalue | 核算项目值 | varchar | 300 |  | √ | ' ' | 核算项目值 |
| 3 | fflexfield | 核算项目类型 | varchar | 30 |  | √ | ' ' | 核算项目类型 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_assist_txt |  | fid |
| 2 | pk_t_xkoac_assist_txt |  | fentryid |
