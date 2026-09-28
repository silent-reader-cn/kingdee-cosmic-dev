# 应收基础资料模板-ar_rpa_settlescheme

## 应收基础资料模板-主表 t_ar_rpascheme

- **表名称：** 应收基础资料模板-主表
- **表名：** t_ar_rpascheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 12 | fexceplandesc | 执行计划 | varchar | 255 |  | √ | ' ' | 执行计划 |
| 13 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 14 | fexecuterid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_rpascheme |  | fid |
| 2 | idx_ar_rpas_number |  | fnumber |

---

## 组织单据体-子表 t_ar_rpaschemeorgentry

- **表名称：** 组织单据体-子表
- **表名：** t_ar_rpaschemeorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_rpaso_fid |  | fid |
| 2 | pk_t_ar_rpaschemeorgentry |  | fentryid |
| 3 | idx_ar_rpaso_org |  | forgid |

---

## 应收基础资料模板-多语言表 t_ar_rpascheme_l

- **表名称：** 应收基础资料模板-多语言表
- **表名：** t_ar_rpascheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_rpascheme_l |  | fpkid |
| 2 | idx_ar_rpasl_fid |  | fid,flocaleid |

---

## 规则单据体-子表 t_ar_rpascheruleentry

- **表名称：** 规则单据体-子表
- **表名：** t_ar_rpascheruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaindatesrc | 主方业务日期来源 | varchar | 255 |  | √ | ' ' | 主方业务日期来源 |
| 3 | fasstfilter | 辅方过滤条件 | varchar | 255 |  | √ | ' ' | 辅方过滤条件 |
| 4 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 apself :应付红蓝对冲 payself :付款红蓝对冲 aparsettle :应付冲应收 payrecsettle :付款冲退款 liqsettle :应付清理 recsettle :应收收款核销 arapsettle :应收冲应付 arself :应收红蓝对冲 recself :收款红蓝对冲 recpaysettle :收款冲退款 recclearing :收款清理 arliqsettle :应收清理 arpaymentsettle :应收退款核销 |
| 5 | fasstdatesrc | 辅方业务日期来源 | varchar | 255 |  | √ | ' ' | 辅方业务日期来源 |
| 6 | fmainfilter_tag | 主方过滤条件_详情 | text | 0 |  |  | null | 主方过滤条件_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftimeorder | 核销时间顺序 | varchar | 30 |  | √ | ' ' | 核销时间顺序,枚举: asc :按日期从前往后 desc :按日期从后往前 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmainbill | 主方单据 | varchar | 30 |  | √ | ' ' | 主方单据 |
| 11 | fmatchfieldinfo | 匹配字段信息 | varchar | 2000 |  | √ | ' ' | 匹配字段信息 |
| 12 | fasstbill | 辅方单据 | varchar | 30 |  | √ | ' ' | 辅方单据 |
| 13 | fmainfilter | 主方过滤条件 | varchar | 255 |  | √ | ' ' | 主方过滤条件 |
| 14 | fcurrencymatch | 币种匹配规则 | varchar | 5 |  | √ | '0' | 币种匹配规则,枚举: 0 :相同 |
| 15 | fasstactmatch | 往来单位匹配规则 | varchar | 5 |  | √ | ' ' | 往来单位匹配规则,枚举: 0 :相同 1 :可以不同 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fasstfilter_tag | 辅方过滤条件_详情 | text | 0 |  |  | null | 辅方过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_rpascheruleentry |  | fentryid |
| 2 | idx_ar_rpasr_fid |  | fid |
