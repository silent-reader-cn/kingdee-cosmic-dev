# 抽样方案-qcbd_sampscheme

## 接收信息单据体-子表 t_qcbd_recinfoentity

- **表名称：** 接收信息单据体-子表
- **表名：** t_qcbd_recinfoentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamppercentage | 抽样百分比% | numeric | 19 | 6 | √ | 0.000000 | 抽样百分比% |
| 3 | fsamplingsizecode | 样本量字码 | varchar | 50 |  | √ | ' ' | 样本量字码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fac | 允收数数值 | int8 | 64 |  | √ | 0 | 允收数数值 |
| 6 | fbatchinitialvalue | 起始值 | int8 | 64 |  |  | 0 | 起始值 |
| 7 | fentitystatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 8 | fbatchcutoffvalue | 截止值（含） | int8 | 64 |  |  | 0 | 截止值（含） |
| 9 | fstrictnessentry | 严格度 | varchar | 5 |  | √ | ' ' | 严格度,枚举: 1 :正常检验 2 :加严检验 3 :放宽检验 |
| 10 | fsamplingsize | 样本量 | int8 | 64 |  | √ | 0 | 样本量 |
| 11 | faqlvalueentry | AQL值 | varchar | 5 |  | √ | ' ' | AQL值,枚举: 1 :0.010 2 :0.015 3 :0.025 4 :0.040 5 :0.065 6 :0.10 7 :0.15 8 :0.25 9 :0.40 10 :0.65 11 :1.0 12 :1.5 13 :2.5 14 :4.0 15 :6.5 16 :10 17 :15 18 :25 19 :40 20 :65 21 :100 22 :150 23 :250 24 :400 25 :650 26 :1000 |
| 12 | finspectionlevelentry | 检验水平 | varchar | 5 |  | √ | ' ' | 检验水平,枚举: 1 :一般(Ⅰ) 2 :一般(Ⅱ) 3 :一般(Ⅲ) 4 :特殊(S-1) 5 :特殊(S-2) 6 :特殊(S-3) 7 :特殊(S-4) |
| 13 | fformula | 样本量计算公式 | varchar | 255 |  | √ | ' ' | 样本量计算公式 |
| 14 | finspectionrule | 抽样规则 | varchar | 5 |  | √ | ' ' | 抽样规则,枚举: A :全检 B :按比例 C :按固定数量 D :自定义抽样表 E :按计算公式 |
| 15 | fre | 拒收数 | int8 | 64 |  | √ | 0 | 拒收数 |
| 16 | facstr | 允收数 | varchar | 50 |  | √ | ' ' | 允收数 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_recinfoentity_fid |  | fid |
| 2 | t_qcbd_recinfoentity_pkey |  | fentryid |

---

## 抽样方案-多语言表 t_qcbd_sampscheme_l

- **表名称：** 抽样方案-多语言表
- **表名：** t_qcbd_sampscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcbd_sampscheme_l |  | fpkid |
| 2 | idx_qcbd_ss_l_fid |  | fid,flocaleid |

---

## 抽样方案-使用范围位图表 t_qcbd_sampscheme_m

- **表名称：** 抽样方案-使用范围位图表
- **表名：** t_qcbd_sampscheme_m

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
| 1 | pk_t_qcbd_sampscheme_m |  | forgid |

---

## 抽样方案-主表 t_qcbd_sampscheme

- **表名称：** 抽样方案-主表
- **表名：** t_qcbd_sampscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 抽样方案分类 qcbd_sampplangroup |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finspectionlevel | 检验水平 | varchar | 30 |  | √ | ' ' | 检验水平,枚举: 1 :一般(Ⅰ) 2 :一般(Ⅱ) 3 :一般(Ⅲ) 4 :特殊(S-1) 5 :特殊(S-2) 6 :特殊(S-3) 7 :特殊(S-4) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 14 | fstrictness | 严格度 | varchar | 30 |  | √ | ' ' | 严格度,枚举: 1 :正常检验 2 :加严检验 3 :放宽检验 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fsamplingtype | 抽样类型 | varchar | 30 |  | √ | ' ' | 抽样类型,枚举: 1 :百分比抽检 2 :固定数抽检 3 :按国标抽检 4 :公式定义抽检 5 :全检 6 :免检 7 :自定义抽检 |
| 19 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 23 | faqlvalue | AQL值 | varchar | 30 |  | √ | ' ' | AQL值,枚举: 0.010 :0.010 0.015 :0.015 0.025 :0.025 0.040 :0.040 0.065 :0.065 0.10 :0.10 0.15 :0.15 0.25 :0.25 0.40 :0.40 0.65 :0.65 1.0 :1.0 1.5 :1.5 2.5 :2.5 4.0 :4.0 6.5 :6.5 10 :10 15 :15 25 :25 40 :40 65 :65 100 :100 150 :150 250 :250 400 :400 650 :650 1000 :1000 |
| 24 | finspectiontype | finspectiontype | varchar | 30 |  | √ | ' ' |  |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcbd_sampscheme |  | fid |
| 2 | uidx_qcbd_sampscheme_billno |  | fnumber |
| 3 | idx_t_qcbd_sampscheme_createorg |  | fcreateorgid |
| 4 | idx_t_qcbd_sampscheme_master |  | fmasterid |

---

## 抽样方案-使用范围表 t_qcbd_sampscheme_u

- **表名称：** 抽样方案-使用范围表
- **表名：** t_qcbd_sampscheme_u

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
| 1 | t_qcbd_sampscheme_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_sampscheme_u_uo |  | fuseorgid |
