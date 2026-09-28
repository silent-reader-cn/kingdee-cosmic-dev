# 物料质检信息-bd_inspect_cfg

## 物料质检信息-主表 t_bd_inspect_cfg

- **表名称：** 物料质检信息-主表
- **表名：** t_bd_inspect_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fosqcpflg | 产品委外检验 | bpchar | 1 |  | √ | '0' | 产品委外检验 |
| 4 | fmaterialid | 物料(冗余显示用，不支持业务逻辑) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | freturnsflg | 退货检验 | bpchar | 1 |  | √ | '0' | 退货检验 |
| 6 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | ffinishflg | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 9 | fproductretflg | 生产退料检验 | bpchar | 1 |  | √ | '0' | 生产退料检验 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fdeliveryflg | 发货检验 | bpchar | 1 |  | √ | '0' | 发货检验 |
| 12 | ffirstcontrolmode | 首检控制方式 | varchar | 5 |  | √ | 'A' | 首检控制方式,枚举: A :严格控制 B :非严格控制 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ffirstflag | 产品首检 | bpchar | 1 |  | √ | '0' | 产品首检 |
| 15 | fstatus | 质检信息数据状态 | varchar | 5 |  | √ | ' ' | 质检信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fxkallocationtype | 质检信息分配类型 | varchar | 30 |  | √ | ' ' | 质检信息分配类型,枚举: 1 :个性化 2 :共享型 |
| 21 | fqcpflg | 来料检验 | bpchar | 1 |  | √ | '0' | 来料检验 |
| 22 | fcreateorgid | 质检信息创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | foutsourcingretflg | 委外退料检验 | bpchar | 1 |  | √ | '0' | 委外退料检验 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fprodpatrolflag | 其他检验 | bpchar | 1 |  | √ | '0' | 其他检验 |
| 26 | fprocedureflg | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fiscontrolreturnmtrl | 严格控制从生产退料请检单发起退料 | bpchar | 1 |  | √ | '0' | 严格控制从生产退料请检单发起退料 |
| 29 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 30 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fmbdmasterid | 物料库存信息内码 | int8 | 64 |  | √ | 0 | 物料库存信息内码 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fctrlstrategy | 质检信息控制策略 | varchar | 5 |  | √ | '5' | 质检信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 35 | fisautonew | 自动新增 | bpchar | 1 |  | √ | '0' | 自动新增 |
| 36 | foemrecieveflg | 受托材料检验 | bpchar | 1 |  | √ | '0' | 受托材料检验 |
| 37 | fnocheckflg | 免检设置 | bpchar | 1 |  | √ | '0' | 免检设置 |
| 38 | fenable | 质检信息使用状态 | varchar | 5 |  | √ | ' ' | 质检信息使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 40 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fstockflg | 在库检验 | bpchar | 1 |  | √ | '0' | 在库检验 |
| 42 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_inspct_fcreatetime |  | fcreatetime |
| 2 | idx_t_bd_inspect_cfg_master |  | fmasterid |
| 3 | idx_t_bd_inspect_cfgbit |  | fbitindex |
| 4 | idx_t_bd_inspect_cfg_createorg |  | fcreateorgid |
| 5 | pk_t_bd_inspect_cfg |  | fid |
| 6 | idx_bd_inspct_fnumber |  | fnumber |
| 7 | idx_t_bd_inspect_cfgsrcid |  | fsourcedataid |

---

## 物料质检信息-使用范围位图表 t_bd_inspect_cfg_m

- **表名称：** 物料质检信息-使用范围位图表
- **表名：** t_bd_inspect_cfg_m

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
| 1 | pk_t_bd_inspect_cfg_m |  | forgid |

---

## 物料质检信息-多语言表 t_bd_inspect_cfg_l

- **表名称：** 物料质检信息-多语言表
- **表名：** t_bd_inspect_cfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_inspctl_fname |  | fname |
| 2 | idx_bd_inspctl_fid |  | fid,flocaleid |
| 3 | pk_t_bd_inspect_cfg_l |  | fpkid |

---

## 物料质检信息-使用范围表 t_bd_inspect_cfg_u

- **表名称：** 物料质检信息-使用范围表
- **表名：** t_bd_inspect_cfg_u

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
| 1 | idx_t_bd_inspect_cfg_u_uo |  | fuseorgid |
| 2 | pk_t_bd_inspect_cfg_u |  | fdataid,fuseorgid |

---

## 单据体-子表 t_bd_inspect_cfg_bt

- **表名称：** 单据体-子表
- **表名：** t_bd_inspect_cfg_bt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbd_inspectbt_fid |  | fid |
| 2 | pk_t_bd_inspect_cfg_bt |  | fentryid |

---

## 检验控制-来料检验-子表 t_bd_inspect_qcp

- **表名称：** 检验控制-来料检验-子表
- **表名：** t_bd_inspect_qcp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_inspct_fseq |  | fseq |
| 2 | idx_bd_inspct_fid |  | fid |
| 3 | pk_t_bd_inspect_qcp |  | fentryid |
