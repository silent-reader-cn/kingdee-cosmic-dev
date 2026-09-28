# 工程变更维护（旧）-pdm_eco

## 组件-子表 t_pdm_ecomentry

- **表名称：** 组件-子表
- **表名：** t_pdm_ecomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fsupplytype | 供应类型 | bpchar | 5 |  | √ | ' ' | 供应类型,枚举: 10910 :本库存组织领料 10920 :跨库存组织调拨 10930 :跨库存组织领料 10940 :跨库存组织直送 |
| 4 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 5 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 6 | fissuemode | 领送料方式 | bpchar | 5 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11030 :看板 11050 :直送 11040 :不领料 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 9 | foperationnumber | 工序号 | varchar | 100 |  | √ | ' ' | 工序号 |
| 10 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 11 | fownertype | 供应方式 | varchar | 30 |  | √ | ' ' | 供应方式,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 12 | fbomentryid | 组件分录ID | int8 | 64 |  | √ | 0 | 组件分录ID |
| 13 | fmode | 行标识 | bpchar | 1 |  | √ | ' ' | 行标识,枚举: A :新增 B :变更前 C :变更后 D :删除 E :失效 |
| 14 | fleadtime | 提前期偏置时间(天) | numeric | 23 | 10 | √ | 0.0000000000 | 提前期偏置时间(天) |
| 15 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 16 | fisjumplevel | 是否跳层 | bpchar | 1 |  | √ | '0' | 是否跳层 |
| 17 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 18 | fmaterialattr | 物料属性 | varchar | 10 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 19 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 21 | fisreplaceplanmm | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 22 | fqtytype | 用量类型 | bpchar | 1 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 23 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 24 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 25 | fentryprocessseq | 序列号 | varchar | 30 |  | √ | ' ' | 序列号 |
| 26 | fentryisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 29 | fisbackflush | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 30 | fwarehouseid | 默认发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 31 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 32 | fownerid | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | flocationid | 默认发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 34 | foutorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 36 | ftimeunit | 时间单位 | bpchar | 1 |  | √ | ' ' | 时间单位,枚举: D :天 H :时 M :分 S :秒 |
| 37 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 38 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 39 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | freplaceplanid | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_ecomentry_pkey |  | fentryid |
| 2 | idx_pdm_ecomentry_fidfseq |  | fid,fseq |
| 3 | idx_pdm_ecomentry_fmaterialid |  | fmaterialid |
| 4 | idx_pdm_ecomentry_vdaterange |  | fvaliddate,finvaliddate |

---

## 阶梯用量-子表 t_pdm_ecoqtyentry

- **表名称：** 阶梯用量-子表
- **表名：** t_pdm_ecoqtyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbatchstartqty | 批量开始 | numeric | 23 | 10 | √ | 0.0000000000 | 批量开始 |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fsrcid | BOM阶梯用量ID | int8 | 64 |  | √ | 0 | BOM阶梯用量ID |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 6 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 7 | fisstepfix | 阶梯固定 | bpchar | 1 |  | √ | '0' | 阶梯固定 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 10 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 11 | fbatchendqty | 批量截止 | numeric | 23 | 10 | √ | 0.0000000000 | 批量截止 |
| 12 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_ecoqtyentry |  | fentryid |
| 2 | t_pdm_ecoqtyentry_pkey |  | fdetailid |

---

## 产品-子表 t_pdm_ecopentry

- **表名称：** 产品-子表
- **表名：** t_pdm_ecopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | ECN失效日期 | timestamp | 0 |  |  | null | ECN失效日期 |
| 3 | fecnversionid | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 4 | fecn | ECN版本 | varchar | 100 |  | √ | ' ' | ECN版本 |
| 5 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 6 | fexecdate | 实施日期 | timestamp | 0 |  |  | null | 实施日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnewversionid | 新版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 10 | fexecstatus | 实施状态 | bpchar | 1 |  | √ | ' ' | 实施状态,枚举: A :待实施 B :已实施 C :已失效 |
| 11 | fproentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 12 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | foldversionid | 旧版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 14 | fecreasonid | 变更原因 | int8 | 64 |  | √ | 0 | 变更原因 pdm_ecnreason |
| 15 | fexecmode | 实施方式 | bpchar | 1 |  | √ | ' ' | 实施方式,枚举: A :立即执行 B :指定日期 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fentryversioncontrol | 版本控制 | varchar | 30 |  | √ | ' ' | 版本控制,枚举: A :修改版本 B :顺延版本 C :指定版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_ecopentry_pkey |  | fentryid |
| 2 | idx_pdm_ecopentry_fbomid |  | fbomid |
| 3 | idx_pdm_ecopentry_fidfseq |  | fid,fseq |

---

## 组件-多语言表 t_pdm_ecomentry_l

- **表名称：** 组件-多语言表
- **表名：** t_pdm_ecomentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_ecomentry_l_pkey |  | fpkid |
| 2 | idx_pdm_ecomentry_l |  | fentryid,flocaleid |

---

## 工程变更维护（旧）-主表 t_pdm_eco

- **表名称：** 工程变更维护（旧）-主表
- **表名：** t_pdm_eco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 1 :按管控单元逐级分配 2 :按管控单元自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 12 | ftypeid | 变更对象类型 | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillno | 工程变更编号 | varchar | 60 |  | √ | ' ' | 工程变更编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fversioncontrol | 版本控制 | bpchar | 1 |  | √ | 'A' | 版本控制,枚举: A :修改版本 B :顺延版本 C :指定版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_eco_fbillno |  | fbillno |
| 2 | t_pdm_eco_pkey |  | fid |
| 3 | idx_pdm_eco_forgid |  | forgid |

---

## 安装位置-子表 t_pdm_ecosetupentry

- **表名称：** 安装位置-子表
- **表名：** t_pdm_ecosetupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 组件数量 | numeric | 23 | 10 | √ | 0.0000000000 | 组件数量 |
| 2 | fsrcid | BOM安装位置ID | int8 | 64 |  | √ | 0 | BOM安装位置ID |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_ecosetupentry_pkey |  | fdetailid |
| 2 | idx_pdm_ecosetupentry |  | fentryid |

---

## 工程变更维护（旧）-多语言表 t_pdm_eco_l

- **表名称：** 工程变更维护（旧）-多语言表
- **表名：** t_pdm_eco_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工程变更名称 | varchar | 100 |  | √ | ' ' | 工程变更名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_eco_l |  | fid,flocaleid |
| 2 | t_pdm_eco_l_pkey |  | fpkid |

---

## 安装位置-多语言表 t_pdm_ecosetupentry_l

- **表名称：** 安装位置-多语言表
- **表名：** t_pdm_ecosetupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 200 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_ecosetupentry_l_pkey |  | fpkid |
| 2 | idx_pdm_ecosetupentry_l |  | fdetailid,flocaleid |
