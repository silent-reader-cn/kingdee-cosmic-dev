# 显示方案-amccsa_displayscheme

## 显示方案-主表 t_amccsa_displayscheme

- **表名称：** 显示方案-主表
- **表名：** t_amccsa_displayscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fschdinfoconfig | 计划信息 | varchar | 50 |  | √ | ' ' | 计划信息,枚举: 0 :行号 1 :物料编码 2 :物料名称 3 :规格型号 4 :客户物料编码 5 :客户物料名称 6 :客户物料规格型号 7 :物料版本 8 :辅助属性 9 :客户参考值 10 :客户采购订单号 11 :年份型号 12 :销售单位 13 :发放号 14 :单据状态 15 :前期累计截止日 16 :前期累计需求量 17 :默认交货时间 |
| 6 | fdefaultscheme | 默认方案 | varchar | 50 |  | √ | ' ' | 默认方案,枚举: 0 :是 1 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_amccsa_displayscheme_m0 |  | fschdinfoconfig |
| 2 | pk_amccsa_displayscheme |  | fid |
