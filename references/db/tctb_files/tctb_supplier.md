# 供应商-tctb_supplier

## 供应商-多语言表 t_tctb_supplier_l

- **表名称：** 供应商-多语言表
- **表名：** t_tctb_supplier_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_supplier_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_supplier_l |  | fpkid |

---

## 适用税收协议信息-子表 t_tctb_suppliertreaty

- **表名称：** 适用税收协议信息-子表
- **表名：** t_tctb_suppliertreaty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 4 | ftreatynameid | 适用税收协议名称 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcnfep_bizdef_entry |
| 5 | ftreatytaxrate | 税收协定优惠税率 | varchar | 50 |  | √ | ' ' | 税收协定优惠税率,枚举: 0% :0% 5% :5% 7% :7% 8% :8% 10% :10% |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ftreatyagreementid | 适用税收协定条款 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcnfep_bizdef_entry |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_suppliertreaty |  | fentryid |
| 2 | idx_tctb_suppliertreaty_fk |  | fid |

---

## 供应商-主表 t_tctb_supplier

- **表名称：** 供应商-主表
- **表名：** t_tctb_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | ftaxfilename | 税号的证件名称 | varchar | 100 |  | √ | ' ' | 税号的证件名称 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_supplierid |  | fsupplierid |
| 2 | pk_tctb_supplier |  | fid |
