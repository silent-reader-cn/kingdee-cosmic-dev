# 规则取数卡片数据-bdtaxr_rule_fetch_card

## 规则取数卡片数据-主表 t_bdtaxr_rulefetch_card

- **表名称：** 规则取数卡片数据-主表
- **表名：** t_bdtaxr_rulefetch_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单元格汇总id | int8 | 64 |  | √ | 0 | 单元格汇总id |
| 2 | fadjustamount | 调整数值 | numeric | 23 | 10 | √ | 0 | 调整数值 |
| 3 | fcardname | 卡片名称 | varchar | 300 |  | √ | ' ' | 卡片名称 |
| 4 | ftotalamount | 总数 | numeric | 23 | 10 | √ | 0 | 总数 |
| 5 | ffetchorg | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 8 | famount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 9 | fadjustexplain | 调整说明 | varchar | 2000 |  | √ | ' ' | 调整说明 |
| 10 | frulename | 规则名称 | varchar | 300 |  | √ | ' ' | 规则名称 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_rulefetch_card |  | fentryid |
| 2 | idx_bdtaxr_rulefetch_card_fk |  | fid |

---

## 单据体-子表 t_bdtaxr_rulefetch_detail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_rulefetch_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 3 | fadvancedconfjson | fadvancedconfjson | text | 0 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffetchdirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fconditionjson | fconditionjson | text | 0 |  |  | null |  |
| 8 | fenddate | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 9 | fbizdimensionfilter | fbizdimensionfilter | text | 0 |  |  | null |  |
| 10 | fstartdate | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 12 | fabsolute | 绝对值 | varchar | 50 |  | √ | ' ' | 绝对值 |
| 13 | famounttype | famounttype | varchar | 50 |  | √ | ' ' |  |
| 14 | fdatasource | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 15 | foriginamount | 源金额 | numeric | 23 | 10 | √ | 0 | 源金额 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 19 | ffetchtype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_rulefetch_detail |  | fdetailid |
| 2 | idx_bdtaxr_rulefetch_detail_fk |  | fentryid |
