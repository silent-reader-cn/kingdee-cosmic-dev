# 土地增值税预缴取数明细-tcret_tdzzs_yj_det

## 土地增值税预缴取数明细-主表 t_tcret_tdzzs_yj_det

- **表名称：** 土地增值税预缴取数明细-主表
- **表名：** t_tcret_tdzzs_yj_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | forgid | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 6 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 11 | ftaxaccountserialno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 12 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 13 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 14 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 15 | fincometype | 申报收入类型id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 16 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 18 | fbuildingtype | 房产类型id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdeclaretype | 申报类型id | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 21 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 22 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 23 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 24 | fyjxm | 项目id | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 25 | fsubbuildingtype | 房产类型子目id | int8 | 64 |  | √ | 0 | [房产类型子目 tcret_tdzzs_fclxzm](../tcret_files/tcret_tdzzs_fclxzm.md) |
| 26 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :含税价换算不含税价 cysldsqs :税额换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_yj_det |  | fid |
| 2 | idx_tcret_tdzzs_yj_det_yjxm |  | fyjxm |
