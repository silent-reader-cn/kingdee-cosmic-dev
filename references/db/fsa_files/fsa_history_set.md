# 历史设置版本-fsa_history_set

## 历史设置版本-主表 t_fsa_history_set

- **表名称：** 历史设置版本-主表
- **表名：** t_fsa_history_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdatacontent | 数据内容（json） | varchar | 255 |  | √ | ' ' | 数据内容（json） |
| 5 | fdataid | 数据主键 | int8 | 64 |  | √ | 0 | 数据主键 |
| 6 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 7 | fdatacontent_tag | 数据内容（json）_详情 | text | 0 |  |  | null | 数据内容（json）_详情 |
| 8 | fschemaid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 9 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_history_set_1 |  | fschemaid,fdataid |
| 2 | pk_t_fsa_history_set |  | fid |
| 3 | idx_history_set_2 |  | fversion |
