# 工序转移单(废弃)-sfc_protransferbill

## 转出信息-子表 t_sfc_ptfbilloutentry

- **表名称：** 转出信息-子表
- **表名：** t_sfc_ptfbilloutentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwarehousepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 3 | fbadqualifiedinbaseqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 4 | freverseavailableqty | 可逆向转移基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向转移基本数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foutreworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | ftransferredout | 转出地 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 9 | fbadconformitybaseqty | 不合格基本数量（入库信息） | numeric | 23 | 10 | √ | 0 | 不合格基本数量（入库信息） |
| 10 | foutprocess | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 11 | fpushwarehousebaseqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0 | 下推入库基本数量 |
| 12 | freversereceivebaseqty | 可逆向让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向让步接收基本数量 |
| 13 | freversereworkbaseqty | 可逆向返工基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向返工基本数量 |
| 14 | foutworkwastebaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 15 | fmanufacturebill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 16 | foutscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 17 | fouttype | 转出类别 | varchar | 50 |  | √ | ' ' | 转出类别,枚举: mpdm_workcentre :工作中心 bd_supplier :供应商 |
| 18 | fscrapinbaseqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 19 | freversequalifybaseqty | 可逆向合格基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向合格基本数量 |
| 20 | fconformityqty | 合格数量（入库信息） | numeric | 23 | 10 | √ | 0 | 合格数量（入库信息） |
| 21 | fdiscardqty | 报废数量（入库信息） | numeric | 23 | 10 | √ | 0 | 报废数量（入库信息） |
| 22 | favailablebaseqty | 可转基本数量 | numeric | 23 | 10 | √ | 0 | 可转基本数量 |
| 23 | finspectiontype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 24 | fdiscardbaseqty | 报废基本数量（入库信息） | numeric | 23 | 10 | √ | 0 | 报废基本数量（入库信息） |
| 25 | foutjunkbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 26 | foutoprunit | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fmanufactureentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 29 | foutreceivebaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 30 | foutjunkqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 31 | fbadconformityqty | 不合格数量（入库信息） | numeric | 23 | 10 | √ | 0 | 不合格数量（入库信息） |
| 32 | ftransferqty | 转移数量 | numeric | 23 | 10 | √ | 0 | 转移数量 |
| 33 | finsbaseunit | 基本单位（入库信息） | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fconformitybaseqty | 合格基本数量（入库信息） | numeric | 23 | 10 | √ | 0 | 合格基本数量（入库信息） |
| 35 | freversescrapbaseqty | 可逆向料废基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向料废基本数量 |
| 36 | freverseworkwastebaseqty | 可逆向工废基本数量 | numeric | 23 | 10 | √ | 0 | 可逆向工废基本数量 |
| 37 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :顺序转移 2 :跳序转移 3 :逆顺序转移 4 :逆跳序转移 |
| 38 | foutworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 39 | foutproductunit | 生产计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | foutqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 41 | foutreworkbaseqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 42 | favailableqty | 可转数量 | numeric | 23 | 10 | √ | 0 | 可转数量 |
| 43 | foutpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | foutreceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 45 | foutprocessid | 转出工序id | int8 | 64 |  | √ | 0 | [工序计划分录f7(废弃) sfc_manftech_f7](../sfc_files/sfc_manftech_f7.md) |
| 46 | foutprocessplan | 转出工序计划 | int8 | 64 |  | √ | 0 | [工序计划f7(废弃) sfc_manftech_head_f7](../sfc_files/sfc_manftech_head_f7.md) |
| 47 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | ftransferbaseqty | 转移基本数量 | numeric | 23 | 10 | √ | 0 | 转移基本数量 |
| 49 | fsrcbillentryid | 来源单据分录id | varchar | 50 |  | √ | ' ' | 来源单据分录id |
| 50 | foutqualifybaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 51 | foutscrapbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 52 | ftransfertype | 转移类型 | varchar | 50 |  | √ | ' ' | 转移类型,枚举: 11 :主组织-主组织 12 :主组织-协同组织 13 :主组织-供应商 21 :协同组织-主组织 22 :协同组织-协同组织 23 :协同组织-供应商 31 :供应商-主组织 32 :供应商-协同组织 33 :供应商-供应商 |
| 53 | fqualifiedinbaseqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 54 | finspectionbaseqty | 检验基本数量 | numeric | 23 | 10 | √ | 0 | 检验基本数量 |
| 55 | fpushinspectionbaseqty | 下推检验基本数量 | numeric | 23 | 10 | √ | 0 | 下推检验基本数量 |
| 56 | focostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_ptfbilloutentry_fk |  | fid |
| 2 | pk_sfc_ptfbilloutentry |  | fentryid |

---

## 转入信息-子表 t_sfc_ptfbillinentry

- **表名称：** 转入信息-子表
- **表名：** t_sfc_ptfbillinentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | finprocessplan | 转入工序计划 | int8 | 64 |  | √ | 0 | [工序计划f7(废弃) sfc_manftech_head_f7](../sfc_files/sfc_manftech_head_f7.md) |
| 4 | foutentryentityid | 转出行id | varchar | 50 |  | √ | ' ' | 转出行id |
| 5 | finprocess | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 6 | fintype | 转入类别 | varchar | 50 |  | √ | ' ' | 转入类别,枚举: mpdm_workcentre :工作中心 bd_supplier :供应商 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ficostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 9 | finprocessid | 转入工序id | int8 | 64 |  | √ | 0 | [工序计划分录f7(废弃) sfc_manftech_f7](../sfc_files/sfc_manftech_f7.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ftransferredin | 转入地 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_ptfbillinentry |  | fentryid |
| 2 | idx_sfc_ptfbillinentry_fk |  | fid |

---

## 工序转移单(废弃)-主表 t_sfc_protransferbill

- **表名称：** 工序转移单(废弃)-主表
- **表名：** t_sfc_protransferbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsrcbillid | 来源单据id | varchar | 50 |  | √ | ' ' | 来源单据id |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fremakes | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_protransfer_orgid |  | forgid |
| 2 | pk_sfc_protransferbill |  | fid |

---

## 工序转移单(废弃)-反写记录表 t_sfc_protransferbill_wb

- **表名称：** 工序转移单(废弃)-反写记录表
- **表名：** t_sfc_protransferbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_protransferbill_wb |  | fentryid |
| 2 | idx_sfc_protransferbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_sfc_ptfbilloutentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_ptfbilloutentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_ptfbilloutentry_lk_fk |  | fentryid |
| 2 | pk_sfc_ptfbilloutentry_lk |  | fpkid |

---

## 工序转移单(废弃)-关联追踪表 t_sfc_protransferbill_tc

- **表名称：** 工序转移单(废弃)-关联追踪表
- **表名：** t_sfc_protransferbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_protransferbill_tc_tid |  | ftid |
| 2 | pk_sfc_protransferbill_tc |  | fid |
| 3 | idx_sfc_protransferbill_tc_tbill |  | ftbillid |
