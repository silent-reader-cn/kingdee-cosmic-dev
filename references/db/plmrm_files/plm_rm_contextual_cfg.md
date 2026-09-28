# 需求上下文关系配置-plm_rm_contextual_cfg

## 需求上下文关系配置-主表 t_ipd_contextual_cfgs

- **表名称：** 需求上下文关系配置-主表
- **表名：** t_ipd_contextual_cfgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisrm | 是否需求类 | bpchar | 1 |  | √ | '0' | 是否需求类 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fshow | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsourcemodel | 源工作项 | varchar | 50 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 11 | ftargetmodel | 目标工作项 | varchar | 50 |  | √ | ' ' | [业务对象列表_可多选 bos_flydb_objlist](../superquery_files/bos_flydb_objlist.md) |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_contextual_cfgs_m0 |  | fbillno |
| 2 | idx_t_ipd_contextual_cfgs |  | fsourcemodel,ftargetmodel |
| 3 | pk_ipd_contextual_cfgs |  | fid |
