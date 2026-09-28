# 从价房产原值分摊信息-tcret_cjfcyzft_info

## 从价房产原值分摊信息-主表 t_tcret_cjfcyzft_info

- **表名称：** 从价房产原值分摊信息-主表
- **表名：** t_tcret_cjfcyzft_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 房产名称 | varchar | 50 |  | √ | ' ' | 房产名称 |
| 4 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fadjustedvalue | 调整后房产原值 | numeric | 23 | 10 | √ | 0 | 调整后房产原值 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fhousemanagement | 房产属地管理 | int8 | 64 |  | √ | 0 | 房产税属地管理 tpo_tcret_fcs_apanage |
| 11 | fenddate | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fadjustedrentvalue | 调整后出租房产原值 | numeric | 23 | 10 | √ | 0 | 调整后出租房产原值 |
| 14 | fcjjzratiomethod | 从价计征比例计算方法 | varchar | 50 |  | √ | ' ' | 从价计征比例计算方法,枚举: rentarea :出租面积倒挤占比 selfuse :自用空置公摊占比 |
| 15 | fstartdate | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 16 | ftaxpaylimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 |
| 17 | fenable | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 房产编码 | int8 | 64 |  | √ | 0 | [房产基础信息 tdm_fcs_basic_info](../tdm_files/tdm_fcs_basic_info.md) |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fadjustedcjjzvalue | 调整后从价计征房产原值 | numeric | 23 | 10 | √ | 0 | 调整后从价计征房产原值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cjfcyzft_org_number_date |  | forg,fnumber,fstartdate,fenddate |
| 2 | pk_tcret_cjfcyzft_info |  | fid |

---

## 单据体-子表 t_tcret_cjmjft_area

- **表名称：** 单据体-子表
- **表名：** t_tcret_cjmjft_area

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcjjzratio | 从价计征比例 | numeric | 23 | 10 | √ | 0 | 从价计征比例 |
| 3 | fvacancyarea | 空置面积 | numeric | 23 | 10 | √ | 0 | 空置面积 |
| 4 | fassertvalue | 房产原值 | numeric | 23 | 10 | √ | 0 | 房产原值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frentarea | 出租面积 | numeric | 23 | 10 | √ | 0 | 出租面积 |
| 7 | fselfusearea | 自用面积 | numeric | 23 | 10 | √ | 0 | 自用面积 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fpublicarea | 公摊面积 | numeric | 23 | 10 | √ | 0 | 公摊面积 |
| 11 | fperiod | 期间 | timestamp | 0 |  |  | null | 期间 |
| 12 | farea | 房产建筑面积 | numeric | 23 | 10 | √ | 0 | 房产建筑面积 |
| 13 | fcjjzassertvalue | 从价计征房产原值 | numeric | 23 | 10 | √ | 0 | 从价计征房产原值 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_cjmjft_area_fk |  | fid |
| 2 | pk_tcret_cjmjft_area |  | fentryid |
