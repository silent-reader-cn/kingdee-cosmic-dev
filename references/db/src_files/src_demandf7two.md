# 项目立项分录F7-src_demandf7two

## 标的附件-附件表 t_src_purlistentry_fj

- **表名称：** 标的附件-附件表
- **表名：** t_src_purlistentry_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlistentry_fj_bid |  | fbasedataid |
| 2 | pk_src_purlistentry_fj |  | fpkid |
| 3 | idx_src_purlistentry_fj_fid |  | fentryid |

---

## 项目立项分录F7-主表 t_src_notyearinfo

- **表名称：** 项目立项分录F7-主表
- **表名：** t_src_notyearinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 项目立项 | int8 | 64 |  | √ | 0 | [项目立项F7 src_demandnotwo](../src_files/src_demandnotwo.md) |
| 2 | ftextfield1 | ftextfield1 | varchar | 50 |  | √ | ' ' |  |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fsupplierno1 | fsupplierno1 | int8 | 64 |  | √ | 0 |  |
| 6 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 7 | farrivedate1 | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 11 | fprojectno1 | fprojectno1 | varchar | 50 |  | √ | ' ' |  |
| 12 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcheckboxfield1 | fcheckboxfield1 | bpchar | 1 |  | √ | ' ' |  |
| 14 | fk_sf_city | fk_sf_city | int8 | 64 |  | √ | 0 |  |
| 15 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 16 | flinenumber1 | 需求申请单行号 | varchar | 50 |  | √ | ' ' | 需求申请单行号 |
| 17 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | frfqbillno | frfqbillno | varchar | 50 |  | √ | ' ' |  |
| 19 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 20 | freqsource11 | 需求来源 | varchar | 30 |  | √ | ' ' | 需求来源,枚举: 1 :寻源申请 2 :采购申请 3 :项目立项 4 :项目启动 |
| 21 | fmaterial1 | 标的编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | findicate1 | 需求频次 | varchar | 30 |  | √ | ' ' | 需求频次,枚举: 1 :一次性需求 2 :持续性需求 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fprice3 | fprice3 | numeric | 23 | 10 | √ | 0 |  |
| 27 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 28 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 30 | freqqty2 | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 31 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 32 | fmaterialname1 | 标的编码 | varchar | 100 |  | √ | ' ' | 标的编码 |
| 33 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 34 | fk_sf_companycode | fk_sf_companycode | int8 | 64 |  | √ | 0 |  |
| 35 | funit2 | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | freqdescribe | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 38 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fprice2 | fprice2 | numeric | 23 | 10 | √ | 0 |  |
| 40 | fyearswitch | fyearswitch | bpchar | 1 |  | √ | ' ' |  |
| 41 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 42 | freqorg1 | freqorg1 | int8 | 64 |  | √ | 0 |  |
| 43 | fentryamount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 44 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 45 | fsrcbillno | 源单单号 | varchar | 50 |  | √ | ' ' | 源单单号 |
| 46 | ftaxamount2 | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 47 | fcontractline | fcontractline | int8 | 64 |  | √ | 0 |  |
| 48 | fk_sf_place | fk_sf_place | int8 | 64 |  | √ | 0 |  |
| 49 | fspecialreason | 标的描述 | varchar | 1024 |  |  | ' ' | 标的描述 |
| 50 | fmaterialmodel1 | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 51 | fprice | 预估未税单价 | numeric | 23 | 10 | √ | 0 | 预估未税单价 |
| 52 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 53 | fapplyno1 | fapplyno1 | varchar | 50 |  | √ | ' ' |  |
| 54 | ftaxprice1 | 预估含税单价 | numeric | 23 | 10 | √ | 0 | 预估含税单价 |
| 55 | fsceneid | 寻源场景 | int8 | 64 |  | √ | 0 | [寻源场景F7 src_demandscene](../src_files/src_demandscene.md) |
| 56 | fcategory2 | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 57 | fspecialpurreason | fspecialpurreason | varchar | 50 |  | √ | ' ' |  |
| 58 | fcontractnold | fcontractnold | int8 | 64 |  | √ | 0 |  |
| 59 | fld | fld | varchar | 50 |  | √ | ' ' |  |
| 60 | fmaterial1code | 标的编码 | varchar | 50 |  | √ | ' ' | 标的编码 |
| 61 | fecpno | fecpno | varchar | 50 |  | √ | ' ' |  |
| 62 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 63 | fmaterialgroup1 | fmaterialgroup1 | int8 | 64 |  | √ | 0 |  |
| 64 | freqtype1 | freqtype1 | int8 | 64 |  | √ | 0 |  |
| 65 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 66 | fentrystatus11 | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :暂存 B :未执行 C :已执行 D :已终止 |
| 67 | fqty1 | fqty1 | numeric | 23 | 10 | √ | 0 |  |
| 68 | fprojectname1 | fprojectname1 | varchar | 50 |  | √ | ' ' |  |
| 69 | fprice12 | fprice12 | numeric | 23 | 10 | √ | 0 |  |
| 70 | fprice13 | fprice13 | numeric | 23 | 10 | √ | 0 |  |
| 71 | fprice14 | fprice14 | numeric | 23 | 10 | √ | 0 |  |
| 72 | fprice15 | fprice15 | numeric | 23 | 10 | √ | 0 |  |
| 73 | fapplyno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 74 | fsuppliername1 | fsuppliername1 | varchar | 50 |  | √ | ' ' |  |
| 75 | fk_sf_busiarea | fk_sf_busiarea | int8 | 64 |  | √ | 0 |  |
| 76 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_notyearinfo_fid |  | fid |
| 2 | idx_src_notyearinfo_pid |  | fprojectid |
| 3 | idx_src_notyearinfo_applyno |  | fapplyno |
| 4 | pk_src_notyearinfo |  | fentryid |
