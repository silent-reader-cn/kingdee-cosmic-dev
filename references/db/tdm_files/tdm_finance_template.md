# 报表模板-tdm_finance_template

## 报表模板-主表 t_tdm_finance_tmpl

- **表名称：** 报表模板-主表
- **表名：** t_tdm_finance_tmpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftemplatetype | 报表类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_finance_tmpl |  | fid |
| 2 | idx_tdm_finance_tmpl |  | forgid,ftemplatetype |
| 3 | idx_t_tdm_finance_tmpl_createorg |  | fcreateorgid |
| 4 | idx_t_tdm_finance_tmpl_master |  | fmasterid |

---

## 报表项目-子表 t_tdm_finance_tempentry

- **表名称：** 报表项目-子表
- **表名：** t_tdm_finance_tempentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemtype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: tdm_item_lrb :利润表项目 tdm_item_xjllb :现金流量表项目 tdm_item_zcfzb :资产负债表项目 tdm_item_qybdb :所有者权益变动表项目 |
| 3 | famount3 | 金额3 | numeric | 23 | 10 | √ | 0 | 金额3 |
| 4 | famount2 | 金额2 | numeric | 23 | 10 | √ | 0 | 金额2 |
| 5 | famount1 | 金额1 | numeric | 23 | 10 | √ | 0 | 金额1 |
| 6 | fitem | 项目 | int8 | 64 |  | √ | 0 | 利润表项目 tdm_item_lrb |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freportitem | 项目1 | int8 | 64 |  | √ | 0 | 利润表项目 tdm_item_lrb |
| 9 | frownum | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_finance_tempentry_fk |  | fid |
| 2 | pk_tdm_finance_tempentry |  | fentryid |

---

## 报表模板-使用范围表 t_tdm_finance_tmpl_u

- **表名称：** 报表模板-使用范围表
- **表名：** t_tdm_finance_tmpl_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_finance_tmpl_u_uo |  | fuseorgid |
| 2 | pk_t_tdm_finance_tmpl_u |  | fdataid,fuseorgid |

---

## 报表模板-多语言表 t_tdm_finance_tmpl_l

- **表名称：** 报表模板-多语言表
- **表名：** t_tdm_finance_tmpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_finance_tmpl_l |  | fid,flocaleid |
| 2 | pk_tdm_finance_tmpl_l |  | fpkid |

---

## 报表模板-使用范围位图表 t_tdm_finance_tmpl_m

- **表名称：** 报表模板-使用范围位图表
- **表名：** t_tdm_finance_tmpl_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tdm_finance_tmpl_m |  | forgid |
