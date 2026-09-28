# 发票领购-sim_inv_apply

## 发票领购-主表 t_sim_inv_apply

- **表名称：** 发票领购-主表
- **表名：** t_sim_inv_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremainquantity | 剩余份数合计 | int8 | 64 |  | √ | 0 | 剩余份数合计 |
| 3 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :普通电子发票 027 :专用电子发票 |
| 4 | favailablequantity | 可领用数量 | int8 | 64 |  | √ | 0 | 可领用数量 |
| 5 | fapplypurchasequantity | 申请领购数量 | int8 | 64 |  | √ | 0 | 申请领购数量 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 企业管理 bdm_org |
| 7 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 8 | fconductor | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_inv_apply |  | fid |
| 2 | idx_sim_inv_apply |  | fepinfo |
