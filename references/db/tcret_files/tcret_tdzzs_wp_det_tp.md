# 土地增值税尾盘取数明细(暂存)-tcret_tdzzs_wp_det_tp

## 土地增值税尾盘取数明细(暂存)-主表 t_tcret_tdzzs_wp_det_tp

- **表名称：** 土地增值税尾盘取数明细(暂存)-主表
- **表名：** t_tcret_tdzzs_wp_det_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fdeclareitem | 尾盘申报项目id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 4 | forgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | ftaxaccountserialno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 13 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 15 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 16 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 18 | fbuildingtype | 房产类型id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fxmid | 项目id | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 21 | fdeclaretype | 申报类型id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 22 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 23 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 24 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 25 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_wp_det_tp |  | forgid,fskssqq,fskssqz |
| 2 | pk_tcret_tdzzs_wp_det_tp |  | fid |
