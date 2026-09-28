# 单据历史版本记录表-fcs_changehistory

## 单据历史版本记录表-主表 t_fcs_changehistory

- **表名称：** 单据历史版本记录表-主表
- **表名：** t_fcs_changehistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisapplycreate | 申请生成 | bpchar | 1 |  | √ | '0' | 申请生成 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbillinfo_tag | 修改的JSON信息_详情 | text | 0 |  |  | null | 修改的JSON信息_详情 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | freason | 修改原因 | varchar | 255 |  |  | ' ' | 修改原因 |
| 9 | fbizid | 业务单ID | int8 | 64 |  | √ | 0 | 业务单ID |
| 10 | flastversion | 是否最后一个版本 | bpchar | 1 |  | √ | '0' | 是否最后一个版本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbillinfo | 修改的JSON信息 | varchar | 255 |  |  | ' ' | 修改的JSON信息 |
| 13 | fseqnumber | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fapplyid | 申请单ID | int8 | 64 |  | √ | 0 | 申请单ID |
| 16 | fbizentity | 业务单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 17 | fapplybillno | 申请单编码 | varchar | 80 |  | √ | ' ' | 申请单编码 |
| 18 | fapplyentity | 申请单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_changehistory |  | fid |
| 2 | idx_fcs_changehistory |  | fbizid,fbizentity |
