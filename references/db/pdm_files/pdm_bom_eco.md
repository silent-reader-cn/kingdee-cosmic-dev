# 工程变更单-pdm_bom_eco

## 关联子实体-子表 t_pdm_bom_eco_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pdm_bom_eco_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_bom_eco_lk |  | fpkid |
| 2 | idx_pdm_bom_eco_lk_fk |  | fid |

---

## 工程变更单-关联追踪表 t_pdm_bom_eco_tc

- **表名称：** 工程变更单-关联追踪表
- **表名：** t_pdm_bom_eco_tc

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
| 1 | pk_pdm_bom_eco_tc |  | fid |
| 2 | idx_pdm_bom_eco_tc_tbill |  | ftbillid |
| 3 | idx_pdm_bom_eco_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pdm_bomecopentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pdm_bomecopentry_lk

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
| 1 | pk_pdm_bomecopentry_lk |  | fpkid |
| 2 | idx_pdm_bomecopentry_lk_fk |  | fentryid |

---

## 产品-多语言表 t_pdm_bomecopentry_l

- **表名称：** 产品-多语言表
- **表名：** t_pdm_bomecopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_bomecopentry_l |  | fentryid,flocaleid |
| 2 | pk_pdm_bomecopentry_l |  | fpkid |

---

## 工程变更单-多语言表 t_pdm_bom_eco_l

- **表名称：** 工程变更单-多语言表
- **表名：** t_pdm_bom_eco_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_bom_eco_l_il |  | fid,flocaleid |
| 2 | pk_pdm_bom_eco_l |  | fpkid |

---

## 工程变更单-主表 t_pdm_bom_eco

- **表名称：** 工程变更单-主表
- **表名：** t_pdm_bom_eco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fischanged | 已变更 | bpchar | 1 |  | √ | '0' | 已变更 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplmecnid | PLMECNID | int8 | 64 |  | √ | 0 | PLMECNID |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 11 | fisonlychangemainproduct | 仅变更主产品 | bpchar | 1 |  | √ | '0' | 仅变更主产品 |
| 12 | fdatasrctype | 单据来源 | varchar | 5 |  | √ | ' ' | 单据来源,枚举: A :ERP创建 B :API传入 C :PLM传入 |
| 13 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fctrlstrategy | 控制策略（废弃） | varchar | 30 |  | √ | ' ' | 控制策略（废弃）,枚举: 1 :按管控单元逐级分配 2 :按管控单元自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 16 | ftypeid | 变更对象类型（废弃） | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenable | 使用状态（废弃） | varchar | 30 |  | √ | ' ' | 使用状态（废弃）,枚举: 0 :禁用 1 :可用 |
| 19 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_bom_eco |  | fid |
| 2 | idx_pdm_bom_eco_fbillno |  | fbillno |

---

## 工程变更单-反写记录表 t_pdm_bom_eco_wb

- **表名称：** 工程变更单-反写记录表
- **表名：** t_pdm_bom_eco_wb

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
| 1 | pk_pdm_bom_eco_wb |  | fentryid |
| 2 | idx_pdm_bom_eco_wb_fk |  | fid |

---

## 产品-子表 t_pdm_bomecopentry

- **表名称：** 产品-子表
- **表名：** t_pdm_bomecopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | ECN失效日期 | timestamp | 0 |  |  | null | ECN失效日期 |
| 3 | fecn | ECN版本 | varchar | 50 |  | √ | ' ' | ECN版本 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 6 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 7 | fchangetype | 变更类型 | varchar | 5 |  | √ | ' ' | 变更类型,枚举: A :立即变更 B :用完旧料 C :指定日期变更 |
| 8 | fmftbomid | fmftbomid | varchar | 50 |  | √ | ' ' |  |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | febomid | febomid | varchar | 50 |  | √ | ' ' |  |
| 11 | fproentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 12 | fisretainrepmat | 保留替代物料 | bpchar | 1 |  | √ | '0' | 保留替代物料 |
| 13 | fisparticipatedeval | 已参与变更评估 | bpchar | 1 |  | √ | '0' | 已参与变更评估 |
| 14 | foldversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fvaliddate | 子项生效时间 | timestamp | 0 |  |  | null | 子项生效时间 |
| 16 | fecreasonid | 变更原因 | int8 | 64 |  | √ | 0 | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 17 | fexecmode | 实施方式（废弃） | varchar | 30 |  | √ | ' ' | 实施方式（废弃）,枚举: A :立即执行 B :指定日期 |
| 18 | fentryversioncontrol | 生成新BOM | varchar | 30 |  | √ | ' ' | 生成新BOM,枚举: A :否 B :是 C :指定版本 D :初始版本 |
| 19 | fplmecnentryid | PLMECN分录ID | int8 | 64 |  | √ | 0 | PLMECN分录ID |
| 20 | fecnversionid | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 21 | fexecdate | 实施日期（废弃） | timestamp | 0 |  |  | null | 实施日期（废弃） |
| 22 | fbomuse | BOM用途 | varchar | 36 |  | √ | ',A,B,C,D,' | BOM用途,枚举: A :自制 B :委外 C :报价 D :组装 |
| 23 | fspecifynewbomnum | 指定新BOM编码 | varchar | 100 |  | √ | ' ' | 指定新BOM编码 |
| 24 | fnewversionid | 新物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fnewbom | 新BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 26 | fexecstatus | 实施状态（废弃） | varchar | 30 |  | √ | ' ' | 实施状态（废弃）,枚举: A :待实施 B :已实施 C :已失效 |
| 27 | fbomauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | fecoapplybillno | 工程变更申请单 | varchar | 50 |  | √ | '' | 工程变更申请单 |
| 29 | fecobomid | 变更BOMID | int8 | 64 |  | √ | 0 | 变更BOMID |
| 30 | fisdisableoldbom | 禁用旧BOM | bpchar | 1 |  | √ | '0' | 禁用旧BOM |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_bomecopentry |  | fentryid |
| 2 | idx_pdm_bomecopentry_fid |  | fid |
