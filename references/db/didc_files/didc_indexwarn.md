# 指标风险项-didc_indexwarn

## 指标风险项-主表 t_didc_indexwarn

- **表名称：** 指标风险项-主表
- **表名：** t_didc_indexwarn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frepeattime |  | int4 | 32 |  | √ | 0 |  |
| 3 | fdimensionid | 维度id | varchar | 500 |  | √ | ' ' | 维度id |
| 4 | fradiovalue | 默认时间维度精度 | varchar | 50 |  | √ | ' ' | 默认时间维度精度 |
| 5 | frepeatday |  | varchar | 50 |  | √ | ' ' | ,枚举: |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 7 | fcatalogueid | 所属指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 8 | fstatus | 启用 | varchar | 50 |  | √ | '1' | 启用 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fnumbervalue | 时间数 | varchar | 50 |  | √ | ' ' | 时间数 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fchannel | 发送 | varchar | 50 |  | √ | ' ' | 发送,枚举: |
| 13 | fplan | 风险项名称 | varchar | 50 |  | √ | ' ' | 风险项名称 |
| 14 | fdatetype | 维度时间类型 | varchar | 50 |  | √ | ' ' | 维度时间类型 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsuggest_tag | 行动建议_详情 | text | 0 |  |  | ' ' | 行动建议_详情 |
| 17 | fbillstatus | 风险项状态 | varchar | 50 |  | √ | ' ' | 风险项状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 19 | frisk | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级,枚举: 1 :高风险 2 :中风险 3 :低风险 |
| 20 | frequirementname_tag | 过滤条件_详情 | text | 0 |  |  | ' ' | 过滤条件_详情 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 22 | frepeatmode | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: DAY :每天 WEEK :每周 MONTH :每月 |
| 23 | frequirement | 目录条件json字符串 | varchar | 255 |  | √ | ' ' | 目录条件json字符串 |
| 24 | ftimetype | 默认时间维度类型 | varchar | 50 |  | √ | ' ' | 默认时间维度类型 |
| 25 | frequirement_tag | 目录条件json字符串_详情 | text | 0 |  |  | ' ' | 目录条件json字符串_详情 |
| 26 | frequirementname | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 27 | fcontent_tag | 消息内容_详情 | text | 0 |  |  | ' ' | 消息内容_详情 |
| 28 | findexcatalogue | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 29 | fsuggest | 行动建议 | varchar | 255 |  | √ | ' ' | 行动建议 |
| 30 | fcontent | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 31 | fnotice | 消息通知 | bpchar | 1 |  | √ | ' ' | 消息通知 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdimension | 分析维度 | varchar | 500 |  | √ | ' ' | 分析维度 |
| 34 | findextrend | 指标趋势 | varchar | 50 |  | √ | ' ' | 指标趋势,枚举: high :越高越好 low :越低越好 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indewarn |  | fcatalogueid |
| 2 | pk_t_didc_indexwarn |  | fid |

---

## 单据体-子表 t_didc_indexwarnentry

- **表名称：** 单据体-子表
- **表名：** t_didc_indexwarnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 值 | numeric | 23 | 10 | √ | 0 | 值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbasis | 依据 | varchar | 50 |  | √ | ' ' | 依据,枚举: 1 :指标值 2 :目标进度 3 :指标波动 4 :指标对比 |
| 5 | findexrequirement | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: |
| 6 | findexname | 指标名 | varchar | 50 |  | √ | ' ' | 指标名,枚举: |
| 7 | fsymbol |  | varchar | 50 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indexwarnentry |  | fid,fentryid |
| 2 | pk_t_didc_indexwarnentry |  | fentryid |

---

## 指标风险项-多语言表 t_didc_indexwarn_l

- **表名称：** 指标风险项-多语言表
- **表名：** t_didc_indexwarn_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fplan | 风险项名称 | varchar | 50 |  | √ | ' ' | 风险项名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indexwarn_l |  | fid |
| 2 | pk_t_didc_indexwarn_l |  | fpkid |

---

## 给-多选基础资料表 t_didc_warnuser

- **表名称：** 给-多选基础资料表
- **表名：** t_didc_warnuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_warnuser |  | fid |
| 2 | pk_t_didc_warnuser |  | fpkid |
