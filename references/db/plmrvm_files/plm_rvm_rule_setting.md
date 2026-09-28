# 评审完成转换规则配置-plm_rvm_rule_setting

## 评审完成转换规则配置-主表 t_plm_rvm_rule_settin

- **表名称：** 评审完成转换规则配置-主表
- **表名：** t_plm_rvm_rule_settin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frvmobj_type | 评审对象类型 | varchar | 50 |  | √ | ' ' | 评审对象类型,枚举: plm_prm_lc_status :产品路标 plm_rm_lc_status_mrd :MRD plm_rm_lc_status_prd :PRD plm_pm_projectstatus :项目 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frvmobj_status | 评审对象状态 | int8 | 64 |  | √ | 0 | 路标状态 plm_prm_lc_status |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | frvm_point | 评审点 | int8 | 64 |  | √ | 0 | [评审点 plm_qm_review_point](../plmrvm_files/plm_qm_review_point.md) |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_rule_settin |  | fid |
| 2 | idx_plm_rvm_rule_settin_m0 |  | fbillno |
