# 制造BOMf7(废弃)-sfc_mftbomf7

## 联副产品-子表 t_pdm_mftbomcopentry

- **表名称：** 联副产品-子表
- **表名：** t_pdm_mftbomcopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fprocesssequence | fprocesssequence | int4 | 32 |  | √ | 0 |  |
| 4 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 9 | foperationnumber | foperationnumber | varchar | 50 |  | √ | ' ' |  |
| 10 | fprodunitid | fprodunitid | int8 | 64 |  | √ | 0 |  |
| 11 | ftype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 12 | fentrymasterid | fentrymasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fprocessnumber | fprocessnumber | int4 | 32 |  | √ | 0 |  |
| 16 | fprodqty | fprodqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | foperationid | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 19 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomcopentry_fid |  | fid |
| 2 | t_pdm_mftbomcopentry_pkey |  | fentryid |

---

## 制造BOMf7(废弃)-主表 t_pdm_mftbom

- **表名称：** 制造BOMf7(废弃)-主表
- **表名：** t_pdm_mftbom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | BOM分组 | int8 | 64 |  | √ | 0 | [BOM分组 mpdm_bomgroup](../mpdm_files/mpdm_bomgroup.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fyieldrate | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsalorderentryseq | fsalorderentryseq | varchar | 50 |  | √ | ' ' |  |
| 9 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 10 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 11 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 13 | fsalorderid | fsalorderid | int8 | 64 |  | √ | 0 |  |
| 14 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 15 | fqtybaseunit | fqtybaseunit | int8 | 64 |  | √ | 0 |  |
| 16 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdatasource | fdatasource | bpchar | 1 |  | √ | 1 |  |
| 21 | fnumber | BOM编码 | varchar | 100 |  | √ | ' ' | BOM编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |
| 25 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 26 | fsalorderno | fsalorderno | varchar | 50 |  |  | ' ' |  |
| 27 | fsalorderentryid | fsalorderentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 30 | fecn | fecn | int8 | 64 |  | √ | 0 |  |
| 31 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 32 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 33 | fbonded | fbonded | bpchar | 1 |  | √ | '0' |  |
| 34 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 38 | fplmmaterialver | fplmmaterialver | varchar | 50 |  | √ | ' ' |  |
| 39 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | freplacenoid | 替代号 | int8 | 64 |  | √ | 0 | [BOM替代号 mpdm_replaceno](../mpdm_files/mpdm_replaceno.md) |
| 41 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fecnversion | fecnversion | varchar | 50 |  | √ | ' ' |  |
| 45 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 46 | fmatid | fmatid | int8 | 64 |  | √ | 0 |  |
| 47 | fbomuse | fbomuse | varchar | 36 |  | √ | ',A,B,C,D,' |  |
| 48 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 49 | fplmbomid | fplmbomid | int8 | 64 |  | √ | 0 |  |
| 50 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 51 | fsrcsuperbomid | fsrcsuperbomid | int8 | 64 |  | √ | 0 |  |
| 52 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 53 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 54 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbom_pkey |  | fid |
| 2 | idx_t_pdm_mftbom_createorg |  | fcreateorgid |
| 3 | idx_t_pdm_mftbom_master |  | fmasterid |
| 4 | idx_pdm_mftbom_compt3 |  | fmatid,ftypeid,fstatus,fenable |
| 5 | idx_pdm_mftbom_compt1 |  | fmatid,ftypeid,fstatus,fenable,freplacenoid,fversionid |
| 6 | idx_pdm_mftbom_compt2 |  | fmatid,ftypeid,fstatus,fenable,freplacenoid |
| 7 | idx_pdm_mftbom_fmaterial |  | fmaterialid |
| 8 | idx_pdm_mftbom_fnumber |  | fnumber |

---

## 阶梯用量-子表 t_pdm_mftbomqtyentry

- **表名称：** 阶梯用量-子表
- **表名：** t_pdm_mftbomqtyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbatchstartqty | 批量开始 | numeric | 23 | 10 | √ | 0.0000000000 | 批量开始 |
| 2 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 3 | fbatchendqty | 批量截止 | numeric | 23 | 10 | √ | 0.0000000000 | 批量截止 |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 6 | fisstepfix | 是否阶梯固定 | bpchar | 1 |  | √ | '0' | 是否阶梯固定 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbomqtyentry_pkey |  | fdetailid |
| 2 | idx_pdm_mftbomqtyentry_fk |  | fentryid |

---

## 组件信息-子表 t_pdm_mftbomentry

- **表名称：** 组件信息-子表
- **表名：** t_pdm_mftbomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fissuemode | fissuemode | varchar | 30 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | freppriority | freppriority | int8 | 64 |  | √ | 0 |  |
| 6 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 7 | fecnverion | fecnverion | varchar | 50 |  | √ | ' ' |  |
| 8 | foperatemrp | foperatemrp | varchar | 30 |  | √ | ' ' |  |
| 9 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 10 | fchilddenominator | fchilddenominator | numeric | 23 | 10 | √ | 0 |  |
| 11 | fplmbomentryid | fplmbomentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 13 | fentryecnid | fentryecnid | varchar | 100 |  | √ | ' ' |  |
| 14 | fentrymatid | fentrymatid | int8 | 64 |  | √ | 0 |  |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 18 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fentrychildtype | fentrychildtype | varchar | 30 |  | √ | ' ' |  |
| 21 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 22 | fecnvaliddate | fecnvaliddate | timestamp | 0 |  |  | null |  |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 26 | frepacetype | frepacetype | varchar | 50 |  | √ | ' ' |  |
| 27 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 28 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 29 | fismodifiable | fismodifiable | bpchar | 1 |  | √ | '0' |  |
| 30 | foutorgid | foutorgid | int8 | 64 |  | √ | 0 |  |
| 31 | ftimeunit | ftimeunit | varchar | 30 |  | √ | ' ' |  |
| 32 | fisoptional | fisoptional | bpchar | 1 |  | √ | '0' |  |
| 33 | fentrymasterid | fentrymasterid | int8 | 64 |  | √ | 0 |  |
| 34 | fisreplaceshow | fisreplaceshow | bpchar | 1 |  | √ | '0' |  |
| 35 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 36 | fsupplyorgid | fsupplyorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fentryecn | fentryecn | int8 | 64 |  | √ | 0 |  |
| 39 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 40 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 41 | fiskey | fiskey | bpchar | 1 |  | √ | '0' |  |
| 42 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 43 | freplacemode | freplacemode | varchar | 5 |  | √ | ' ' |  |
| 44 | fchildnumerator | fchildnumerator | numeric | 23 | 10 | √ | 0 |  |
| 45 | foperationnumber | foperationnumber | varchar | 50 |  | √ | ' ' |  |
| 46 | fleadtime | fleadtime | int8 | 64 |  | √ | 0 |  |
| 47 | fmaterialattr | fmaterialattr | varchar | 30 |  | √ | ' ' |  |
| 48 | foutlocationid | foutlocationid | int8 | 64 |  | √ | 0 |  |
| 49 | fentryconfigcode | fentryconfigcode | int8 | 64 |  | √ | 0 |  |
| 50 | fisreplaceplanmm | fisreplaceplanmm | bpchar | 1 |  | √ | '0' |  |
| 51 | fchildunitid | fchildunitid | int8 | 64 |  | √ | 0 |  |
| 52 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 53 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 54 | fecnno | fecnno | varchar | 50 |  | √ | ' ' |  |
| 55 | fisbackflush | fisbackflush | varchar | 30 |  | √ | ' ' |  |
| 56 | fisreplaceable | fisreplaceable | bpchar | 1 |  | √ | '0' |  |
| 57 | fprovidetype | fprovidetype | int8 | 64 |  | √ | 0 |  |
| 58 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 59 | ftype | 组件类型 | varchar | 30 |  | √ | ' ' | 组件类型,枚举: A :库存 |
| 60 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 61 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 62 | fisstockalloc | fisstockalloc | bpchar | 1 |  | √ | '0' |  |
| 63 | freplaceplanstrategy | freplaceplanstrategy | varchar | 10 |  | √ | ' ' |  |
| 64 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 65 | fprovideorgid | fprovideorgid | int8 | 64 |  | √ | 0 |  |
| 66 | fisselectable | fisselectable | bpchar | 1 |  | √ | '0' |  |
| 67 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 68 | fisbackflushnew | fisbackflushnew | varchar | 30 |  | √ | ' ' |  |
| 69 | freplaceplanid | freplaceplanid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomentry_fid |  | fid |
| 2 | idx_pdm_mftbomentry_m1 |  | fmaterialid |
| 3 | t_pdm_mftbomentry_pkey |  | fentryid |
| 4 | idx_pdm_mftbomentry_c2 |  | fid,finvaliddate |
| 5 | idx_pdm_mftbomentry_c1 |  | fid,fvaliddate,finvaliddate |
| 6 | idx_pdm_mftbomentry_c3 |  | fid,finvaliddate,fissuemode |

---

## 安装位置-子表 t_pdm_mftbomsetupentry

- **表名称：** 安装位置-子表
- **表名：** t_pdm_mftbomsetupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 组件数量 | numeric | 23 | 10 | √ | 0.0000000000 | 组件数量 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomsetupentry_fk |  | fentryid |
| 2 | t_pdm_mftbomsetupentry_pkey |  | fdetailid |

---

## 安装位置-多语言表 t_pdm_mftbomsetupentry_l

- **表名称：** 安装位置-多语言表
- **表名：** t_pdm_mftbomsetupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 2000 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomsetupentry_l_el |  | fdetailid,flocaleid |
| 2 | t_pdm_mftbomsetupentry_l_pkey |  | fpkid |

---

## 制造BOMf7(废弃)-使用范围表 t_pdm_mftbom_u

- **表名称：** 制造BOMf7(废弃)-使用范围表
- **表名：** t_pdm_mftbom_u

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
| 1 | t_pdm_mftbom_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_mftbom_u_uo |  | fuseorgid |

---

## 制造BOMf7(废弃)-使用范围位图表 t_pdm_mftbom_m

- **表名称：** 制造BOMf7(废弃)-使用范围位图表
- **表名：** t_pdm_mftbom_m

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
| 1 | pk_t_pdm_mftbom_m |  | forgid |

---

## 制造BOMf7(废弃)-多语言表 t_pdm_mftbom_l

- **表名称：** 制造BOMf7(废弃)-多语言表
- **表名：** t_pdm_mftbom_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbom_l_pkey |  | fpkid |
| 2 | idx_pdm_mftbom_l_fid |  | fid,flocaleid |
