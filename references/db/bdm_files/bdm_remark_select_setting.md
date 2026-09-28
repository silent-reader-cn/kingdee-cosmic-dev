# 已选备注设置-bdm_remark_select_setting

## 已选备注设置-主表 t_bdm_remark_select_set

- **表名称：** 已选备注设置-主表
- **表名：** t_bdm_remark_select_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremarktype | 备注类型 | bpchar | 1 |  | √ | ' ' | 备注类型,枚举: 0 :发票备注 1 :行备注 |
| 3 | fcreatetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 4 | fselectkey | 已选字段标识 | varchar | 50 |  | √ | ' ' | 已选字段标识 |
| 5 | fselectalias | 已选字段别名 | varchar | 50 |  | √ | ' ' | 已选字段别名 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fselectname | 已选字段名称 | varchar | 50 |  | √ | ' ' | 已选字段名称 |
| 8 | fselected | 是否已选 | bpchar | 1 |  | √ | ' ' | 是否已选,枚举: 1 :展示 0 :不展示 |
| 9 | fremarkid | 备注id | int8 | 64 |  | √ | 0 | 备注id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_remark_select_set |  | fid |
| 2 | idx_bdm_remark_select_set |  | forgid |
