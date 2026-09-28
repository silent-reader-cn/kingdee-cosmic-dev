# 成本BOM-scax_costbom

## 联副产品-多语言表 t_scax_costbomcopentry_l

- **表名称：** 联副产品-多语言表
- **表名：** t_scax_costbomcopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_costbomcopentry_l |  | fentryid,flocaleid |
| 2 | pk_scax_costbomcopentry_l |  | fpkid |

---

## 组件信息-子表 t_scax_costbomentry

- **表名称：** 组件信息-子表
- **表名：** t_scax_costbomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 5 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0 | 用量：分母 |
| 6 | fmaterialid | 子项物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0 | 用量：分子 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fmaterialinfoid | 子项编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fbaseqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0 | 基本单位用量：分子 |
| 12 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 13 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbaseqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0 | 基本单位用量：分母 |
| 15 | ftype | 子项类型 | varchar | 30 |  | √ | ' ' | 子项类型,枚举: A :库存 |
| 16 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_bomentry |  | fid |
| 2 | pk_scax_costbomentry |  | fentryid |

---

## 成本BOM-多语言表 t_scax_costbom_l

- **表名称：** 成本BOM-多语言表
- **表名：** t_scax_costbom_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costbom_l |  | fpkid |
| 2 | idx_scax_costbom_l |  | fid,flocaleid |

---

## 成本BOM-主表 t_scax_costbom

- **表名称：** 成本BOM-主表
- **表名：** t_scax_costbom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterialid | 主产品物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | fmaterialinfoid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 7 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 8 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 20 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 1 :逐级分配 2 :自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 26 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | BOM编码 | varchar | 80 |  | √ | ' ' | BOM编码 |
| 29 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scax_costbom_master |  | fmasterid |
| 2 | idx_scax_costbom_number |  | fnumber |
| 3 | pk_scax_costbom |  | fid |
| 4 | idx_scax_costbom |  | fmaterialid |
| 5 | idx_t_scax_costbom_createorg |  | fcreateorgid |

---

## 成本BOM-使用范围表 t_scax_costbom_u

- **表名称：** 成本BOM-使用范围表
- **表名：** t_scax_costbom_u

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
| 1 | idx_t_scax_costbom_u_uo |  | fuseorgid |
| 2 | pk_t_scax_costbom_u |  | fdataid,fuseorgid |

---

## 联副产品-子表 t_scax_costbomcopentry

- **表名称：** 联副产品-子表
- **表名：** t_scax_costbomcopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcopentrytype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 3 | fcopentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fcopentryvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 5 | fcopentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 6 | fcopentryunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcopentrycostweight | 成本权重% | numeric | 23 | 10 | √ | 0 | 成本权重% |
| 10 | fcopentryinvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scax_costbomcopentry |  | fentryid |
| 2 | idx_scax_cosbomcopentry_fid |  | fid |
