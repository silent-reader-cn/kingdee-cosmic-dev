# 自定义分类的关系表-fpy_business_relation

## 自定义分类的关系表-主表 tk_fpy_business_relation

- **表名称：** 自定义分类的关系表-主表
- **表名：** tk_fpy_business_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 3 | fk_fpy_child_pk | 子级主键ID | int8 | 64 |  | √ | 0 | 子级主键ID |
| 4 | fk_fpy_child_busnum | 子级分类编码 | varchar | 50 |  | √ | ' ' | 子级分类编码 |
| 5 | fk_fpy_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 6 | fk_fpy_parent_pk | 父级主键ID | int8 | 64 |  | √ | 0 | 父级主键ID |
| 7 | fk_fpy_parent_busnum | 父级分类编码 | varchar | 50 |  | √ | ' ' | 父级分类编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_business_relation |  | fid |
