# 条码参数-barcm_barcodeparam

## 条码参数-主表 t_barcm_bcparam

- **表名称：** 条码参数-主表
- **表名：** t_barcm_bcparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauxqtyalgo | 条码辅助数量算法 | bpchar | 1 |  | √ | ' ' | 条码辅助数量算法,枚举: 0 :按源单数量折算 1 :动态换算 |
| 3 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcondefbcruleid | 手工装箱默认容器条码规则： | int8 | 64 |  | √ | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 11 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 12 | fnoduplicateinonebox | 单箱不允许重复扫描 | bpchar | 1 |  | √ | '0' | 单箱不允许重复扫描 |
| 13 | fmatecodeconpack | 物料条码连续装箱（作废） | bpchar | 1 |  | √ | '0' | 物料条码连续装箱（作废） |
| 14 | fenableaudioplay | PDA语音提示 | bpchar | 1 |  | √ | '0' | PDA语音提示 |
| 15 | fmatbardefqty | 物料条码默认数量为1 | bpchar | 1 |  | √ | '0' | 物料条码默认数量为1 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fscanconfir | 出库扫描确认校验库存量 | bpchar | 1 |  | √ | 0 | 出库扫描确认校验库存量,枚举: 0 :不控制 1 :预警提示 2 :严格控制 |
| 20 | fsinglegennum | 单次条码生成总个数 | int4 | 32 |  | √ | 0 | 单次条码生成总个数 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsinglegensrcnum | 单次条码生成源单行数 | int4 | 32 |  | √ | 0 | 单次条码生成源单行数 |
| 23 | fpermitexceed | 允许超源单数量生成条码 | bpchar | 1 |  | √ | 0 | 允许超源单数量生成条码,枚举: 0 :不控制 1 :预警提示 2 :严格控制 |
| 24 | fprintinterval | 打印时间间隔(s) | int4 | 32 |  | √ | 0 | 打印时间间隔(s) |
| 25 | fnoduplicateinallbox | 跨箱不允许重复扫描 | bpchar | 1 |  | √ | '0' | 跨箱不允许重复扫描 |
| 26 | fisoutdeductmqty | 出库扣减主档数量 | bpchar | 1 |  | √ | '0' | 出库扣减主档数量 |
| 27 | fctrlstrategy | 控制策略 | bpchar | 3 |  | √ | ' ' | 控制策略,枚举: 7 :私有 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 30 | fsingleprintnum | 单次打印发送条数 | int4 | 32 |  | √ | 0 | 单次打印发送条数 |
| 31 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 32 | fdynparseqty | 动态解析默认数量为1 | bpchar | 1 |  | √ | '0' | 动态解析默认数量为1 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_barcm_bcparam_createorg |  | fcreateorgid |
| 2 | idx_t_barcm_bcparam_master |  | fmasterid |
| 3 | pk_barcm_bcparam |  | fid |
| 4 | idx_barcm_bcparam_number |  | fnumber |

---

## 条码解析参数-多语言表 t_barcm_bcparamentry_l

- **表名称：** 条码解析参数-多语言表
- **表名：** t_barcm_bcparamentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdescription | 说明（作废） | varchar | 255 |  | √ | ' ' | 说明（作废） |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcparamentry_fidflid |  | fentryid,flocaleid |
| 2 | pk_barcm_bcparamentry_l |  | fpkid |

---

## 条码解析参数-子表 t_barcm_bcparamentry

- **表名称：** 条码解析参数-子表
- **表名：** t_barcm_bcparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuseable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbarcodeparseruleid | 条码解析规则 | int8 | 64 |  | √ | 0 | [条码解析规则 barcm_barcodeparserule](../barcm_files/barcm_barcodeparserule.md) |
| 5 | fdescription | 说明（作废） | varchar | 255 |  | √ | ' ' | 说明（作废） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcparamentry |  | fentryid |
| 2 | idx_barcm_bcparamentry_fid |  | fid |

---

## 条码参数-多语言表 t_barcm_bcparam_l

- **表名称：** 条码参数-多语言表
- **表名：** t_barcm_bcparam_l

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
| 1 | idx_barcm_bcparam_fidflid |  | fid,flocaleid |
| 2 | pk_barcm_bcparam_l |  | fpkid |

---

## 条码参数-使用范围表 t_barcm_bcparam_u

- **表名称：** 条码参数-使用范围表
- **表名：** t_barcm_bcparam_u

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
| 1 | pk_t_barcm_bcparam_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_bcparam_u_uo |  | fuseorgid |
