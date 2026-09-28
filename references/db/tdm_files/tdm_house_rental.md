# 房产出租台账-tdm_house_rental

## 房产出租台账-主表 t_tdm_house_rental_entity

- **表名称：** 房产出租台账-主表
- **表名：** t_tdm_house_rental_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 房产出租信息 | int8 | 64 |  | √ | 0 | [房产出租信息 tdm_house_rental_info](../tdm_files/tdm_house_rental_info.md) |
| 2 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frentmonth | 合同约定租期（月份数） | int8 | 64 |  | √ | 0 | 合同约定租期（月份数） |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fhouserentalinfo | fhouserentalinfo | int8 | 64 |  | √ | 0 |  |
| 7 | frentalincome | frentalincome | numeric | 23 | 10 | √ | 0 |  |
| 8 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fenddate | 申报租金起止.结束 | timestamp | 0 |  |  | null | 申报租金起止.结束 |
| 10 | fhirearea | 出租面积（㎡） | numeric | 23 | 10 | √ | 0 | 出租面积（㎡） |
| 11 | fstartdate | 申报租金起止.开始 | timestamp | 0 |  |  | null | 申报租金起止.开始 |
| 12 | ftenantry | 承租方名称 | varchar | 200 |  | √ | ' ' | 承租方名称 |
| 13 | feachrentincome | 每期申报租金收入 | numeric | 23 | 10 | √ | 0 | 每期申报租金收入 |
| 14 | frentincome | 租金收入（元） | numeric | 23 | 10 | √ | 0 | 租金收入（元） |
| 15 | fhiretaxcode | 承租方纳税人识别号 | varchar | 50 |  | √ | ' ' | 承租方纳税人识别号 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_house_rental_entity_fk |  | fid |
| 2 | pk_tdm_house_rental_entity |  | fentryid |
