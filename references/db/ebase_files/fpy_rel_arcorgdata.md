# 归档组织和数据关联表-fpy_rel_arcorgdata

## 归档组织和数据关联表-主表 tk_fpy_rel_arcorgdata

- **表名称：** 归档组织和数据关联表-主表
- **表名：** tk_fpy_rel_arcorgdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_ctrlstrategy | 管控策略 | varchar | 50 |  | √ | ' ' | 管控策略,枚举: 1 :全局共享 2 :按组织分配 |
| 3 | fk_fpy_data_pk | 对象数据id | int8 | 64 |  | √ | 0 | 对象数据id |
| 4 | fk_fpy_arcorg_pk | 归档组织id | int8 | 64 |  | √ | 0 | 归档组织id |
| 5 | fk_fpy_formid | formId | varchar | 50 |  | √ | ' ' | formId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_rel_arcorgdata |  | fid |
