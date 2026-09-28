# 渠道目标单-occbo_channelgoalsbill

## 渠道目标单-主表 t_occbo_channelgoals

- **表名称：** 渠道目标单-主表
- **表名：** t_occbo_channelgoals

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 目标说明 | varchar | 255 |  | √ | ' ' | 目标说明 |
| 3 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fgoalsyearid | 目标年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 9 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fisautocalculate | 自动统计目标值 | bpchar | 1 |  | √ | '1' | 自动统计目标值 |
| 12 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fgoalstype | 目标类型 | bpchar | 1 |  | √ | ' ' | 目标类型,枚举: A :年度目标 B :月度目标 |
| 17 | fgoalsmap | 年月对应分录关系 | varchar | 2000 |  | √ | ' ' | 年月对应分录关系 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 目标编号 | varchar | 80 |  | √ | ' ' | 目标编号 |
| 20 | fdimension | KPI维度 | bpchar | 1 |  | √ | '1' | KPI维度,枚举: 0 :金额 1 :数量 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fkpiid | KPI | int8 | 64 |  | √ | 0 | KPI occbo_kpi_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals |  | fbillno |
| 2 | pk_occbo_channelgoals |  | fid |

---

## 渠道目标单-多语言表 t_occbo_channelgoals_l

- **表名称：** 渠道目标单-多语言表
- **表名：** t_occbo_channelgoals_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_l |  | fid,flocaleid |
| 2 | pk_occbo_channelgoals_l |  | fpkid |

---

## 目标详情-子表 t_occbo_chlgoals_entry

- **表名称：** 目标详情-子表
- **表名：** t_occbo_chlgoals_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoalsnum12 | 目标值12 | numeric | 23 | 10 | √ | 0 | 目标值12 |
| 3 | fgoalsnum11 | 目标值11 | numeric | 23 | 10 | √ | 0 | 目标值11 |
| 4 | fgoalsnum14 | 目标值14 | numeric | 23 | 10 | √ | 0 | 目标值14 |
| 5 | fgoalsnum13 | 目标值13 | numeric | 23 | 10 | √ | 0 | 目标值13 |
| 6 | fgoalsnum10 | 目标值10 | numeric | 23 | 10 | √ | 0 | 目标值10 |
| 7 | factualnum1 | 实际值1 | numeric | 23 | 10 | √ | 0 | 实际值1 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchannelid | 经销商 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fgoalsnum16 | 目标值16 | numeric | 23 | 10 | √ | 0 | 目标值16 |
| 12 | fgoalsnum15 | 目标值15 | numeric | 23 | 10 | √ | 0 | 目标值15 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fentrytotalnum | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 15 | factualnum9 | 实际值9 | numeric | 23 | 10 | √ | 0 | 实际值9 |
| 16 | factualnum8 | 实际值8 | numeric | 23 | 10 | √ | 0 | 实际值8 |
| 17 | fgoalsnum8 | 目标值8 | numeric | 23 | 10 | √ | 0 | 目标值8 |
| 18 | factualnum7 | 实际值7 | numeric | 23 | 10 | √ | 0 | 实际值7 |
| 19 | fgoalsnum9 | 目标值9 | numeric | 23 | 10 | √ | 0 | 目标值9 |
| 20 | factualnum6 | 实际值6 | numeric | 23 | 10 | √ | 0 | 实际值6 |
| 21 | fgoalsnum6 | 目标值6 | numeric | 23 | 10 | √ | 0 | 目标值6 |
| 22 | factualnum5 | 实际值5 | numeric | 23 | 10 | √ | 0 | 实际值5 |
| 23 | fgoalsnum7 | 目标值7 | numeric | 23 | 10 | √ | 0 | 目标值7 |
| 24 | factualnum4 | 实际值4 | numeric | 23 | 10 | √ | 0 | 实际值4 |
| 25 | fgoalsnum4 | 目标值4 | numeric | 23 | 10 | √ | 0 | 目标值4 |
| 26 | factualnum3 | 实际值3 | numeric | 23 | 10 | √ | 0 | 实际值3 |
| 27 | fgoalsnum5 | 目标值5 | numeric | 23 | 10 | √ | 0 | 目标值5 |
| 28 | factualnum2 | 实际值2 | numeric | 23 | 10 | √ | 0 | 实际值2 |
| 29 | fgoalsnum2 | 目标值2 | numeric | 23 | 10 | √ | 0 | 目标值2 |
| 30 | factualnum15 | 实际值15 | numeric | 23 | 10 | √ | 0 | 实际值15 |
| 31 | fgoalsnum3 | 目标值3 | numeric | 23 | 10 | √ | 0 | 目标值3 |
| 32 | factualnum16 | 实际值16 | numeric | 23 | 10 | √ | 0 | 实际值16 |
| 33 | factualnum13 | 实际值13 | numeric | 23 | 10 | √ | 0 | 实际值13 |
| 34 | fgoalsnum1 | 目标值1 | numeric | 23 | 10 | √ | 0 | 目标值1 |
| 35 | factualnum14 | 实际值14 | numeric | 23 | 10 | √ | 0 | 实际值14 |
| 36 | factualnum11 | 实际值11 | numeric | 23 | 10 | √ | 0 | 实际值11 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | factualnum12 | 实际值12 | numeric | 23 | 10 | √ | 0 | 实际值12 |
| 39 | factualnum10 | 实际值10 | numeric | 23 | 10 | √ | 0 | 实际值10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_entry |  | fchannelid |
| 2 | pk_occbo_chlgoals_entry |  | fentryid |

---

## 目标月度-多选基础资料表 t_occbo_chlgoals_rp

- **表名称：** 目标月度-多选基础资料表
- **表名：** t_occbo_chlgoals_rp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_chlgoals_rp |  | fpkid |
| 2 | idx_occbo_chlgoals_rp |  | fid,fbasedataid |

---

## 目标详情-分表 t_occbo_chlgoals_entry_a

- **表名称：** 目标详情-分表
- **表名：** t_occbo_chlgoals_entry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompletionrate6 | 完成率6 | varchar | 50 |  | √ | ' ' | 完成率6 |
| 3 | fcompletionrate15 | 完成率15 | varchar | 50 |  | √ | ' ' | 完成率15 |
| 4 | fcompletionrate7 | 完成率7 | varchar | 50 |  | √ | ' ' | 完成率7 |
| 5 | fcompletionrate16 | 完成率16 | varchar | 50 |  | √ | ' ' | 完成率16 |
| 6 | fcompletionrate8 | 完成率8 | varchar | 50 |  | √ | ' ' | 完成率8 |
| 7 | fcompletionrate13 | 完成率13 | varchar | 50 |  | √ | ' ' | 完成率13 |
| 8 | fcompletionrate9 | 完成率9 | varchar | 50 |  | √ | ' ' | 完成率9 |
| 9 | fcompletionrate14 | 完成率14 | varchar | 50 |  | √ | ' ' | 完成率14 |
| 10 | fcompletionrate2 | 完成率2 | varchar | 50 |  | √ | ' ' | 完成率2 |
| 11 | fcompletionrate11 | 完成率11 | varchar | 50 |  | √ | ' ' | 完成率11 |
| 12 | fcompletionrate3 | 完成率3 | varchar | 50 |  | √ | ' ' | 完成率3 |
| 13 | fcompletionrate12 | 完成率12 | varchar | 50 |  | √ | ' ' | 完成率12 |
| 14 | fcompletionrate4 | 完成率4 | varchar | 50 |  | √ | ' ' | 完成率4 |
| 15 | fcompletionrate5 | 完成率5 | varchar | 50 |  | √ | ' ' | 完成率5 |
| 16 | fcompletionrate10 | 完成率10 | varchar | 50 |  | √ | ' ' | 完成率10 |
| 17 | fcompletionrate1 | 完成率1 | varchar | 50 |  | √ | ' ' | 完成率1 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_entry_a |  | fid |
| 2 | pk_occbo_chlgoals_entry_a |  | fentryid |
