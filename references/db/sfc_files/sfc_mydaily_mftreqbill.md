# 航材(废弃)-sfc_mydaily_mftreqbill

## 航材(废弃)-主表 t_im_mdc_mftreqbills

- **表名称：** 航材(废弃)-主表
- **表名：** t_im_mdc_mftreqbills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fheadproject | fheadproject | int8 | 64 |  | √ | 0 |  |
| 5 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fapplyuserid | fapplyuserid | int8 | 64 |  | √ | 0 |  |
| 9 | finvorg | finvorg | int8 | 64 |  | √ | 0 |  |
| 10 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 11 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | funitsrctype | funitsrctype | varchar | 30 |  | √ | 'NULL' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcomment | fcomment | varchar | 512 |  | √ | ' ' |  |
| 18 | fsettlecurrency | fsettlecurrency | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbillcretype | fbillcretype | varchar | 50 |  | √ | ' ' |  |
| 23 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 24 | fmaterialtype | fmaterialtype | varchar | 50 |  | √ | ' ' |  |
| 25 | fprofessiona | fprofessiona | int8 | 64 |  | √ | 0 |  |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_mftreqbills_forgid |  | forgid |
| 2 | pk_im_mdc_mftreqbills |  | fid |
| 3 | idx_mdc_mftreqbills_fbillno |  | fbillno |

---

## 单据体-子表 t_im_mdc_mftreqentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_mftreqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | fsrcsystem | varchar | 50 |  | √ | ' ' |  |
| 3 | flogisticsbill | flogisticsbill | bpchar | 1 |  | √ | '0' |  |
| 4 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 9 | ffilenumber | ffilenumber | varchar | 50 |  | √ | ' ' |  |
| 10 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 13 | freplacegroup | freplacegroup | varchar | 50 |  | √ | ' ' |  |
| 14 | fdeliverdate | 配送时间 | timestamp | 0 |  |  | null | 配送时间 |
| 15 | fauditqty | 审批数量 | numeric | 23 | 10 | √ | 0 | 审批数量 |
| 16 | frowstatus | frowstatus | varchar | 50 |  | √ | ' ' |  |
| 17 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 20 | forderentryseq | 工单行号 | varchar | 50 |  | √ | ' ' | 工单行号 |
| 21 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 22 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 23 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 24 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 25 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 30 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 31 | forderno | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 32 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 33 | fmaterialmasterid | fmaterialmasterid | int8 | 64 |  | √ | 0 |  |
| 34 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 35 | flengthunit | flengthunit | int8 | 64 |  | √ | 0 |  |
| 36 | fqtyunit2nd | fqtyunit2nd | numeric | 23 | 10 | √ | 0 |  |
| 37 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 50 |  | √ | ' ' |  |
| 38 | fsupplymode | fsupplymode | varchar | 50 |  | √ | ' ' |  |
| 39 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 40 | fexpirydate | fexpirydate | timestamp | 0 |  |  | null |  |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 44 | fmaterialgroup | fmaterialgroup | int8 | 64 |  | √ | 0 |  |
| 45 | foutqty | 下推领料数量 | numeric | 23 | 10 | √ | 0 | 下推领料数量 |
| 46 | fbigintfield | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 47 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 48 | flotnumber | flotnumber | varchar | 50 |  | √ | ' ' |  |
| 49 | fuseoutbaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 50 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 51 | funit2ndid | funit2ndid | int8 | 64 |  | √ | 0 |  |
| 52 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 53 | fwmssstatus | 配送状态 | varchar | 50 |  | √ | ' ' | 配送状态,枚举: A :已配送 |
| 54 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 55 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 56 | forderentryid | 工单分录id | int8 | 64 |  | √ | 0 | 工单分录id |
| 57 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 58 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 59 | fworkcard | 工卡 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 60 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 61 | fuseoutqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 62 | ffullsize | ffullsize | bpchar | 1 |  | √ | '0' |  |
| 63 | foutinvorg | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 65 | fpickbaseqty | fpickbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 66 | fwidth | fwidth | numeric | 23 | 10 | √ | 0 |  |
| 67 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 68 | foutbaseqty | 下推领料基本数量 | numeric | 23 | 10 | √ | 0 | 下推领料基本数量 |
| 69 | fauditbaseqty | 审批基本数量 | numeric | 23 | 10 | √ | 0 | 审批基本数量 |
| 70 | fdelivercycle | fdelivercycle | int8 | 64 |  | √ | 0 |  |
| 71 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 72 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 73 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 74 | fdoctype | fdoctype | int8 | 64 |  | √ | 0 |  |
| 75 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 76 | fheight | fheight | numeric | 23 | 10 | √ | 0 |  |
| 77 | fbaseqty | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 78 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 79 | fwarehousechange | fwarehousechange | bpchar | 1 |  | √ | '0' |  |
| 80 | fsrcsysbillid | fsrcsysbillid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_req_fmainbillid |  | fmainbillid |
| 2 | idx_mdc_req_fmainbillentryid |  | fmainbillentryid |
| 3 | pk_im_mdc_mftreqentry |  | fentryid |
| 4 | idx_mdc_req_fid |  | fid |
| 5 | idx_mdc_req_fmaterielmasterid |  | fmaterielmasterid |
