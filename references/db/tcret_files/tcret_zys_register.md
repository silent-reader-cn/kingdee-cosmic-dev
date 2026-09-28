# 资源税税源登记信息-tcret_zys_register

## 资源税税源登记信息-多语言表 t_tcret_zys_register_l

- **表名称：** 资源税税源登记信息-多语言表
- **表名：** t_tcret_zys_register_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 税源名称 | varchar | 200 |  | √ | ' ' | 税源名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_zys_register_l_0 |  | fid,flocaleid |
| 2 | pk_tcret_zys_register_l |  | fpkid |

---

## 资源税税源登记信息-主表 t_tcret_zys_register

- **表名称：** 资源税税源登记信息-主表
- **表名：** t_tcret_zys_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :按月申报 season :按季申报 count :按次申报 |
| 3 | fname | 税源名称 | varchar | 200 |  | √ | ' ' | 税源名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fstartdate | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 税源编号 | varchar | 100 |  | √ | ' ' | 税源编号 |
| 15 | ftaxoffice | 税源所属税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_zys_register_fnumber |  | fnumber |
| 2 | pk_tcret_zys_register |  | fid |

---

## 单据体-子表 t_tcret_zys_register_en

- **表名称：** 单据体-子表
- **表名：** t_tcret_zys_register_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 3 | ftaxitem | 税目 | int8 | 64 |  | √ | 0 | 资源税税率表分录 tpo_zys_taxitem_entry |
| 4 | ftaxsubitem | 子目 | varchar | 50 |  | √ | ' ' | 子目,枚举: yk :原矿 xk :选矿 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flevy | 计征方式 | varchar | 50 |  | √ | ' ' | 计征方式,枚举: cjjz :从价计征 cljz :从量计征 |
| 8 | funit | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_zys_register_en_fk |  | fid |
| 2 | pk_tcret_zys_register_en |  | fentryid |
