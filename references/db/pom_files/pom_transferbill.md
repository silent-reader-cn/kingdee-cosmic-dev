# 生产挪料单-pom_transferbill

## 生产挪料单-多语言表 t_pom_transfer_l

- **表名称：** 生产挪料单-多语言表
- **表名：** t_pom_transfer_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_transfer_l |  | fid,flocaleid |
| 2 | pk_t_pom_transfer_l |  | fpkid |

---

## 挪料明细单据体-分表 t_pom_transferentry_a

- **表名称：** 挪料明细单据体-分表
- **表名：** t_pom_transferentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasenumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 3 | funissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 4 | fstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 5 | fissuemode | 领送料方式 | varchar | 5 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 6 | fiscannegative | 退料 | varchar | 5 |  | √ | ' ' | 退料 |
| 7 | fgoodrejectedqty | 良品退料数量 | numeric | 23 | 10 | √ | 0 | 良品退料数量 |
| 8 | fnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 9 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 10 | fchildmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 11 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 12 | fprocessplan | 工序计划 | varchar | 50 |  | √ | ' ' | 工序计划 |
| 13 | fstandbaseqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 14 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | ' ' | 备料调拨 |
| 15 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 16 | fisjumplevel | 跳层 | varchar | 5 |  | √ | ' ' | 跳层 |
| 17 | fisreplace | 替代件 | bpchar | 1 |  | √ | ' ' | 替代件 |
| 18 | fchildauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fchildprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | frework | 返工 | varchar | 5 |  | √ | ' ' | 返工 |
| 21 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 22 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 23 | fchildmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 24 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fbasedenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 26 | fbadincomerejectedbaseqty | 来料不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料基本数量 |
| 27 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fiskeypart | 关键件 | varchar | 5 |  | √ | ' ' | 关键件 |
| 29 | fchildtracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 30 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 31 | fusebaseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 32 | freplacestrategy | 替代策略 | varchar | 5 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 33 | fchildbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 34 | funissuebaseqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |
| 35 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 39 | fretoverdrawnqty | 多领退回数量 | numeric | 23 | 10 | √ | 0 | 多领退回数量 |
| 40 | fretoverdrawnbaseqty | 多领退回基本数量 | numeric | 23 | 10 | √ | 0 | 多领退回基本数量 |
| 41 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 42 | fbadtaskrejectedqty | 作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料数量 |
| 43 | fdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 44 | fuseqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 45 | fbadincomerejectedqty | 来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料数量 |
| 46 | fgoodrejectedbaseqty | 良品退料基本数量 | numeric | 23 | 10 | √ | 0 | 良品退料基本数量 |
| 47 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fqtytype | 用量类型 | varchar | 5 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 49 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | ' ' | 替代主料 |
| 50 | fbadtaskrejectedbaseqty | 作业不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料基本数量 |
| 51 | fisbackflush | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 52 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 53 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 54 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_transferentry_a |  | fentryid |
| 2 | idx_pom_transferentry_a_fid |  | fid |

---

## 生产挪料单-主表 t_pom_transfer

- **表名称：** 生产挪料单-主表
- **表名：** t_pom_transfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fisgenerate | 是否生成 | bpchar | 1 |  | √ | ' ' | 是否生成 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpairqty | 挪料套数 | numeric | 23 | 10 | √ | 0 | 挪料套数 |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fintype | 转入类型 | bpchar | 1 |  | √ | ' ' | 转入类型,枚举: A :未领转入 B :欠料转入 C :成套转入 |
| 11 | fouttype | 转出类型 | bpchar | 1 |  | √ | ' ' | 转出类型,枚举: A :余料转出 B :超领转出 C :成套转出 |
| 12 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 0 :转出 1 :转入 |
| 16 | foutdate | 转出日期 | timestamp | 0 |  |  | null | 转出日期 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftransferwarehouseid | 中转仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 19 | ftransferflocationid | 中转仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 20 | findate | 转入日期 | timestamp | 0 |  |  | null | 转入日期 |
| 21 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_transfer_fno |  | fbillno |
| 2 | idx_pom_transfer_forg |  | forgid,fdeptid |
| 3 | pk_t_pom_transfer |  | fid |

---

## 挪料明细单据体-子表 t_pom_transferentry

- **表名称：** 挪料明细单据体-子表
- **表名：** t_pom_transferentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchildbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 3 | frowtype | 行类型 | varchar | 5 |  | √ | ' ' | 行类型,枚举: 0 :转出行 1 :转入行 |
| 4 | forderid | 生产工单id | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwipbaseqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 7 | ffeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 8 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 9 | ffeedingbaseqty | 补料基本数量 | numeric | 23 | 10 | √ | 0 | 补料基本数量 |
| 10 | fchildlicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 11 | fdemandbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 12 | ftaskstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | forderentryseq | 生产工单行号 | int4 | 32 |  | √ | 0 | 生产工单行号 |
| 15 | freturnbillno | 生产退料单编号 | varchar | 50 |  | √ | ' ' | 生产退料单编号 |
| 16 | fqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 17 | fchildbaseunitid | 子项基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 19 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | forderno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 21 | frejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 22 | fstockentryid | 用料清单分录id | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 23 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 24 | fwipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | foutqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 27 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 28 | ftransferqty | 挪料数量 | numeric | 23 | 10 | √ | 0 | 挪料数量 |
| 29 | forderentryid | 生产工单分录id | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 30 | foutbillno | 生产领料单编号 | varchar | 50 |  | √ | ' ' | 生产领料单编号 |
| 31 | fpid | 父Id | int8 | 64 |  | √ | 0 | 父Id |
| 32 | factissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 33 | foverissuecontrl | 转入超发控制 | varchar | 5 |  | √ | ' ' | 转入超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 34 | fchildmaterialid | 子项物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 35 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | frejectedbaseqty | 退料基本数量 | numeric | 23 | 10 | √ | 0 | 退料基本数量 |
| 37 | fcantransferbaseqty | 可挪基本数量 | numeric | 23 | 10 | √ | 0 | 可挪基本数量 |
| 38 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fstockid | 用料清单id | int8 | 64 |  | √ | 0 | [生产用料清单f7 pom_mftstockf7](../pom_files/pom_mftstockf7.md) |
| 40 | foutbillid | 生产领料单id | int8 | 64 |  | √ | 0 | 生产领料单id |
| 41 | foutentryseq | foutentryseq | varchar | 255 |  | √ | ' ' |  |
| 42 | foutbaseqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0 | 关联领料基本数量 |
| 43 | ftransferbaseqty | 挪料基本数量 | numeric | 23 | 10 | √ | 0 | 挪料基本数量 |
| 44 | fcantransferqty | 可挪数量 | numeric | 23 | 10 | √ | 0 | 可挪数量 |
| 45 | freturnentryseq | freturnentryseq | varchar | 255 |  | √ | ' ' |  |
| 46 | freturnbillid | 生产退料单id | int8 | 64 |  | √ | 0 | 生产退料单id |
| 47 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 48 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 49 | fscrapbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 50 | factissuebaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_transferentry |  | fentryid |
| 2 | idx_pom_transferentry_fid |  | fid |
