# 活动结果记录单-ocmem_activityresult

## 活动结果记录单-主表 t_ocmem_activityresult

- **表名称：** 活动结果记录单-主表
- **表名：** t_ocmem_activityresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyuserqty | 购买人数 | numeric | 23 | 10 | √ | 0 | 购买人数 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbuyamount | 购买金额 | numeric | 23 | 10 | √ | 0 | 购买金额 |
| 6 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fuserqty | 参加人数 | numeric | 23 | 10 | √ | 0 | 参加人数 |
| 8 | fimplementation_tag | 执行状况_详情 | text | 0 |  |  | null | 执行状况_详情 |
| 9 | fimplementation | 执行状况 | text | 0 |  |  | null | 执行状况 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpicture6 | 照片6 | varchar | 255 |  | √ | ' ' | 照片6 |
| 13 | fpicture5 | 照片5 | varchar | 255 |  | √ | ' ' | 照片5 |
| 14 | fdeptid | 执行部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fpicture4 | 照片4 | varchar | 255 |  | √ | ' ' | 照片4 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fpicture3 | 照片3 | varchar | 255 |  | √ | ' ' | 照片3 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fpicture2 | 照片2 | varchar | 255 |  | √ | ' ' | 照片2 |
| 20 | factivitystatus | 活动状态 | bpchar | 1 |  | √ | ' ' | 活动状态,枚举: A :计划 B :已完成 C :进行中 D :已取消 E :已结案 |
| 21 | fpicture1 | 照片1 | varchar | 255 |  | √ | ' ' | 照片1 |
| 22 | fuserid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | factivitybillid | 营销活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_activityresult |  | factivitybillid |
| 2 | pk_ocmem_activityresult |  | fid |
