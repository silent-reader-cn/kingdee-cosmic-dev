# 规则取数汇总数据-rdem_rule_fetch_summary

## 卡片明细-子表 t_rdem_rulefetch_detail

- **表名称：** 卡片明细-子表
- **表名：** t_rdem_rulefetch_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 rdem_datasource_entry |
| 2 | fadvancedconfjson | 高级配置JSON | varchar | 2000 |  | √ | ' ' | 高级配置JSON |
| 3 | ffetchdirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconditionjson | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fenddate | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 8 | ffetchamount | 取数金额 | numeric | 23 | 2 | √ | 0 | 取数金额 |
| 9 | fstartdate | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 10 | famounttype | 金额字段基础资料类型 | varchar | 50 |  | √ | ' ' | 金额字段基础资料类型,枚举: rdem_datasource_entry :数据源字段配置 rdem_col_member :列维成员管理 |
| 11 | fabsolute | 绝对值 | varchar | 50 |  | √ | ' ' | 绝对值 |
| 12 | fdatasource | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 13 | foriginamount | 源金额 | numeric | 23 | 2 | √ | 0 | 源金额 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | ffetchtype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rulefetch_detail |  | fdetailid |
| 2 | idx_rdem_rulefetch_detail_fk |  | fentryid |

---

## 卡片-子表 t_rdem_rulefetch_card

- **表名称：** 卡片-子表
- **表名：** t_rdem_rulefetch_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustamount | 调整数值 | numeric | 23 | 2 | √ | 0 | 调整数值 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fcardname | 卡片名称 | varchar | 50 |  | √ | ' ' | 卡片名称 |
| 4 | ftotalamount | 总数 | numeric | 23 | 2 | √ | 0 | 总数 |
| 5 | ffetchorg | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 8 | fadjustexplain | 调整说明 | varchar | 2000 |  | √ | ' ' | 调整说明 |
| 9 | famount | 取数金额 | numeric | 23 | 2 | √ | 0 | 取数金额 |
| 10 | frulename | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rulefetch_card |  | fentryid |
| 2 | idx_rdem_rulefetch_card_fk |  | fid |

---

## 规则取数汇总数据-主表 t_rdem_rulefetch_sum

- **表名称：** 规则取数汇总数据-主表
- **表名：** t_rdem_rulefetch_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frulefetchmainid | 规则取数主表id | int8 | 64 |  | √ | 0 | 规则取数主表id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | flastamount | 结果值 | numeric | 23 | 10 | √ | 0 | 结果值 |
| 6 | freportitem | 报表项 | varchar | 100 |  | √ | ' ' | 报表项 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 8 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 9 | fadjustamount | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 10 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | foriginamount | 原数值 | numeric | 23 | 10 | √ | 0 | 原数值 |
| 13 | fruleitem | 规则项目类型 | varchar | 200 |  | √ | ' ' | 规则项目类型 |
| 14 | fruleid | 规则id | varchar | 500 |  | √ | ' ' | 规则id |
| 15 | fruletable | 规则表 | varchar | 100 |  | √ | ' ' | 规则表 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_rulefetch_sum_m0 |  | freportitem |
| 2 | pk_rdem_rulefetch_sum |  | fid |

---

## 调整记录-子表 t_rdem_rulefetch_edit

- **表名称：** 调整记录-子表
- **表名：** t_rdem_rulefetch_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustamount | 调整数值 | numeric | 23 | 2 | √ | 0 | 调整数值 |
| 2 | fcreator | 调整人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fpreadjust | 调整前数值 | numeric | 23 | 2 | √ | 0 | 调整前数值 |
| 5 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: 1 :数据源调整 2 :手工录入调整 |
| 6 | fcreatetime | 调整时间 | timestamp | 0 |  |  | null | 调整时间 |
| 7 | fpostadjust | 调整后数值 | numeric | 23 | 2 | √ | 0 | 调整后数值 |
| 8 | ffetchorg | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fadjustexplain | 调整说明 | varchar | 2000 |  | √ | ' ' | 调整说明 |
| 11 | frulename | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rulefetch_edit |  | fentryid |
| 2 | idx_rdem_rulefetch_edit_fk |  | fid |
