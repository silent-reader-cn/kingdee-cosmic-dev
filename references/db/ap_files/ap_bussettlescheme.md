# 暂估应付核销方案-ap_bussettlescheme

## 暂估应付核销方案-主表 t_ap_bussettlescheme

- **表名称：** 暂估应付核销方案-主表
- **表名：** t_ap_bussettlescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdefaultscheme | 默认方案 | bpchar | 1 |  | √ | ' ' | 默认方案 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 14 | fisallsame | 物料/费用项目/资产编码相同 | bpchar | 1 |  | √ | '0' | 物料/费用项目/资产编码相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_bussettlescheme |  | fid |
| 2 | idx_ap_bussettlescheme_number |  | fnumber |

---

## 暂估应付核销方案-多语言表 t_ap_bussettlescheme_l

- **表名称：** 暂估应付核销方案-多语言表
- **表名：** t_ap_bussettlescheme_l

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
| 1 | pk_t_ap_bussettlescheme_l |  | fpkid |
| 2 | idx_ap_bussettlescheme_fid |  | fid,flocaleid |

---

## 规则单据体-子表 t_ap_bussettleschemerule

- **表名称：** 规则单据体-子表
- **表名：** t_ap_bussettleschemerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlerelation | 核销关系 | varchar | 50 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 aparsettle :应付冲应收 payrecsettle :付款冲退款 aprecsettle :应付退款核销 apself :应付红蓝对冲 apbusfinsettle :暂估财务核销 apbusself :暂估红蓝核销 |
| 3 | fmatchrulevalue | 匹配规则 | varchar | 255 |  | √ | ' ' | 匹配规则 |
| 4 | fmatchrulevalue_tag | 匹配规则_详情 | text | 0 |  |  | null | 匹配规则_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmatchruledesc | 匹配规则 | varchar | 1000 |  | √ | ' ' | 匹配规则 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_bussettleschemer_fid |  | fid |
| 2 | pk_t_ap_bussettleschemerule |  | fentryid |

---

## 组织单据体-子表 t_ap_bussettleschemeorge

- **表名称：** 组织单据体-子表
- **表名：** t_ap_bussettleschemeorge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | forg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_bussettleschemeorge |  | fentryid |
| 2 | idx_ap_bussettleschemeo_fid |  | fid |
