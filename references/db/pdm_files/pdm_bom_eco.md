# 工程变更单-pdm_bom_eco

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 1 :按管控单元逐级分配 2 :按管控单元自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 12 | ftypeid | 变更对象类型 | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillno | 工程变更编号 | varchar | 30 |  | √ | ' ' | 工程变更编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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

## 产品-子表 t_pdm_bomecopentry

- **表名称：** 产品-子表
- **表名：** t_pdm_bomecopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | ECN失效日期 | timestamp | 0 |  |  | null | ECN失效日期 |
| 3 | fecnversionid | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 4 | fecn | ECN版本 | varchar | 50 |  | √ | ' ' | ECN版本 |
| 5 | fexecdate | 实施日期 | timestamp | 0 |  |  | null | 实施日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbomuse | BOM用途 | varchar | 36 |  | √ | ',A,B,C,D,' | BOM用途,枚举: A :自制 B :委外 C :报价 D :组装 |
| 8 | fmftbomid | fmftbomid | varchar | 50 |  | √ | ' ' |  |
| 9 | fnewversionid | 新物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fnewbom | 新BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 12 | febomid | febomid | varchar | 50 |  | √ | ' ' |  |
| 13 | fexecstatus | 实施状态 | varchar | 30 |  | √ | ' ' | 实施状态,枚举: A :待实施 B :已实施 C :已失效 |
| 14 | fbomauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fproentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 16 | fecobomid | 变更BOMID | int8 | 64 |  | √ | 0 | 变更BOMID |
| 17 | foldversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 18 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 19 | fecreasonid | 变更原因 | int8 | 64 |  | √ | 0 | 变更原因 pdm_ecnreason |
| 20 | fexecmode | 实施方式 | varchar | 30 |  | √ | ' ' | 实施方式,枚举: A :立即执行 B :指定日期 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fentryversioncontrol | 生成新BOM | varchar | 30 |  | √ | ' ' | 生成新BOM,枚举: A :否 B :是 C :指定版本 D :初始版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_bomecopentry |  | fentryid |
| 2 | idx_pdm_bomecopentry_fid |  | fid |
