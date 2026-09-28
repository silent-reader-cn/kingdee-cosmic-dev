# 应付付款核销方案-ap_settlescheme

## 应付付款核销方案-主表 t_ap_settlescheme

- **表名称：** 应付付款核销方案-主表
- **表名：** t_ap_settlescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 160 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 10 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 11 | fexecuterid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_ss_number |  | fnumber |
| 2 | t_ap_settlescheme_pkey |  | fid |

---

## 组织单据体-子表 t_ap_settleschemeorgentry

- **表名称：** 组织单据体-子表
- **表名：** t_ap_settleschemeorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sso_fid |  | fid |
| 2 | t_ap_settleschemeorgentry_pkey |  | fentryid |
| 3 | idx_ap_sso_org |  | forgid |

---

## 应付付款核销方案-多语言表 t_ap_settlescheme_l

- **表名称：** 应付付款核销方案-多语言表
- **表名：** t_ap_settlescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_ssl_fid |  | fid |
| 2 | t_ap_settlescheme_l_pkey |  | fpkid |

---

## 规则单据体-子表 t_ap_settlescheruleentry

- **表名称：** 规则单据体-子表
- **表名：** t_ap_settlescheruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaindatesrc | 主方业务日期来源 | varchar | 255 |  | √ | ' ' | 主方业务日期来源 |
| 3 | fasstfilter | 辅方过滤条件 | varchar | 255 |  | √ | ' ' | 辅方过滤条件 |
| 4 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 apself :应付红蓝对冲 payself :付款红蓝对冲 aparsettle :应付冲应收 payrecsettle :付款冲退款 |
| 5 | fasstdatesrc | 辅方业务日期来源 | varchar | 255 |  | √ | ' ' | 辅方业务日期来源 |
| 6 | fmainfilter_tag | 主方过滤条件_详情 | text | 0 |  |  | null | 主方过滤条件_详情 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ftimeorder | 核销时间顺序 | varchar | 30 |  | √ | ' ' | 核销时间顺序,枚举: asc :按日期从前往后 desc :按日期从后往前 |
| 9 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 10 | fmatchfieldinfo | 匹配字段信息 | varchar | 2000 |  |  | null | 匹配字段信息 |
| 11 | fasstbill | 辅方单据 | varchar | 30 |  | √ | ' ' | 辅方单据 |
| 12 | fmainfilter | 主方过滤条件 | varchar | 255 |  | √ | ' ' | 主方过滤条件 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fasstfilter_tag | 辅方过滤条件_详情 | text | 0 |  |  | null | 辅方过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settlescheruleentry_pkey |  | fentryid |
| 2 | idx_ap_ssr_fid |  | fid |
