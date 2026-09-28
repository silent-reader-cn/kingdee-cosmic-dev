# 订单计划控制规则-ocbsoc_orderpcrule

## 订单计划控制规则-主表 t_ocbsoc_orderpcrule

- **表名称：** 订单计划控制规则-主表
- **表名：** t_ocbsoc_orderpcrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmthplandatatype | 本月计划取数 | bpchar | 1 |  | √ | ' ' | 本月计划取数,枚举: A :按渠道销售计划 B :按省区销售计划 C :按大区销售计划 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcontrolintensity | 计划外订单控制强度 | bpchar | 1 |  | √ | ' ' | 计划外订单控制强度,枚举: N :不控制 W :预警提示 C :取消交易 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 17 | fcontroltime | 计划外订单控制时点 | bpchar | 1 |  | √ | ' ' | 计划外订单控制时点,枚举: A :保存 B :提交 C :审核 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_orderpcrule |  | fid |
| 2 | idx_ocbsoc_orderpcrule |  | fnumber |

---

## 订单计划控制规则-多语言表 t_ocbsoc_orderpcrule_l

- **表名称：** 订单计划控制规则-多语言表
- **表名：** t_ocbsoc_orderpcrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_ordpcre_flid |  | fid,flocaleid |
| 2 | pk_ocbsoc_orderpcrule_l |  | fpkid |

---

## 本月有效数量取数设置-子表 t_ocbsoc_orderpcrule_e

- **表名称：** 本月有效数量取数设置-子表
- **表名：** t_ocbsoc_orderpcrule_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialcol | 物料字段标识 | varchar | 100 |  | √ | ' ' | 物料字段标识 |
| 3 | fitemcolname | 商品字段 | varchar | 100 |  | √ | ' ' | 商品字段 |
| 4 | fdeptcolname | 计划部门取数 | varchar | 100 |  | √ | ' ' | 计划部门取数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentityobjectid | 单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fstatfieldformula | 统计字段表达式 | varchar | 2000 |  | √ | ' ' | 统计字段表达式 |
| 8 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 9 | fdatecol | 时间取数标识 | varchar | 100 |  | √ | ' ' | 时间取数标识 |
| 10 | fdeptcol | 计划部门取数标识 | varchar | 100 |  | √ | ' ' | 计划部门取数标识 |
| 11 | fdatecolname | 时间取数 | varchar | 100 |  | √ | ' ' | 时间取数 |
| 12 | fstatfieldname | 统计字段 | varchar | 100 |  | √ | ' ' | 统计字段 |
| 13 | fcondition | 条件 | text | 0 |  |  | null | 条件 |
| 14 | fdatasource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: A :源单字段 B :计算公式 |
| 15 | fstatfieldcol | 统计字段标识 | varchar | 100 |  | √ | ' ' | 统计字段标识 |
| 16 | fconditionfilter_tag | 条件_详情 | text | 0 |  |  | null | 条件_详情 |
| 17 | fmaterialcolname | 物料字段 | varchar | 100 |  | √ | ' ' | 物料字段 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fitemcol | 商品字段标识 | varchar | 100 |  | √ | ' ' | 商品字段标识 |
| 20 | fconditionfilter | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_ordpcre_e |  | fid |
| 2 | pk_ocbsoc_orderpcrule_e |  | fentryid |
