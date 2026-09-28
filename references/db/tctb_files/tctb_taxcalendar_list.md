# 税务日历清单-tctb_taxcalendar_list

## 税务日历清单-主表 t_tctb_taxcalendar_list

- **表名称：** 税务日历清单-主表
- **表名：** t_tctb_taxcalendar_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjkjzrq | 缴款截止日期 | timestamp | 0 |  |  | null | 缴款截止日期 |
| 6 | ftaxyearid | 纳税期间 | int8 | 64 |  | √ | 0 | [纳税期间 tctb_taxyear](../tctb_files/tctb_taxyear.md) |
| 7 | ftaxareagroupid | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fdatefield1 | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | fsbjzrq | 申报截止日期 | timestamp | 0 |  |  | null | 申报截止日期 |
| 11 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftaxationsysid | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 16 | ftaxcycle | 纳税周期 | varchar | 50 |  | √ | ' ' | 纳税周期,枚举: month :月报 season :季报 halfyear :半年报 year :年报 |
| 17 | fperiodyear | 纳税期间起始年份 | int8 | 64 |  | √ | 0 | 纳税期间起始年份 |
| 18 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_calendar_list_01 |  | fbillno |
| 2 | pk_tctb_taxcalendar_list |  | fid |
