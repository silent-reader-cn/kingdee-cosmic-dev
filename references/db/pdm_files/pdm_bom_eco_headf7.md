# 工程变更单F7-pdm_bom_eco_headf7

## 工程变更单F7-主表 t_pdm_bom_eco

- **表名称：** 工程变更单F7-主表
- **表名：** t_pdm_bom_eco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fdisableuserid | fdisableuserid | int8 | 64 |  | √ | 0 |  |
| 4 | fischanged | 已变更 | bpchar | 1 |  | √ | '0' | 已变更 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplmecnid | fplmecnid | int8 | 64 |  | √ | 0 |  |
| 9 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 10 | fenabledate | fenabledate | timestamp | 0 |  |  | null |  |
| 11 | fisonlychangemainproduct | 仅变更主产品 | bpchar | 1 |  | √ | '0' | 仅变更主产品 |
| 12 | fdatasrctype | fdatasrctype | varchar | 5 |  | √ | ' ' |  |
| 13 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 16 | ftypeid | ftypeid | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 19 | fenableuserid | fenableuserid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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
| 2 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 3 | fecn | fecn | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fiscoproduct | fiscoproduct | bpchar | 1 |  | √ | '0' |  |
| 6 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0 |  |
| 7 | fchangetype | fchangetype | varchar | 5 |  | √ | ' ' |  |
| 8 | fmftbomid | fmftbomid | varchar | 50 |  | √ | ' ' |  |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | febomid | febomid | varchar | 50 |  | √ | ' ' |  |
| 11 | fproentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 12 | fisretainrepmat | fisretainrepmat | bpchar | 1 |  | √ | '0' |  |
| 13 | fisparticipatedeval | fisparticipatedeval | bpchar | 1 |  | √ | '0' |  |
| 14 | foldversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 16 | fecreasonid | 变更原因 | int8 | 64 |  | √ | 0 | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 17 | fexecmode | fexecmode | varchar | 30 |  | √ | ' ' |  |
| 18 | fentryversioncontrol | fentryversioncontrol | varchar | 30 |  | √ | ' ' |  |
| 19 | fplmecnentryid | fplmecnentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fecnversionid | fecnversionid | int8 | 64 |  | √ | 0 |  |
| 21 | fexecdate | fexecdate | timestamp | 0 |  |  | null |  |
| 22 | fbomuse | fbomuse | varchar | 36 |  | √ | ',A,B,C,D,' |  |
| 23 | fspecifynewbomnum | fspecifynewbomnum | varchar | 100 |  | √ | ' ' |  |
| 24 | fnewversionid | fnewversionid | int8 | 64 |  | √ | 0 |  |
| 25 | fnewbom | fnewbom | int8 | 64 |  | √ | 0 |  |
| 26 | fexecstatus | fexecstatus | varchar | 30 |  | √ | ' ' |  |
| 27 | fbomauxpropertyid | fbomauxpropertyid | int8 | 64 |  | √ | 0 |  |
| 28 | fecoapplybillno | fecoapplybillno | varchar | 50 |  | √ | '' |  |
| 29 | fecobomid | fecobomid | int8 | 64 |  | √ | 0 |  |
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
