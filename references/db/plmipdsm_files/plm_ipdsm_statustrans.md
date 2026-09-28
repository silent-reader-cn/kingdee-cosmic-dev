# 状态转换规则配置-plm_ipdsm_statustrans

## 状态转换规则配置-主表 t_plm_ipdsm_statustrans

- **表名称：** 状态转换规则配置-主表
- **表名：** t_plm_ipdsm_statustrans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcstatusid | 源工作项状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 4 | fsrcitemid | 源工作项 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftaritemid | 目标工作项 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 10 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: validate :校验 linkage :联动 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftarstatus | 目标工作项状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fscope | 影响范围 | varchar | 50 |  | √ | ' ' | 影响范围,枚举: relate :关联项 context :上下文 relate,context :关联项和上下文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_statustrans |  | fid |
| 2 | idx_plm_ipdsm_statustrans_m0 |  | fbillno |
